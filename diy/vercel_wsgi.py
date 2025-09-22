#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vercel WSGI配置文件
专门用于Vercel平台部署
"""

import os
import sys

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from web_app import app

# Vercel需要这个变量
application = app

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
