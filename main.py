# -*- coding: utf-8 -*- 
# !/usr/bin/env python3

# Name: main.py
# Author: https://github.com/536
# Create Time: 2020-05-24 20:43
import sys

import PythonMagick  # https://www.lfd.uci.edu/~gohlke/pythonlibs/#pythonmagick

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from interface.ui import UI


class MainWindow(UI):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    def on_button_convert_clicked(self):
        if self.files:
            for file in self.files:
                img = PythonMagick.Image(file)
                img.sample('32x32')
                img.write(file[:-3] + 'ico')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    win.show()
    sys.exit(app.exec_())
