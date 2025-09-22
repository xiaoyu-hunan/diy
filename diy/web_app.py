#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
化妆品DIY网页应用
使用Flask框架提供Web界面
"""

# 没啥，就是导入依赖包而已~
from flask import Flask, render_template, request, jsonify, redirect, url_for  # pyright: ignore[reportUnusedImport, reportMissingImports]
import sqlite3
import json
from extract_pdf_data import CosmeticsDatabase

app = Flask(__name__)

# 初始化数据库
db = CosmeticsDatabase()

@app.route('/')
def index():
    """首页 - 显示所有产品列表"""
    products = db.search_products()
    return render_template('index.html', products=products)

@app.route('/search')
def search():
    """搜索页面"""
    keyword = request.args.get('q', '')
    products = db.search_products(keyword)
    return render_template('search.html', products=products, keyword=keyword)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """产品详情页面"""
    product = db.get_product_details(product_id)
    if not product:
        return "产品未找到", 404
    return render_template('product_detail.html', product=product)

@app.route('/api/search')
def api_search():
    """API接口 - 搜索产品"""
    keyword = request.args.get('q', '')
    products = db.search_products(keyword)
    return jsonify(products)

@app.route('/api/product/<int:product_id>')
def api_product_detail(product_id):
    """API接口 - 获取产品详情"""
    product = db.get_product_details(product_id)
    if not product:
        return jsonify({'error': '产品未找到'}), 404
    return jsonify(product)

@app.route('/categories')
def categories():
    """分类页面"""
    conn = sqlite3.connect(db.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT category FROM products ORDER BY category")
    categories = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    # 获取每个分类的产品数量
    category_data = []
    for category in categories:
        products = db.search_products()
        count = len([p for p in products if p['category'] == category])
        category_data.append({'name': category, 'count': count})
    
    return render_template('categories.html', categories=category_data)

@app.route('/category/<category>')
def category_products(category):
    """分类产品列表"""
    products = db.search_products()
    category_products = [p for p in products if p['category'] == category]
    return render_template('category.html', products=category_products, category=category)

if __name__ == '__main__':
    # 开发环境配置
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
