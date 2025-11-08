package com.pestcontrol.pestreportextractor;

import android.content.Intent;
import android.os.Bundle;
import org.kivy.android.PythonActivity;

/**
 * Flask Web 应用的 Activity 包装器
 * 用于启动 Flask Web 服务器并在 WebView 中显示
 */
public class MainActivity extends PythonActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }
}
