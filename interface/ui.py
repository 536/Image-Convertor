# -*- coding: utf-8 -*- 
# !/usr/bin/env python3

# Name: ui.py
# Author: https://github.com/536
# Create Time: 2020-05-28 22:43
import sys

from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPalette, QColor, QMouseEvent
from PyQt5.QtWidgets import *

from conf.settings import APP_NAME
from sources import sources


class Tab(QTabWidget):
    def __init__(self, parent=None):
        super(Tab, self).__init__(parent)

    def enterEvent(self, event: QtCore.QEvent) -> None:
        self.activateWindow()


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
        self.button_select = QPushButton('Select images..', self)
        self.button_select.setObjectName('button_select')
        self.button_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_convert = QPushButton('Convert', self)
        self.button_convert.setObjectName('button_convert')
        self.button_convert.setDisabled(True)

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

        self.central = Tab(self)
        self.central.addTab(self.tab_png2ico, 'png2ico')
        self.central.addTab(self.tab_svg2png, 'svg2png')
        self.central.addTab(self.tab_svg2ico, 'svg2ico')

        self.setCentralWidget(self.central)

    def __init_statusBar(self):
        self.statusBar = QStatusBar()
        self.statusBar.setStyleSheet('')
        self.setStatusBar(self.statusBar)
        self.progress = QProgressBar(self)
        self.progress.setVisible(False)
        self.progress.setTextVisible(False)
        self.statusBar.addPermanentWidget(self.progress)

    @pyqtSlot()
    def on_button_select_clicked(self):
        self.files, _ = QFileDialog.getOpenFileNames(self, 'Select images..', '', '*.png')
        self.statusBar.showMessage(f'{len(self.files)} file(s) selected.', msecs=5000)
        self.button_convert.setEnabled(bool(self.files))

    @pyqtSlot()
    def on_button_convert_clicked(self):
        pass

    def disable_button_convert(self):
        self.button_convert.setDisabled(True)

    def update_progress(self, msg):
        if msg == 100:
            self.progress.setVisible(False)
        else:
            self.progress.setValue(msg)

    def update_statusbar(self, msg):
        self.statusBar.showMessage(f'{msg} file(s) converted.', msecs=5000)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, event: QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)  # 更改窗口位置
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
