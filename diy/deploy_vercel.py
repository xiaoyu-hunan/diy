#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vercel部署脚本
用于检查和准备Vercel部署
"""

import os
import sys
import subprocess
import json

def check_files():
    """检查必要的文件是否存在"""
    required_files = [
        'vercel.json',
        'api/index.py',
        'web_app.py',
        'requirements.txt',
        'cosmetics_diy.db',
        'templates/',
        'extract_pdf_data.py'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ 缺少以下文件:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    else:
        print("✅ 所有必要文件都存在")
        return True

def check_database():
    """检查数据库文件"""
    db_path = 'cosmetics_diy.db'
    if os.path.exists(db_path):
        size = os.path.getsize(db_path)
        print(f"✅ 数据库文件存在，大小: {size} bytes")
        return True
    else:
        print("❌ 数据库文件不存在")
        return False

def check_vercel_config():
    """检查Vercel配置"""
    try:
        with open('vercel.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        print("✅ Vercel配置文件格式正确")
        print(f"   版本: {config.get('version', 'N/A')}")
        print(f"   构建配置: {len(config.get('builds', []))} 个")
        print(f"   路由配置: {len(config.get('routes', []))} 个")
        return True
    except Exception as e:
        print(f"❌ Vercel配置文件错误: {e}")
        return False

def check_requirements():
    """检查requirements.txt"""
    try:
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            requirements = f.read().strip().split('\n')
        
        print(f"✅ 找到 {len(requirements)} 个依赖包:")
        for req in requirements:
            if req.strip():
                print(f"   - {req.strip()}")
        return True
    except Exception as e:
        print(f"❌ 无法读取requirements.txt: {e}")
        return False

def main():
    """主函数"""
    print("🔍 检查Vercel部署准备情况...")
    print("=" * 50)
    
    checks = [
        ("文件检查", check_files),
        ("数据库检查", check_database),
        ("Vercel配置检查", check_vercel_config),
        ("依赖包检查", check_requirements)
    ]
    
    all_passed = True
    for check_name, check_func in checks:
        print(f"\n📋 {check_name}:")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 所有检查都通过了！可以部署到Vercel")
        print("\n📝 部署命令:")
        print("   1. npm install -g vercel")
        print("   2. vercel login")
        print("   3. vercel")
        print("   4. vercel --prod")
    else:
        print("❌ 发现问题，请先修复后再部署")
    
    return all_passed

if __name__ == "__main__":
    main()
