"""Adds tab-completion to Python's somewhat verbose super() construct.

Based on https://github.com/clarabstract/SuperPython

"""
import sublime
import sublime_plugin


class SuperPythonComplete(sublime_plugin.EventListener):

    def find_closest_regions(self, view, scope, min_indent, max_row):
        """Search closest scope upper than current."""
        matches = view.find_by_selector(scope)
        matches = [m for m in matches
                   if (self.get_indent(view, m) < min_indent
                       and max_row > self.get_row(view, m))]
        return matches[-1]

    def get_indent(self, view, region):
        """Get size of indentation for 'region'.

        Returns:
            int: Size of indentation for 'region'

        """
        line = view.substr(view.line(region))
        return sum(self.tab_size if space == '\t' else 1
                   for space in line.replace(line.lstrip(), ''))

    def get_row(self, view, region):
        """Get number of first row for 'region'.

        Returns:
            int: Number of first row for 'region'

        """
        return view.rowcol(region.begin())[0]

    def on_activated(self, view):
        self.tab_size = view.settings().get('tab_size')

    def on_query_completions(self, view, prefix, locations):
        if prefix != 'super':
            return

        point = locations[0]

        # Work only in python
        if not view.match_selector(point, 'source.python'):
            return

        target = sublime.Region(point, point)
        indent = self.get_indent(view, target)

        # We are on the top of indent hierarchy level. Do nothing.
        if indent == 0:
            return

        row = self.get_row(view, target)

        try:
            fn_region = self.find_closest_regions(
                view, 'entity.name.function.python', indent, row)
            fn_params_region = self.find_closest_regions(
                view, 'meta.function.parameters.python', indent, row)
        except IndexError:
            # We could't find some scopes
            return

        fn_name = view.substr(fn_region).strip()

        fn_params = view.substr(view.line(fn_params_region))
        start = fn_params.find('(') + 1
        end = fn_params.find(')', start)
        fn_params = fn_params[start:end].strip()

        fn_args = []
        args_splitter = ','
        kwargs_splitter = '='
        for param in fn_params.split(args_splitter):
            if param in ('cls', 'self'):
                continue
            params = param.strip().split(kwargs_splitter)
            param = params[0]
            if len(params) == 2:
                param += kwargs_splitter + param
            fn_args.append(param)

        fn_args = (args_splitter + ' ').join(fn_args)

        replacement = 'super()'
        replacement += '.{fn_name}(${{1:{fn_args}}})'
        replacement = replacement.format(fn_name=fn_name, fn_args=fn_args)

        return [(prefix, replacement)]
