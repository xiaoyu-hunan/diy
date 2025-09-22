#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vercel API处理函数
用于在Vercel平台上部署Flask应用
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_app import app

# Vercel需要这个变量
handler = app
