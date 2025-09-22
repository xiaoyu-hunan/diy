#!/bin/bash

# 化妆品DIY网页部署脚本
# 使用方法: ./deploy.sh

set -e  # 遇到错误立即退出

echo "🚀 开始部署化妆品DIY网页应用..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 配置变量 (请根据实际情况修改)
APP_DIR="/var/www/cosmetics-diy"
DOMAIN="your-domain.com"
NGINX_CONF="/etc/nginx/sites-available/cosmetics-diy"
SERVICE_NAME="cosmetics-diy"

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 检查是否为root用户
if [ "$EUID" -ne 0 ]; then
    print_error "请使用sudo运行此脚本"
    exit 1
fi

# 1. 更新系统包
print_status "更新系统包..."
apt update && apt upgrade -y

# 2. 安装必要的软件包
print_status "安装必要的软件包..."
apt install -y python3 python3-pip python3-venv nginx git

# 3. 创建应用目录
print_status "创建应用目录..."
mkdir -p $APP_DIR
cd $APP_DIR

# 4. 创建虚拟环境
print_status "创建Python虚拟环境..."
python3 -m venv venv
source venv/bin/activate

# 5. 安装Python依赖
print_status "安装Python依赖..."
pip install --upgrade pip
pip install -r requirements-prod.txt

# 6. 复制应用文件 (假设文件已在当前目录)
print_status "复制应用文件..."
cp -r . $APP_DIR/

# 7. 设置文件权限
print_status "设置文件权限..."
chown -R www-data:www-data $APP_DIR
chmod +x $APP_DIR/deploy.sh

# 8. 配置Nginx
print_status "配置Nginx..."
cp nginx.conf $NGINX_CONF

# 替换配置文件中的占位符
sed -i "s/your-domain.com/$DOMAIN/g" $NGINX_CONF
sed -i "s|/path/to/your/app|$APP_DIR|g" $NGINX_CONF

# 创建软链接
ln -sf $NGINX_CONF /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default

# 测试Nginx配置
nginx -t

# 9. 配置系统服务
print_status "配置系统服务..."
cp cosmetics-diy.service /etc/systemd/system/

# 替换服务文件中的占位符
sed -i "s|/path/to/your/app|$APP_DIR|g" /etc/systemd/system/cosmetics-diy.service
sed -i "s|/path/to/your/venv|$APP_DIR/venv|g" /etc/systemd/system/cosmetics-diy.service

# 重新加载systemd
systemctl daemon-reload

# 10. 启动服务
print_status "启动服务..."
systemctl enable $SERVICE_NAME
systemctl start $SERVICE_NAME
systemctl restart nginx

# 11. 检查服务状态
print_status "检查服务状态..."
sleep 5

if systemctl is-active --quiet $SERVICE_NAME; then
    print_success "应用服务运行正常"
else
    print_error "应用服务启动失败"
    systemctl status $SERVICE_NAME
    exit 1
fi

if systemctl is-active --quiet nginx; then
    print_success "Nginx服务运行正常"
else
    print_error "Nginx服务启动失败"
    systemctl status nginx
    exit 1
fi

# 12. 显示部署信息
print_success "🎉 部署完成！"
echo ""
echo "📋 部署信息:"
echo "   应用目录: $APP_DIR"
echo "   域名: $DOMAIN"
echo "   服务名: $SERVICE_NAME"
echo ""
echo "🔧 常用命令:"
echo "   查看应用状态: sudo systemctl status $SERVICE_NAME"
echo "   重启应用: sudo systemctl restart $SERVICE_NAME"
echo "   查看应用日志: sudo journalctl -u $SERVICE_NAME -f"
echo "   查看Nginx状态: sudo systemctl status nginx"
echo "   重启Nginx: sudo systemctl restart nginx"
echo ""
echo "🌐 访问地址:"
echo "   http://$DOMAIN"
echo "   http://$(curl -s ifconfig.me)"  # 显示公网IP
echo ""
print_warning "请记得配置防火墙和安全组，开放80和443端口"

# 13. 显示防火墙配置建议
echo ""
echo "🔥 防火墙配置建议:"
echo "   sudo ufw allow 22/tcp    # SSH"
echo "   sudo ufw allow 80/tcp    # HTTP"
echo "   sudo ufw allow 443/tcp   # HTTPS"
echo "   sudo ufw --force enable  # 启用防火墙"

