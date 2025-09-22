# 手动部署到Vercel指南

由于npm权限问题，我们提供手动部署的步骤。

## 方法1: 通过Vercel网站部署（推荐）

### 步骤1: 准备项目
✅ 所有必要文件已准备就绪：
- `vercel.json` - Vercel配置文件
- `api/index.py` - API处理函数
- `web_app.py` - Flask应用
- `requirements.txt` - 依赖包
- `cosmetics_diy.db` - 数据库文件
- `templates/` - 模板文件
- `.vercelignore` - 排除文件

### 步骤2: 上传到Git仓库
1. 将项目推送到GitHub/GitLab/Bitbucket
2. 确保所有文件都已提交

### 步骤3: 在Vercel网站部署
1. 访问 [vercel.com](https://vercel.com)
2. 点击 "New Project"
3. 选择您的Git仓库
4. 选择项目根目录
5. 点击 "Deploy"

## 方法2: 使用Vercel CLI（需要解决npm权限问题）

### 解决npm权限问题
```bash
# 方法1: 清理npm缓存
npm cache clean --force

# 方法2: 更改npm全局安装目录
npm config set prefix "C:\\npm-global"
npm config set cache "C:\\npm-cache"

# 方法3: 使用yarn代替npm
npm install -g yarn
yarn global add vercel
```

### 部署命令
```bash
# 登录Vercel
vercel login

# 部署到预览环境
vercel

# 部署到生产环境
vercel --prod
```

## 方法3: 使用Docker部署

如果Vercel部署仍有问题，可以考虑使用Docker：

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "web_app.py"]
```

## 部署后检查

### 1. 检查部署状态
- 访问Vercel控制台
- 查看部署日志
- 检查函数执行状态

### 2. 测试应用功能
- 访问首页
- 测试搜索功能
- 检查产品详情页面

### 3. 监控性能
- 查看函数执行时间
- 监控内存使用
- 检查错误日志

## 常见问题解决

### 问题1: 函数超时
**解决方案**: 优化数据库查询，减少响应时间

### 问题2: 数据库连接失败
**解决方案**: 确保数据库文件路径正确

### 问题3: 模板文件未找到
**解决方案**: 检查templates目录结构

### 问题4: 依赖包安装失败
**解决方案**: 检查requirements.txt格式

## 环境变量设置

在Vercel控制台设置：
- `FLASK_DEBUG`: `False`
- `PYTHONPATH`: `.`

## 监控和维护

1. **定期检查部署状态**
2. **监控函数执行时间**
3. **查看错误日志**
4. **更新依赖包版本**

## 联系支持

如果问题仍然存在：
1. 查看Vercel控制台详细错误
2. 检查函数日志
3. 联系Vercel技术支持
4. 考虑使用其他部署平台（如Railway、Render等）
