# -*- coding: utf-8 -*- 
# !/usr/bin/env python3

# Name: settings.py
# Author: https://github.com/536
# Create Time: 2020-05-28 23:10
APP_NAME = 'Image Convertor'
VERSION = 'v1.0'

central_qss = """
QWidget {
    background: #363D48;
}
"""

tab_qss = """
/* The tab widget frame */
QTabWidget::pane {
    border-top: 2px solid #618BE5;
}

QTabBar {
}

QTabBar::tab:first {}
QTabBar::tab:last {}

QTabBar::tab {
    color: #FFFFFF;
    background: transparent;
    font-family: "MicroSoft YaHei";
    font-size: 14px;
    padding-left: -9px;
    padding-right: -9px;
    width: 120px;
    height: 40px;
}

QTabBar::tab:selected,
QTabBar::tab:hover {
    background: #618BE5;
    font-family: "MicroSoft YaHei";
    font-size: 14px;
}

/*整个最上面的tab栏*/
QTabWidget::tab-bar {
}
"""