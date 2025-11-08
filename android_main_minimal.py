#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
虫害情况自动提取工具 - Android 最小化版本 v4.0
不依赖任何 UI 框架，仅使用 Python 原生库
直接输出到系统日志和文件
"""

import os
import sys
from datetime import datetime
from pathlib import Path


def main():
    """主程序入口"""

    # 获取应用存储路径
    app_dir = Path.home() / "pestreportextractor"
    app_dir.mkdir(exist_ok=True)

    # 日志文件路径
    log_file = app_dir / "app.log"

    # 启动信息
    startup_info = f"""
=====================================
虫害报告提取器 v4.0 - 最小化版本
启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
=====================================

系统信息:
- Python 版本: {sys.version}
- 平台: {sys.platform}
- 应用存储: {app_dir}

库支持状态:
"""

    # 检查可选库
    libraries = {
        'pdfplumber': False,
        'openpyxl': False,
        'pandas': False,
    }

    for lib_name in libraries:
        try:
            __import__(lib_name)
            libraries[lib_name] = True
            startup_info += f"- {lib_name}: ✓ 已加载\n"
        except ImportError:
            startup_info += f"- {lib_name}: ✗ 未安装\n"

    startup_info += f"""
=====================================
应用已成功启动！
此版本不使用 UI 框架，所有输出将写入日志文件。
日志位置: {log_file}
=====================================

"""

    # 打印到控制台
    print(startup_info)

    # 写入日志文件
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(startup_info)

    # 保持进程运行（Android 需要）
    try:
        print("应用正在运行... （按 Ctrl+C 退出）")
        while True:
            import time
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n应用已关闭")
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"应用关闭时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


if __name__ == '__main__':
    main()
