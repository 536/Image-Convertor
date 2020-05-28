# -*- coding: utf-8 -*- 
# !/usr/bin/env python3

# Name: ui.py
# Author: https://github.com/536
# Create Time: 2020-05-28 22:43
import sys

from PyQt5 import QtCore, Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import *

from conf.settings import APP_NAME, tab_qss, central_qss
from sources import sources


class UI(QMainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)

        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(':/app.png'))
        self.setFixedSize(400, 200)

        self.files = None

        self.__init_menu()
        self.__init_central()
        self.__init_statusBar()
        QtCore.QMetaObject.connectSlotsByName(self)

    def __init_menu(self):
        pass

    def __init_central(self):
        self.button_select = QPushButton('Select images..', self)
        self.button_select.setObjectName('button_select')
        self.button_select.setStyleSheet("""
            QPushButton {
                width: 100px;
                height: 100px;
                font-family: "Microsoft YaHei";
                font-size: 16px;
                background: transparent;
                color: #FFFFFF;
                border: 1px solid #618BE5;
            }
            QPushButton:hover {
                background: #618BE5;
            }
        """)
        self.button_convert = QPushButton('Convert', self)
        self.button_convert.setObjectName('button_convert')
        self.button_convert.setDisabled(True)
        self.button_convert.setStyleSheet("""
            QPushButton {
                width: 100px;
                height: 100px;
                font-family: "Microsoft YaHei";
                font-size: 16px;
                background: transparent;
                color: #FFFFFF;
                border: 1px solid #E2514B;
            }
            QPushButton:hover {
                background: #E2514B;
            }
            QPushButton::disabled {
                color: #A5A5A5;
            }
        """)

        layout = QHBoxLayout()
        layout.addWidget(self.button_select)
        layout.addWidget(self.button_convert)
        self.tab_png2ico = QWidget(self)
        self.tab_png2ico.setLayout(layout)

        layout = QHBoxLayout()
        layout.addWidget(self.button_select)
        layout.addWidget(self.button_convert)
        self.tab_png2ico = QWidget(self)
        self.tab_png2ico.setLayout(layout)

        _ = QHBoxLayout()
        _.addWidget(QLabel('Developing', self))
        self.tab_svg2png = QWidget(self)
        self.tab_svg2png.setLayout(_)

        _ = QHBoxLayout()
        _.addWidget(QLabel('Developing', self))
        self.tab_svg2ico = QWidget(self)
        self.tab_svg2ico.setLayout(_)

        central = QTabWidget()
        central.setStyleSheet(tab_qss)
        central.addTab(self.tab_png2ico, 'png2ico')
        central.addTab(self.tab_svg2png, 'svg2png')
        central.addTab(self.tab_svg2ico, 'svg2ico')
        self.setStyleSheet(central_qss)
        self.setCentralWidget(central)

    def __init_statusBar(self):
        pass

    @pyqtSlot()
    def on_button_select_clicked(self):
        self.files, _ = QFileDialog.getOpenFileNames(self, 'Select images..', '', '*.png')
        for file in self.files:
            print(file)
        self.button_convert.setEnabled(bool(self.files))

    @pyqtSlot()
    def on_button_convert_clicked(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # palette = QPalette()
    # palette.setColor(QPalette.Window, QColor(53, 53, 53))
    # palette.setColor(QPalette.WindowText, QtCore.Qt.white)
    # palette.setColor(QPalette.Base, QColor(25, 25, 25))
    # palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    # palette.setColor(QPalette.ToolTipBase, QtCore.Qt.white)
    # palette.setColor(QPalette.ToolTipText, QtCore.Qt.white)
    # palette.setColor(QPalette.Text, QtCore.Qt.white)
    # palette.setColor(QPalette.Button, QColor(53, 53, 53))
    # palette.setColor(QPalette.ButtonText, QtCore.Qt.white)
    # palette.setColor(QPalette.BrightText, QtCore.Qt.red)
    # palette.setColor(QPalette.Link, QColor(42, 130, 218))
    # palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    # palette.setColor(QPalette.HighlightedText, QtCore.Qt.black)
    # app.setPalette(palette)

    ui = UI()
    ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    ui.show()
    sys.exit(app.exec_())
