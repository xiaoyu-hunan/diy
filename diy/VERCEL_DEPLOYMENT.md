# Vercel部署指南

## 部署步骤

1. **安装Vercel CLI**（如果还没有安装）：
   ```bash
   npm i -g vercel
   ```

2. **登录Vercel**：
   ```bash
   vercel login
   ```

3. **在项目根目录部署**：
   ```bash
   vercel
   ```

4. **生产环境部署**：
   ```bash
   vercel --prod
   ```

## 重要文件说明

- `vercel.json`: Vercel配置文件，定义了构建和路由规则
- `api/index.py`: Vercel API处理函数
- `vercel_wsgi.py`: Vercel专用的WSGI配置
- `.vercelignore`: 排除不必要的文件，减少部署包大小

## 注意事项

1. **数据库文件**: 确保`cosmetics_diy.db`文件存在于项目根目录
2. **Python版本**: Vercel默认使用Python 3.9
3. **依赖包**: 所有依赖都在`requirements.txt`中定义
4. **静态文件**: 模板文件在`templates/`目录中

## 常见问题解决

### 如果遇到FUNCTION_INVOCATION_FAILED错误：
- 检查数据库文件是否存在
- 确保所有依赖包都正确安装
- 检查Python路径配置

### 如果遇到DEPLOYMENT_NOT_FOUND错误：
- 确保在正确的项目目录中运行`vercel`命令
- 检查`vercel.json`文件格式是否正确

### 如果遇到FUNCTION_PAYLOAD_TOO_LARGE错误：
- 检查`.vercelignore`文件是否正确排除了大文件
- 确保PDF文件被排除在部署之外

## 环境变量

如果需要设置环境变量，可以在Vercel控制台中设置：
- `FLASK_DEBUG`: 设置为`False`用于生产环境
- `PORT`: Vercel会自动设置

## 监控和调试

- 在Vercel控制台中查看部署日志
- 使用`vercel logs`命令查看实时日志
- 检查函数执行时间和内存使用情况
