#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速部署脚本 - 支持多种部署方式
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

class DeploymentManager:
    def __init__(self):
        self.app_dir = Path(__file__).parent
        self.configs = {
            'heroku': {
                'requirements': 'requirements-prod.txt',
                'port': os.environ.get('PORT', 8000),
                'host': '0.0.0.0'
            },
            'railway': {
                'requirements': 'requirements-prod.txt',
                'port': os.environ.get('PORT', 8000),
                'host': '0.0.0.0'
            },
            'render': {
                'requirements': 'requirements-prod.txt',
                'port': os.environ.get('PORT', 8000),
                'host': '0.0.0.0'
            },
            'local': {
                'requirements': 'requirements.txt',
                'port': 5000,
                'host': '127.0.0.1'
            }
        }
    
    def check_requirements(self, platform):
        """检查部署要求"""
        print(f"🔍 检查 {platform} 部署要求...")
        
        if platform == 'heroku':
            try:
                subprocess.run(['heroku', '--version'], check=True, capture_output=True)
                print("✅ Heroku CLI 已安装")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("❌ 请先安装 Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli")
                return False
        
        elif platform == 'railway':
            try:
                subprocess.run(['railway', '--version'], check=True, capture_output=True)
                print("✅ Railway CLI 已安装")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("❌ 请先安装 Railway CLI: https://docs.railway.app/develop/cli")
                return False
        
        return True
    
    def create_procfile(self, platform):
        """创建Procfile"""
        config = self.configs[platform]
        procfile_content = f"web: gunicorn --bind {config['host']}:{config['port']} --workers 4 wsgi:app"
        
        with open('Procfile', 'w') as f:
            f.write(procfile_content)
        
        print(f"✅ 已创建 Procfile for {platform}")
    
    def create_runtime_txt(self):
        """创建runtime.txt"""
        with open('runtime.txt', 'w') as f:
            f.write('python-3.9.16')
        print("✅ 已创建 runtime.txt")
    
    def deploy_heroku(self, app_name=None):
        """部署到Heroku"""
        print("🚀 开始部署到 Heroku...")
        
        if not self.check_requirements('heroku'):
            return False
        
        try:
            # 创建Procfile
            self.create_procfile('heroku')
            self.create_runtime_txt()
            
            # 初始化Git仓库
            if not Path('.git').exists():
                subprocess.run(['git', 'init'], check=True)
                subprocess.run(['git', 'add', '.'], check=True)
                subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)
            
            # 创建Heroku应用
            if app_name:
                subprocess.run(['heroku', 'create', app_name], check=True)
            else:
                subprocess.run(['heroku', 'create'], check=True)
            
            # 设置环境变量
            subprocess.run(['heroku', 'config:set', 'FLASK_DEBUG=False'], check=True)
            
            # 部署
            subprocess.run(['git', 'push', 'heroku', 'main'], check=True)
            
            # 打开应用
            subprocess.run(['heroku', 'open'], check=True)
            
            print("🎉 Heroku 部署完成!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Heroku 部署失败: {e}")
            return False
    
    def deploy_railway(self):
        """部署到Railway"""
        print("🚀 开始部署到 Railway...")
        
        if not self.check_requirements('railway'):
            return False
        
        try:
            # 创建配置文件
            self.create_procfile('railway')
            
            # 登录Railway
            subprocess.run(['railway', 'login'], check=True)
            
            # 初始化项目
            subprocess.run(['railway', 'init'], check=True)
            
            # 部署
            subprocess.run(['railway', 'up'], check=True)
            
            print("🎉 Railway 部署完成!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Railway 部署失败: {e}")
            return False
    
    def deploy_render(self):
        """部署到Render"""
        print("🚀 开始部署到 Render...")
        
        try:
            # 创建配置文件
            self.create_procfile('render')
            self.create_runtime_txt()
            
            print("✅ 配置文件已创建")
            print("📋 请按照以下步骤在Render上部署:")
            print("1. 访问 https://render.com")
            print("2. 连接您的GitHub仓库")
            print("3. 选择 'Web Service'")
            print("4. 使用以下配置:")
            print("   - Build Command: pip install -r requirements-prod.txt")
            print("   - Start Command: gunicorn --bind 0.0.0.0:$PORT wsgi:app")
            print("   - Python Version: 3.9")
            
            return True
            
        except Exception as e:
            print(f"❌ Render 配置失败: {e}")
            return False
    
    def deploy_local(self):
        """本地部署"""
        print("🚀 开始本地部署...")
        
        try:
            # 安装依赖
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
            
            # 启动应用
            print("🌐 启动本地服务器...")
            print("访问地址: http://127.0.0.1:5000")
            print("按 Ctrl+C 停止服务器")
            
            os.environ['FLASK_DEBUG'] = 'True'
            subprocess.run([sys.executable, 'web_app.py'], check=True)
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ 本地部署失败: {e}")
            return False
        except KeyboardInterrupt:
            print("\n👋 服务器已停止")
            return True

def main():
    parser = argparse.ArgumentParser(description='化妆品DIY网页快速部署工具')
    parser.add_argument('platform', choices=['heroku', 'railway', 'render', 'local'],
                       help='部署平台')
    parser.add_argument('--app-name', help='应用名称 (仅Heroku需要)')
    
    args = parser.parse_args()
    
    deployer = DeploymentManager()
    
    print("🎨 化妆品DIY网页部署工具")
    print("=" * 50)
    
    if args.platform == 'heroku':
        deployer.deploy_heroku(args.app_name)
    elif args.platform == 'railway':
        deployer.deploy_railway()
    elif args.platform == 'render':
        deployer.deploy_render()
    elif args.platform == 'local':
        deployer.deploy_local()

if __name__ == '__main__':
    main()

