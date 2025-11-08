#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
虫害情况自动提取工具 - BeeWare 版本 (Android 16 兼容)
使用 Toga UI 框架，支持 Android 16
"""

import toga
from toga.style import Pack
from toga.constants import Row, Column
from datetime import datetime

# 尝试导入可选的库
try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

try:
    from openpyxl import Workbook, load_workbook
    HAS_OPENPYXL = True
except ImportError:
    HAS_OPENPYXL = False

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False


class PestReportApp(toga.App):
    """虫害报告提取器应用 - BeeWare 版本"""

    def startup(self):
        """构建应用UI"""
        # 主容器
        main_box = toga.Box(style=Pack(direction=Column, padding=10))

        # 标题
        title_label = toga.Label(
            '虫害报告提取器 v3.0',
            style=Pack(padding=10, font_size=20, font_weight='bold')
        )
        main_box.add(title_label)

        # 状态显示
        status_text = '应用已成功启动！\n环境: Android BeeWare'
        status_label = toga.Label(
            status_text,
            style=Pack(padding=10, font_size=12)
        )
        main_box.add(status_label)

        # 库支持信息标题
        libs_title = toga.Label(
            '依赖库状态',
            style=Pack(padding=(10, 10, 5, 10), font_weight='bold')
        )
        main_box.add(libs_title)

        # 库信息容器
        libs_container = toga.Box(style=Pack(direction=Column, padding=5))

        libs_info = [
            ('Toga (UI框架)', '✓ 已加载'),
            ('PDFPlumber', '✓' if HAS_PDFPLUMBER else '✗'),
            ('OpenPyXL', '✓' if HAS_OPENPYXL else '✗'),
            ('Pandas', '✓' if HAS_PANDAS else '✗'),
        ]

        for lib_name, lib_status in libs_info:
            lib_box = toga.Box(style=Pack(direction=Row, padding=5))
            lib_name_label = toga.Label(
                f'{lib_name}: ',
                style=Pack(padding=5, width=150)
            )
            lib_status_label = toga.Label(
                lib_status,
                style=Pack(padding=5)
            )
            lib_box.add(lib_name_label)
            lib_box.add(lib_status_label)
            libs_container.add(lib_box)

        main_box.add(libs_container)

        # 按钮容器
        button_container = toga.Box(style=Pack(direction=Column, padding=10, flex=1))

        # 测试按钮
        test_button = toga.Button(
            '测试应用',
            on_press=self.on_test_pressed,
            style=Pack(padding=10, width=200)
        )
        button_container.add(test_button)

        # 信息按钮
        info_button = toga.Button(
            '应用信息',
            on_press=self.on_info_pressed,
            style=Pack(padding=10, width=200)
        )
        button_container.add(info_button)

        # 退出按钮
        exit_button = toga.Button(
            '退出应用',
            on_press=self.on_exit_pressed,
            style=Pack(padding=10, width=200)
        )
        button_container.add(exit_button)

        main_box.add(button_container)

        # 时间戳
        timestamp_label = toga.Label(
            f'启动时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
            style=Pack(padding=10, font_size=10)
        )
        main_box.add(timestamp_label)

        # 创建主窗口
        self.main_window = toga.MainWindow(self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def on_test_pressed(self, widget):
        """测试按钮按下事件"""
        self.main_window.info_dialog(
            '测试结果',
            '✓ 应用响应正常！'
        )

    def on_info_pressed(self, widget):
        """信息按钮按下事件"""
        info_text = f"虫害报告提取器\n版本: 3.0\n日期: {datetime.now().strftime('%Y-%m-%d')}"
        self.main_window.info_dialog(
            '应用信息',
            info_text
        )

    def on_exit_pressed(self, widget):
        """退出按钮按下事件"""
        self.exit()


def main():
    return PestReportApp('虫害报告提取器', 'com.pestcontrol.pestreportextractor')


if __name__ == '__main__':
    app = main()
    app.main_loop()
