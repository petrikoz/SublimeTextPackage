# -*- coding: utf-8 -*-

import os

import sublime
import sublime_plugin


class DeleteFileCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        if self.is_enabled():
            file = self.view.file_name()
            os.remove(file)
            sublime.status_message('Deleted file: %s' % file)

    def is_enabled(self):
        return os.path.isfile(self.view.file_name())
