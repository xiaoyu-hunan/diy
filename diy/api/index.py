#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vercel API处理函数
用于在Vercel平台上部署Flask应用
"""

import sys
import os
import traceback

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from web_app import app
    # Vercel需要这个变量
    handler = app
except Exception as e:
    print(f"Error importing web_app: {e}")
    print(traceback.format_exc())
    
    # 创建一个简单的错误处理应用
    from flask import Flask, jsonify
    error_app = Flask(__name__)
    
    @error_app.route('/')
    def error_handler():
        return jsonify({
            'error': 'Application failed to load',
            'message': str(e),
            'traceback': traceback.format_exc()
        }), 500
    
    handler = error_app
