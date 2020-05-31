# -*- coding: utf-8 -*- 
# !/usr/bin/env python3

# Name: main.py
# Author: https://github.com/536
# Create Time: 2020-05-24 20:43
import sys
from math import ceil

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QStyleFactory

from interface.ui import UI
from libs.png2ico import png2ico


class CommonHelper(object):
    @staticmethod
    def read(style):
        with open(style, mode='r', encoding='utf-8') as f:
            return f.read()


class ThreadConvert(QThread):
    signal_statusbar = pyqtSignal(int)
    signal_progress = pyqtSignal(int)

    def __init__(self, files, key, parent=None):
        super().__init__(parent)

        self.files = files
        self.key = key

    def run(self):
        for num, file in enumerate(self.files):
            self.signal_progress.emit(ceil((num + 1) * 100 / len(self.files)))
            self.key(file)
        self.signal_statusbar.emit(len(self.files))


class MainWindow(UI):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.thread_convert = None

    def on_button_convert_clicked(self):
        if self.files:
            self.thread_convert = ThreadConvert(self.files, png2ico)
            self.progress.setVisible(True)
            self.thread_convert.signal_progress.connect(self.update_progress)
            self.thread_convert.signal_statusbar.connect(self.update_statusbar)
            self.thread_convert.start()
            self.files = None
            self.button_convert.setDisabled(True)


if __name__ == '__main__':
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    app = QApplication(sys.argv)

    win = MainWindow()
    style_sheet = CommonHelper.read('./sources/style.qss')
    win.setStyleSheet(style_sheet)
    win.show()
    sys.exit(app.exec_())
