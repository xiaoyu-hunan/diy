# Vercel错误解决方案

## 常见错误及解决方案

### 1. FUNCTION_INVOCATION_FAILED (500)
**原因**: 函数执行失败，通常是代码错误或依赖问题
**解决方案**:
- ✅ 已添加错误处理到 `api/index.py`
- ✅ 已添加数据库初始化错误处理
- ✅ 已设置最大执行时间30秒

### 2. FUNCTION_INVOCATION_TIMEOUT (504)
**原因**: 函数执行超时
**解决方案**:
- ✅ 已设置 `maxDuration: 30` 秒
- ✅ 已设置 `memory: 1024` MB

### 3. DEPLOYMENT_NOT_FOUND (404)
**原因**: 部署配置错误
**解决方案**:
- ✅ 已正确配置 `vercel.json`
- ✅ 已创建 `api/index.py` 处理函数

### 4. FUNCTION_PAYLOAD_TOO_LARGE (413)
**原因**: 请求或响应数据过大
**解决方案**:
- ✅ 已创建 `.vercelignore` 排除大文件
- ✅ 已排除PDF文件（太大）

### 5. BODY_NOT_A_STRING_FROM_FUNCTION (502)
**原因**: 函数返回格式错误
**解决方案**:
- ✅ 已确保Flask应用正确导出
- ✅ 已添加错误处理机制

## 部署步骤

### 方法1: 使用Vercel CLI（推荐）
```bash
# 1. 安装Vercel CLI
npm install -g vercel

# 2. 登录Vercel
vercel login

# 3. 部署到预览环境
vercel

# 4. 部署到生产环境
vercel --prod
```

### 方法2: 使用Vercel网站
1. 访问 [vercel.com](https://vercel.com)
2. 连接您的GitHub/GitLab/Bitbucket仓库
3. 选择项目根目录
4. 点击部署

## 调试技巧

### 查看部署日志
```bash
# 查看实时日志
vercel logs

# 查看特定部署的日志
vercel logs [deployment-url]
```

### 本地测试
```bash
# 安装Vercel CLI后，本地测试
vercel dev
```

### 检查函数状态
在Vercel控制台的Functions标签页中查看函数执行状态和错误信息。

## 环境变量设置

在Vercel控制台中设置以下环境变量：
- `FLASK_DEBUG`: `False` (生产环境)
- `PYTHONPATH`: `.` (如果需要)

## 常见问题

### Q: 数据库文件无法访问
A: 确保 `cosmetics_diy.db` 文件在项目根目录，且大小不超过50MB

### Q: 模板文件无法找到
A: 确保 `templates/` 目录存在且包含所有HTML文件

### Q: 依赖包安装失败
A: 检查 `requirements.txt` 格式，确保版本号正确

### Q: 函数超时
A: 优化代码性能，减少数据库查询，或增加超时时间

## 监控和维护

1. **定期检查部署状态**
2. **监控函数执行时间**
3. **查看错误日志**
4. **更新依赖包版本**

## 联系支持

如果问题仍然存在，请：
1. 查看Vercel控制台的详细错误信息
2. 检查函数日志
3. 联系Vercel技术支持
