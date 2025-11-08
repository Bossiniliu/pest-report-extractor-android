#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
虫害情况自动提取工具 - Android版本 v2.2 (最小化测试版本)
只使用 Kivy，不依赖复杂的数据处理库
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
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

# Android 支持
ANDROID = False
try:
    from jnius import autoclass, cast
    ANDROID = True
except ImportError:
    pass

# 设置窗口大小
Window.size = (400, 600)


class PestReportApp(App):
    """虫害报告提取器应用"""

    def build(self):
        """构建应用UI"""
        # 主容器
        main_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # 标题
        title_label = Label(
            text='虫害报告提取器 v2.2',
            size_hint_y=0.15,
            bold=True,
            font_size='20sp'
        )
        main_layout.add_widget(title_label)

        # 状态显示
        status_label = Label(
            text='[状态信息]\n应用已成功启动！\n当前环境: Android' if ANDROID else '当前环境: 桌面',
            size_hint_y=0.2,
            markup=True
        )
        main_layout.add_widget(status_label)

        # 库支持信息
        libs_layout = GridLayout(cols=2, spacing=dp(5), size_hint_y=0.25)

        libs_info = [
            ('Kivy', '✓ 已加载'),
            ('PDFPlumber', '✓' if HAS_PDFPLUMBER else '✗'),
            ('OpenPyXL', '✓' if HAS_OPENPYXL else '✗'),
            ('Pandas', '✓' if HAS_PANDAS else '✗'),
        ]

        for lib_name, lib_status in libs_info:
            libs_layout.add_widget(Label(text=lib_name, size_hint_y=1))
            libs_layout.add_widget(Label(text=lib_status, size_hint_y=1))

        main_layout.add_widget(Label(text='[依赖库状态]', size_hint_y=0.05, bold=True))
        main_layout.add_widget(libs_layout)

        # 按钮容器
        button_layout = BoxLayout(orientation='vertical', spacing=dp(10), size_hint_y=0.35)

        # 测试按钮
        test_button = Button(
            text='测试应用',
            size_hint_y=0.25,
            background_color=(0.2, 0.6, 0.2, 1)
        )
        test_button.bind(on_press=self.on_test_pressed)
        button_layout.add_widget(test_button)

        # 信息按钮
        info_button = Button(
            text='应用信息',
            size_hint_y=0.25,
            background_color=(0.2, 0.4, 0.8, 1)
        )
        info_button.bind(on_press=self.on_info_pressed)
        button_layout.add_widget(info_button)

        # 退出按钮
        exit_button = Button(
            text='退出应用',
            size_hint_y=0.25,
            background_color=(0.8, 0.2, 0.2, 1)
        )
        exit_button.bind(on_press=self.on_exit_pressed)
        button_layout.add_widget(exit_button)

        main_layout.add_widget(button_layout)

        # 时间戳
        timestamp_label = Label(
            text=f'启动时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
            size_hint_y=0.05,
            font_size='10sp'
        )
        main_layout.add_widget(timestamp_label)

        return main_layout

    def on_test_pressed(self, instance):
        """测试按钮按下事件"""
        print("✓ 应用响应正常！")

    def on_info_pressed(self, instance):
        """信息按钮按下事件"""
        info_text = f"应用信息:\n"
        info_text += f"名称: 虫害报告提取器\n"
        info_text += f"版本: 2.2\n"
        info_text += f"时间: {datetime.now().strftime('%Y-%m-%d')}"
        print(info_text)

    def on_exit_pressed(self, instance):
        """退出按钮按下事件"""
        print("退出应用...")
        App.get_running_app().stop()


if __name__ == '__main__':
    app = PestReportApp()
    app.title = '虫害报告提取器'
    app.run()
