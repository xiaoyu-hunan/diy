# 化妆品DIY配方库

一个基于Flask的化妆品DIY配方管理系统，提供配方查询、分类浏览、制作指导等功能。

## 功能特点

- 🔍 **智能搜索**: 支持按产品名称、成分、功效等关键词搜索
- 📂 **分类浏览**: 按护肤品、面膜、护发产品等分类查看配方
- 📋 **详细配方**: 包含原料、制作步骤、使用方法、产品功效等完整信息
- 🎨 **美观界面**: 响应式设计，支持移动端访问
- 💾 **数据管理**: 基于SQLite数据库，易于扩展和维护

## 项目结构

```
diy/
├── extract_pdf_data.py      # 数据提取和数据库初始化脚本
├── web_app.py              # Flask Web应用主程序
├── cosmetics_diy.db        # SQLite数据库文件（运行后生成）
├── requirements.txt        # Python依赖包列表
├── README.md              # 项目说明文档
└── templates/             # HTML模板文件
    ├── base.html          # 基础模板
    ├── index.html         # 首页
    ├── search.html        # 搜索页面
    ├── product_detail.html # 产品详情页
    ├── categories.html    # 分类页面
    └── category.html      # 分类产品列表页
```

## 安装和使用

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 初始化数据库

```bash
python extract_pdf_data.py
```

这将创建一个SQLite数据库并导入示例配方数据。

### 3. 启动Web应用

```bash
python web_app.py
```

应用将在 http://localhost:5000 启动。

## 数据库结构

### 主要数据表

- **products**: 产品基本信息
- **ingredients**: 原料信息
- **formulations**: 产品配方（产品-原料关系）
- **recipes**: 制作步骤
- **benefits**: 产品功效
- **usage_instructions**: 使用方法

### 数据关系

```
products (1) -----> (N) formulations
products (1) -----> (N) recipes
products (1) -----> (N) benefits
products (1) -----> (N) usage_instructions
ingredients (1) -----> (N) formulations
```

## 示例数据

项目包含以下示例配方：

1. **薰衣草保湿面霜** - 适合干性皮肤的保湿面霜
2. **茶树精油祛痘凝胶** - 抗菌消炎的祛痘产品
3. **玫瑰保湿精华液** - 富含透明质酸的保湿精华
4. **柠檬美白面膜** - 天然柠檬美白面膜
5. **薄荷清爽洗发水** - 控油去屑的天然洗发水

## 扩展功能

### 添加新配方

可以通过修改 `extract_pdf_data.py` 中的 `sample_recipes` 列表来添加新配方：

```python
sample_recipes.append({
    "name": "新产品名称",
    "category": "产品分类",
    "description": "产品描述",
    "ingredients": [...],
    "steps": [...],
    "benefits": [...],
    "usage": [...]
})
```

### 从PDF提取数据

要处理实际的PDF文件，需要：

1. 安装PDF处理库：`pip install PyPDF2` 或 `pip install pdfplumber`
2. 修改 `parse_pdf_content()` 函数来读取PDF文件
3. 解析PDF内容并提取配方信息

## 技术栈

- **后端**: Flask (Python Web框架)
- **数据库**: SQLite (轻量级关系型数据库)
- **前端**: Bootstrap 5 + HTML5 + CSS3 + JavaScript
- **模板引擎**: Jinja2

## 浏览器支持

- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+

## 开发说明

### 本地开发

1. 克隆项目到本地
2. 创建虚拟环境：`python -m venv venv`
3. 激活虚拟环境：`venv\Scripts\activate` (Windows) 或 `source venv/bin/activate` (Linux/Mac)
4. 安装依赖：`pip install -r requirements.txt`
5. 运行应用：`python web_app.py`

### 生产部署

推荐使用 Gunicorn + Nginx 部署：

```bash
# 安装Gunicorn
pip install gunicorn

# 启动应用
gunicorn -w 4 -b 0.0.0.0:8000 web_app:app
```

## 许可证

本项目采用 MIT 许可证。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 GitHub Issue
- 发送邮件至项目维护者

---

**注意**: 本项目仅用于学习和演示目的。实际使用DIY化妆品配方时，请确保原料安全性和制作过程的卫生条件。
