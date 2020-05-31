# -*- coding: utf-8 -*- 
# !/usr/bin/env python3

# Name: main.py
# Author: https://github.com/536
# Create Time: 2020-05-24 20:43
import sys
from math import ceil

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog

from interface.ui import UI

from libs.convertor import convertor_dict


class CommonHelper(object):
    @staticmethod
    def read(qss):
        try:
            with open(qss, mode='r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(e)
            return ''


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
            self.key(file, '32x32')
        self.signal_statusbar.emit(len(self.files))


class MainWindow(UI):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.thread_convert = None

    def button_select_clicked(self):
        current_text = self.central.tabText(self.central.currentIndex())
        if current_text == 'png2ico':
            self.files, _ = QFileDialog.getOpenFileNames(self, 'Select images..', '', '*.png')
        elif current_text == 'svg2ico':
            self.files, _ = QFileDialog.getOpenFileNames(self, 'Select images..', '', '*.svg')
        elif current_text == 'svg2png':
            self.files, _ = QFileDialog.getOpenFileNames(self, 'Select images..', '', '*.svg')

        self.statusBar.showMessage(f'{len(self.files)} file(s) selected.', msecs=5000)

        if current_text == 'png2ico':
            self.png2ico_button_convert.setEnabled(bool(self.files))
        elif current_text == 'svg2ico':
            self.svg2ico_button_convert.setEnabled(bool(self.files))
        elif current_text == 'svg2png':
            self.svg2png_button_convert.setEnabled(bool(self.files))

    def button_convert_clicked(self):
        if self.files:
            current_text = self.central.tabText(self.central.currentIndex())
            convertor = convertor_dict[current_text]
            self.thread_convert = ThreadConvert(self.files, convertor)
            self.progress.setVisible(True)
            self.thread_convert.signal_progress.connect(self.update_progress)
            self.thread_convert.signal_statusbar.connect(self.update_statusbar)
            self.thread_convert.start()
            self.files = None

            if current_text == 'png2ico':
                self.png2ico_button_convert.setDisabled(True)
            elif current_text == 'svg2ico':
                self.svg2ico_button_convert.setDisabled(True)
            elif current_text == 'svg2png':
                self.svg2png_button_convert.setDisabled(True)


if __name__ == '__main__':
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    app = QApplication(sys.argv)

    win = MainWindow()
    style_sheet = CommonHelper.read('./sources/style.qss')
    win.setStyleSheet(style_sheet)
    win.show()
    sys.exit(app.exec_())
