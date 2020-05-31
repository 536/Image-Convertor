# -*- coding: utf-8 -*- 
# !/usr/bin/env python3

# Name: ui.py
# Author: https://github.com/536
# Create Time: 2020-05-28 22:43
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from conf.settings import APP_NAME
from sources import sources


class UI(QMainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent, flags=QtCore.Qt.WindowStaysOnTopHint)

        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(':/app.png'))
        self.setFixedSize(360, 210)

        self.files = None

        self.__init_menu()
        self.__init_central()
        self.__init_statusBar()
        QtCore.QMetaObject.connectSlotsByName(self)

    def __init_menu(self):
        pass

    def __init_central(self):
        self.png2ico_button_select = QPushButton('Select images..', self)
        self.png2ico_button_select.clicked.connect(self.button_select_clicked)
        self.png2ico_button_select.setObjectName('button_select')
        self.png2ico_button_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.png2ico_button_convert = QPushButton('Convert', self)
        self.png2ico_button_convert.clicked.connect(self.button_convert_clicked)
        self.png2ico_button_convert.setObjectName('button_convert')
        self.png2ico_button_convert.setDisabled(True)

        self.svg2ico_button_select = QPushButton('Select images..', self)
        self.svg2ico_button_select.clicked.connect(self.button_select_clicked)
        self.svg2ico_button_select.setObjectName('button_select')
        self.svg2ico_button_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.svg2ico_button_convert = QPushButton('Convert', self)
        self.svg2ico_button_convert.clicked.connect(self.button_convert_clicked)
        self.svg2ico_button_convert.setObjectName('button_convert')
        self.svg2ico_button_convert.setDisabled(True)

        self.svg2png_button_select = QPushButton('Select images..', self)
        self.svg2png_button_select.clicked.connect(self.button_select_clicked)
        self.svg2png_button_select.setObjectName('button_select')
        self.svg2png_button_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.svg2png_button_convert = QPushButton('Convert', self)
        self.svg2png_button_convert.clicked.connect(self.button_convert_clicked)
        self.svg2png_button_convert.setObjectName('button_convert')
        self.svg2png_button_convert.setDisabled(True)

        png2ico_layout = QHBoxLayout()
        png2ico_layout.addWidget(self.png2ico_button_select)
        png2ico_layout.addWidget(self.png2ico_button_convert)
        self.tab_png2ico = QWidget(self)
        self.tab_png2ico.setLayout(png2ico_layout)

        svg2ico_layout = QHBoxLayout()
        svg2ico_layout.addWidget(self.svg2ico_button_select)
        svg2ico_layout.addWidget(self.svg2ico_button_convert)
        self.tab_svg2ico = QWidget(self)
        self.tab_svg2ico.setLayout(svg2ico_layout)

        svg2png_layout = QHBoxLayout()
        svg2png_layout.addWidget(self.svg2png_button_select)
        svg2png_layout.addWidget(self.svg2png_button_convert)
        self.tab_svg2png = QWidget(self)
        self.tab_svg2png.setLayout(svg2png_layout)

        self.central = QTabWidget(self)
        self.central.addTab(self.tab_png2ico, 'png2ico')
        self.central.addTab(self.tab_svg2ico, 'svg2ico')
        self.central.addTab(self.tab_svg2png, 'svg2png')

        self.setCentralWidget(self.central)

    def __init_statusBar(self):
        self.statusBar = QStatusBar()
        self.statusBar.setStyleSheet('')
        self.setStatusBar(self.statusBar)
        self.progress = QProgressBar(self)
        self.progress.setVisible(False)
        self.progress.setTextVisible(False)
        self.statusBar.addPermanentWidget(self.progress)

    def button_select_clicked(self):
        pass

    def button_convert_clicked(self):
        pass

    def disable_button_convert(self):
        self.png2ico_button_convert.setDisabled(True)

    def update_progress(self, msg):
        if msg == 100:
            self.progress.setVisible(False)
        else:
            self.progress.setValue(msg)

    def update_statusbar(self, msg):
        self.statusBar.showMessage(f'{msg} file(s) converted.', msecs=5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
