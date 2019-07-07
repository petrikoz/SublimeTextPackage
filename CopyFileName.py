# -*- coding: utf-8 -*-

import os

import sublime
import sublime_plugin


class CopyFileNameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        if self.is_enabled():
            filename = os.path.basename(self.view.file_name())
            sublime.set_clipboard(filename)
            sublime.status_message('Copied file name: %s' % filename)

    def is_enabled(self):
        return bool(self.view.file_name())
