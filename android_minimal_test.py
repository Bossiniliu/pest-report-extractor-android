#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
虫害报告工具 - 超极简测试版 v0.1
用于诊断 Android 15 闪退问题
最小化依赖，只有基础 Kivy UI
"""

from kivy.app import App
from kivy.uix.label import Label

class MinimalTestApp(App):
    """超极简应用 - 只显示一个标签"""

    def build(self):
        return Label(text='✅ Hello Android 15!\n\nKivy 基础测试成功')

if __name__ == '__main__':
    print("=" * 50)
    print("🐛 超极简 Kivy 测试应用启动")
    print("=" * 50)
    MinimalTestApp().run()
