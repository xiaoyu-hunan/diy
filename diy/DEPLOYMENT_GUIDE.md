# 化妆品DIY网页部署指南

## 📋 概述

本指南将帮助您将化妆品DIY配方网页应用部署到服务器上，让其他人可以通过互联网访问您的网站。

## 🛠️ 部署选项

### 选项1: 使用云服务器 (推荐)

#### 1.1 选择云服务提供商
- **阿里云ECS**: 适合国内用户，访问速度快
- **腾讯云CVM**: 性价比高，服务稳定
- **AWS EC2**: 全球部署，功能强大
- **Google Cloud**: 技术先进，价格透明
- **Vultr/DigitalOcean**: 价格便宜，适合小型项目

#### 1.2 服务器配置建议
- **CPU**: 1-2核
- **内存**: 1-2GB
- **存储**: 20-40GB SSD
- **带宽**: 1-5Mbps
- **操作系统**: Ubuntu 20.04 LTS 或 CentOS 8

#### 1.3 域名配置
- 购买域名 (阿里云、腾讯云、GoDaddy等)
- 配置DNS解析，将域名指向服务器IP

### 选项2: 使用免费托管平台

#### 2.1 Heroku (推荐)
```bash
# 安装Heroku CLI
# 创建Procfile
echo "web: gunicorn --bind 0.0.0.0:$PORT wsgi:app" > Procfile

# 部署
heroku create your-app-name
git push heroku main
```

#### 2.2 Railway
- 支持从GitHub直接部署
- 免费额度充足
- 自动HTTPS

#### 2.3 Render
- 免费静态网站托管
- 支持Python应用
- 自动部署

## 🚀 详细部署步骤

### 步骤1: 准备服务器

1. **购买云服务器**
   - 选择Ubuntu 20.04 LTS
   - 配置安全组，开放22、80、443端口

2. **连接到服务器**
   ```bash
   ssh root@your-server-ip
   ```

3. **更新系统**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

### 步骤2: 安装必要软件

```bash
# 安装Python和pip
sudo apt install -y python3 python3-pip python3-venv

# 安装Nginx
sudo apt install -y nginx

# 安装Git
sudo apt install -y git

# 安装防火墙
sudo apt install -y ufw
```

### 步骤3: 上传应用文件

```bash
# 方法1: 使用Git (推荐)
cd /var/www
sudo git clone https://github.com/your-username/cosmetics-diy.git
sudo chown -R www-data:www-data cosmetics-diy

# 方法2: 使用SCP上传
scp -r ./diy root@your-server-ip:/var/www/cosmetics-diy
```

### 步骤4: 配置Python环境

```bash
cd /var/www/cosmetics-diy

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements-prod.txt
```

### 步骤5: 配置Gunicorn

```bash
# 测试Gunicorn
gunicorn --bind 0.0.0.0:8000 wsgi:app

# 使用配置文件启动
gunicorn --config gunicorn.conf.py wsgi:app
```

### 步骤6: 配置Nginx

```bash
# 复制配置文件
sudo cp nginx.conf /etc/nginx/sites-available/cosmetics-diy

# 创建软链接
sudo ln -s /etc/nginx/sites-available/cosmetics-diy /etc/nginx/sites-enabled/

# 删除默认配置
sudo rm /etc/nginx/sites-enabled/default

# 测试配置
sudo nginx -t

# 重启Nginx
sudo systemctl restart nginx
```

### 步骤7: 配置系统服务

```bash
# 复制服务文件
sudo cp cosmetics-diy.service /etc/systemd/system/

# 重新加载systemd
sudo systemctl daemon-reload

# 启用并启动服务
sudo systemctl enable cosmetics-diy
sudo systemctl start cosmetics-diy

# 检查状态
sudo systemctl status cosmetics-diy
```

### 步骤8: 配置防火墙

```bash
# 配置防火墙规则
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 80/tcp    # HTTP
sudo ufw allow 443/tcp   # HTTPS
sudo ufw --force enable
```

## 🔧 自动化部署

使用提供的部署脚本：

```bash
# 给脚本执行权限
chmod +x deploy.sh

# 运行部署脚本
sudo ./deploy.sh
```

## 📊 监控和维护

### 查看服务状态
```bash
# 查看应用状态
sudo systemctl status cosmetics-diy

# 查看应用日志
sudo journalctl -u cosmetics-diy -f

# 查看Nginx状态
sudo systemctl status nginx

# 查看Nginx日志
sudo tail -f /var/log/nginx/cosmetics_diy_access.log
```

### 重启服务
```bash
# 重启应用
sudo systemctl restart cosmetics-diy

# 重启Nginx
sudo systemctl restart nginx
```

### 更新应用
```bash
cd /var/www/cosmetics-diy
git pull
source venv/bin/activate
pip install -r requirements-prod.txt
sudo systemctl restart cosmetics-diy
```

## 🔒 安全配置

### SSL证书配置 (Let's Encrypt)
```bash
# 安装Certbot
sudo apt install -y certbot python3-certbot-nginx

# 获取SSL证书
sudo certbot --nginx -d your-domain.com

# 自动续期
sudo crontab -e
# 添加: 0 12 * * * /usr/bin/certbot renew --quiet
```

### 安全加固
```bash
# 配置SSH密钥登录
ssh-keygen -t rsa -b 4096
ssh-copy-id user@server-ip

# 禁用密码登录
sudo nano /etc/ssh/sshd_config
# 设置: PasswordAuthentication no
sudo systemctl restart ssh

# 配置fail2ban
sudo apt install -y fail2ban
sudo systemctl enable fail2ban
```

## 🌐 域名和DNS配置

### 1. 购买域名
- 在域名注册商购买域名
- 推荐: 阿里云、腾讯云、GoDaddy

### 2. 配置DNS解析
```
类型: A
主机记录: @
记录值: 你的服务器IP
TTL: 600

类型: A
主机记录: www
记录值: 你的服务器IP
TTL: 600
```

### 3. 等待DNS生效
- 通常需要5-30分钟
- 可以使用 `nslookup your-domain.com` 检查

## 📱 移动端优化

### 响应式设计
- 应用已包含响应式CSS
- 支持手机、平板访问
- 触摸友好的界面

### PWA配置 (可选)
```html
<!-- 添加到base.html -->
<link rel="manifest" href="/static/manifest.json">
<meta name="theme-color" content="#6366f1">
```

## 🚨 故障排除

### 常见问题

1. **服务无法启动**
   ```bash
   sudo journalctl -u cosmetics-diy -n 50
   ```

2. **Nginx配置错误**
   ```bash
   sudo nginx -t
   ```

3. **端口被占用**
   ```bash
   sudo netstat -tulpn | grep :8000
   ```

4. **权限问题**
   ```bash
   sudo chown -R www-data:www-data /var/www/cosmetics-diy
   ```

### 性能优化

1. **启用Gzip压缩**
   ```nginx
   gzip on;
   gzip_types text/plain text/css application/json application/javascript;
   ```

2. **配置缓存**
   ```nginx
   location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
       expires 1y;
       add_header Cache-Control "public, immutable";
   }
   ```

## 📞 技术支持

如果遇到问题，可以：

1. 查看日志文件
2. 检查服务状态
3. 验证配置文件
4. 搜索相关错误信息

## 🎉 部署完成

部署完成后，您可以通过以下方式访问网站：

- **HTTP**: http://your-domain.com
- **HTTPS**: https://your-domain.com (配置SSL后)
- **IP访问**: http://your-server-ip

恭喜！您的化妆品DIY配方网站已经成功上线！🎊

