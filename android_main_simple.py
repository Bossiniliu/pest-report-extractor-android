#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
虫害报告提取工具 - 简化测试版 v2.1
用于诊断闪退问题
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from pathlib import Path
import sys
import traceback

# Android 存储路径
try:
    from android.permissions import request_permissions, Permission
    from android.storage import primary_external_storage_path
    ANDROID = True
    try:
        STORAGE_PATH = primary_external_storage_path()
    except:
        STORAGE_PATH = "/sdcard"
except:
    ANDROID = False
    STORAGE_PATH = str(Path.home())


class SimpleTestApp(App):
    """简化测试应用"""
    
    def build(self):
        """构建应用界面"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 标题
        title = Label(
            text='🐛 虫害报告工具\n简化测试版 v2.1',
            size_hint=(1, 0.3),
            font_size='24sp'
        )
        layout.add_widget(title)
        
        # 系统信息
        info_text = f"""
系统信息:
- Android: {ANDROID}
- 存储路径: {STORAGE_PATH}
- Python: {sys.version.split()[0]}
        """
        
        info_label = Label(
            text=info_text,
            size_hint=(1, 0.3),
            font_size='14sp'
        )
        layout.add_widget(info_label)
        
        # 状态标签
        self.status_label = Label(
            text='应用启动成功!\n等待权限请求...',
            size_hint=(1, 0.2),
            font_size='16sp'
        )
        layout.add_widget(self.status_label)
        
        # 测试按钮
        test_btn = Button(
            text='📱 测试权限',
            size_hint=(1, 0.2),
            font_size='18sp'
        )
        test_btn.bind(on_press=self.test_permissions)
        layout.add_widget(test_btn)
        
        # 延迟请求权限
        if ANDROID:
            Clock.schedule_once(self.request_permissions, 1.0)
        
        return layout
    
    def request_permissions(self, dt):
        """请求Android权限"""
        try:
            self.status_label.text = '正在请求权限...'
            
            permissions = [
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE
            ]
            
            request_permissions(permissions)
            self.status_label.text = '✅ 权限请求已发送\n请在系统弹窗中授权'
            
        except Exception as e:
            self.status_label.text = f'⚠️ 权限请求失败:\n{str(e)}'
    
    def test_permissions(self, instance):
        """测试权限和文件写入"""
        try:
            self.status_label.text = '测试中...'
            
            # 测试目录创建
            test_dir = Path(STORAGE_PATH) / "PestReportTest"
            test_dir.mkdir(parents=True, exist_ok=True)
            
            # 测试文件写入
            test_file = test_dir / "test.txt"
            test_file.write_text(f"测试时间: {sys.version}\n平台: {ANDROID}")
            
            self.status_label.text = f'✅ 测试成功!\n文件位置:\n{test_file}'
            
        except Exception as e:
            error_msg = f'❌ 测试失败:\n{str(e)}'
            self.status_label.text = error_msg
            print(traceback.format_exc())


if __name__ == '__main__':
    try:
        print("=" * 50)
        print("🐛 简化测试应用启动")
        print(f"Android: {ANDROID}")
        print(f"Storage: {STORAGE_PATH}")
        print("=" * 50)
        
        SimpleTestApp().run()
        
    except Exception as e:
        error_msg = f"\n启动失败:\n{str(e)}\n\n{traceback.format_exc()}"
        print(error_msg)
        
        # 写入错误日志
        try:
            error_file = Path(STORAGE_PATH) / "crash_log.txt"
            with open(error_file, 'w') as f:
                f.write(error_msg)
            print(f"错误日志: {error_file}")
        except:
            pass
        
        raise
