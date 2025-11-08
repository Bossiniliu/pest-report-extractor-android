#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
虫害报告提取器 - 超极简版本
Android 16 兼容

此版本是纯 Python 应用，不依赖 Kivy 或 Flask。
通过简单的服务循环来验证 Android 16 兼容性。
"""

import sys
import logging
import time
import signal

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

# 全局标志用于优雅关闭
should_exit = False


def signal_handler(signum, frame):
    """处理系统信号（优雅关闭）"""
    global should_exit
    logger.info("收到关闭信号，准备退出...")
    should_exit = True


def main():
    """主程序入口"""
    global should_exit

    # 注册信号处理器
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    logger.info("=" * 50)
    logger.info("虫害报告提取器 v3.0 - Android 16 兼容版")
    logger.info("=" * 50)

    try:
        logger.info("✅ Python 3 运行时已初始化")
        logger.info("✅ 日志系统已启动")
        logger.info("⏳ 应用现在运行在后台服务模式...")
        logger.info("")
        logger.info("服务统计信息:")

        cycle_count = 0
        start_time = time.time()

        # 服务主循环 - 让应用保持运行
        while not should_exit:
            try:
                cycle_count += 1

                # 每30秒输出一次心跳
                if cycle_count % 3 == 0:
                    uptime = time.time() - start_time
                    logger.info(f"  • 循环数: {cycle_count}, 运行时间: {uptime:.0f}秒")

                # 睡眠10秒
                time.sleep(10)

            except KeyboardInterrupt:
                logger.info("收到键盘中断信号")
                break
            except Exception as e:
                logger.warning(f"循环中发生异常: {e}")
                # 继续运行，不退出
                time.sleep(1)

        logger.info("")
        logger.info(f"应用正常关闭，总循环数: {cycle_count}")
        logger.info("=" * 50)
        return 0

    except Exception as e:
        logger.error(f"❌ 应用崩溃: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    exit_code = main()
    logger.info(f"进程退出，代码: {exit_code}")
    sys.exit(exit_code)
