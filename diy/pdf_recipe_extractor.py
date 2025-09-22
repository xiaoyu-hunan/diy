#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF配方提取器
从PDF文件中提取真实的化妆品DIY配方
"""

import os
import re
from typing import List, Dict, Any
from extract_pdf_data import CosmeticsDatabase

def install_pdf_libraries():
    """安装PDF处理库"""
    import subprocess
    import sys
    
    libraries = ['PyPDF2', 'pdfplumber', 'pymupdf']
    
    for lib in libraries:
        try:
            __import__(lib)
            print(f"✓ {lib} 已安装")
        except ImportError:
            print(f"正在安装 {lib}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
                print(f"✓ {lib} 安装成功")
            except subprocess.CalledProcessError:
                print(f"✗ {lib} 安装失败")

def extract_text_from_pdf(pdf_path: str) -> str:
    """从PDF文件中提取文本"""
    text = ""
    
    # 尝试使用不同的PDF库
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        print(f"✓ 使用PyPDF2成功提取 {pdf_path}")
    except Exception as e:
        print(f"PyPDF2提取失败: {e}")
        
        try:
            import pdfplumber
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            print(f"✓ 使用pdfplumber成功提取 {pdf_path}")
        except Exception as e:
            print(f"pdfplumber提取失败: {e}")
            
            try:
                import fitz  # PyMuPDF
                doc = fitz.open(pdf_path)
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    text += page.get_text() + "\n"
                doc.close()
                print(f"✓ 使用PyMuPDF成功提取 {pdf_path}")
            except Exception as e:
                print(f"PyMuPDF提取失败: {e}")
                return ""
    
    return text

def parse_recipe_from_text(text: str, filename: str) -> List[Dict]:
    """从文本中解析配方"""
    recipes = []
    
    # 根据文件名选择不同的解析策略
    if "43个DIY护肤品配方" in filename:
        recipes.extend(parse_43_recipes(text))
    elif "精油配方大全" in filename:
        recipes.extend(parse_essential_oil_recipes(text))
    elif "自制化妆品DIY配方" in filename:
        recipes.extend(parse_diy_recipes(text))
    elif "牛尔的爱美书" in filename:
        recipes.extend(parse_nioer_recipes(text))
    else:
        recipes.extend(parse_generic_recipes(text))
    
    return recipes

def parse_43_recipes(text: str) -> List[Dict]:
    """解析43个DIY护肤品配方"""
    recipes = []
    
    # 查找配方标题模式
    title_patterns = [
        r'配方\s*\d+[：:]\s*([^\n]+)',
        r'第\s*\d+\s*个[：:]\s*([^\n]+)',
        r'^\s*\d+[、.]\s*([^\n]+)',
        r'^\s*([^\n]*面霜[^\n]*)',
        r'^\s*([^\n]*面膜[^\n]*)',
        r'^\s*([^\n]*精华[^\n]*)',
        r'^\s*([^\n]*乳液[^\n]*)'
    ]
    
    lines = text.split('\n')
    current_recipe = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # 检查是否是配方标题
        for pattern in title_patterns:
            match = re.search(pattern, line)
            if match:
                if current_recipe:
                    recipes.append(current_recipe)
                
                title = match.group(1).strip()
                current_recipe = {
                    'name': title,
                    'category': determine_category(title),
                    'description': '',
                    'ingredients': [],
                    'steps': [],
                    'benefits': [],
                    'usage': []
                }
                break
        
        # 解析原料
        if current_recipe and ('原料' in line or '成分' in line or '材料' in line):
            ingredients = parse_ingredients_from_text(text, i)
            current_recipe['ingredients'] = ingredients
        
        # 解析制作步骤
        if current_recipe and ('制作' in line or '步骤' in line or '方法' in line):
            steps = parse_steps_from_text(text, i)
            current_recipe['steps'] = steps
    
    if current_recipe:
        recipes.append(current_recipe)
    
    return recipes

def parse_essential_oil_recipes(text: str) -> List[Dict]:
    """解析精油配方"""
    recipes = []
    
    # 精油配方通常包含精油名称和基础油
    oil_patterns = [
        r'([^，,]+精油)[：:]([^\n]+)',
        r'([^，,]+油)[：:]([^\n]+)',
        r'配方[：:]([^\n]+)'
    ]
    
    for pattern in oil_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if len(match) == 2:
                name, description = match
                recipes.append({
                    'name': name.strip(),
                    'category': '精油',
                    'description': description.strip(),
                    'ingredients': [],
                    'steps': [],
                    'benefits': [],
                    'usage': []
                })
    
    return recipes

def parse_diy_recipes(text: str) -> List[Dict]:
    """解析DIY配方"""
    recipes = []
    
    # DIY配方通常有明确的标题
    diy_patterns = [
        r'([^，,]*DIY[^，,]*)',
        r'([^，,]*自制[^，,]*)',
        r'([^，,]*配方[^，,]*)'
    ]
    
    for pattern in diy_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            recipes.append({
                'name': match.strip(),
                'category': '护肤品',
                'description': 'DIY自制配方',
                'ingredients': [],
                'steps': [],
                'benefits': [],
                'usage': []
            })
    
    return recipes

def parse_nioer_recipes(text: str) -> List[Dict]:
    """解析牛尔配方"""
    recipes = []
    
    # 牛尔的配方通常有特定的命名模式
    nioer_patterns = [
        r'([^，,]*牛尔[^，,]*)',
        r'([^，,]*推荐[^，,]*)',
        r'([^，,]*秘方[^，,]*)'
    ]
    
    for pattern in nioer_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            recipes.append({
                'name': match.strip(),
                'category': '护肤品',
                'description': '牛尔推荐配方',
                'ingredients': [],
                'steps': [],
                'benefits': [],
                'usage': []
            })
    
    return recipes

def parse_generic_recipes(text: str) -> List[Dict]:
    """解析通用配方"""
    recipes = []
    
    # 通用模式：查找包含化妆品关键词的行
    cosmetic_keywords = ['面霜', '面膜', '精华', '乳液', '洗发水', '护发素', '精油', '爽肤水']
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        for keyword in cosmetic_keywords:
            if keyword in line and len(line) < 50:  # 标题通常较短
                recipes.append({
                    'name': line,
                    'category': determine_category(line),
                    'description': '从PDF提取的配方',
                    'ingredients': [],
                    'steps': [],
                    'benefits': [],
                    'usage': []
                })
                break
    
    return recipes

def determine_category(name: str) -> str:
    """根据名称确定分类"""
    if any(word in name for word in ['面膜', '泥膜', '贴膜']):
        return '面膜'
    elif any(word in name for word in ['洗发水', '护发素', '发膜', '护发']):
        return '护发产品'
    elif any(word in name for word in ['精油', '按摩油', '香薰']):
        return '精油'
    else:
        return '护肤品'

def parse_ingredients_from_text(text: str, start_index: int) -> List[Dict]:
    """从文本中解析原料信息"""
    ingredients = []
    lines = text.split('\n')
    
    # 查找原料列表
    for i in range(start_index, min(start_index + 20, len(lines))):
        line = lines[i].strip()
        
        # 匹配原料模式
        patterns = [
            r'([^，,]+)[：:]\s*(\d+[gml滴%]+)',
            r'([^，,]+)\s+(\d+[gml滴%]+)',
            r'(\d+[gml滴%]+)\s+([^，,]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                if len(match.groups()) == 2:
                    if match.group(1).replace(' ', '').replace('：', '').replace(':', '').isdigit():
                        amount = match.group(1)
                        name = match.group(2)
                    else:
                        name = match.group(1)
                        amount = match.group(2)
                    
                    ingredients.append({
                        'name': name.strip(),
                        'amount': amount.strip(),
                        'percentage': 0.0,
                        'unit': 'g',
                        'phase': '未知'
                    })
    
    return ingredients

def parse_steps_from_text(text: str, start_index: int) -> List[Dict]:
    """从文本中解析制作步骤"""
    steps = []
    lines = text.split('\n')
    
    step_number = 1
    for i in range(start_index, min(start_index + 30, len(lines))):
        line = lines[i].strip()
        
        # 查找步骤模式
        if re.search(r'[1-9][、.]|步骤|制作|方法', line):
            steps.append({
                'step_number': step_number,
                'description': line,
                'temperature': '',
                'mixing_time': '',
                'notes': ''
            })
            step_number += 1
    
    return steps

def extract_all_pdf_recipes():
    """提取所有PDF文件中的配方"""
    print("开始提取PDF文件中的配方...")
    
    # 安装PDF处理库
    install_pdf_libraries()
    
    # 查找PDF文件
    pdf_files = []
    for file in os.listdir('.'):
        if file.endswith('.pdf'):
            pdf_files.append(file)
    
    print(f"找到 {len(pdf_files)} 个PDF文件:")
    for pdf_file in pdf_files:
        print(f"  - {pdf_file}")
    
    all_recipes = []
    
    for pdf_file in pdf_files:
        print(f"\n正在处理: {pdf_file}")
        try:
            text = extract_text_from_pdf(pdf_file)
            if text:
                recipes = parse_recipe_from_text(text, pdf_file)
                print(f"从 {pdf_file} 提取到 {len(recipes)} 个配方")
                all_recipes.extend(recipes)
            else:
                print(f"无法从 {pdf_file} 提取文本")
        except Exception as e:
            print(f"处理 {pdf_file} 时出错: {e}")
    
    print(f"\n总共提取到 {len(all_recipes)} 个配方")
    
    # 保存提取的配方到数据库
    if all_recipes:
        db = CosmeticsDatabase()
        added_count = 0
        
        for recipe in all_recipes:
            try:
                product_id = db.add_product(recipe["name"], recipe["category"], recipe["description"])
                
                if product_id:
                    # 添加原料
                    for ingredient_data in recipe["ingredients"]:
                        ingredient_id = db.add_ingredient(ingredient_data["name"])
                        db.add_formulation(
                            product_id, ingredient_id, 
                            ingredient_data["amount"], 
                            ingredient_data["percentage"],
                            ingredient_data["unit"],
                            ingredient_data["phase"]
                        )
                    
                    # 添加制作步骤
                    for step in recipe["steps"]:
                        db.add_recipe_step(
                            product_id, step["step_number"], step["description"],
                            step["temperature"], step["mixing_time"], step["notes"]
                        )
                    
                    added_count += 1
                    print(f"✓ 已添加配方: {recipe['name']}")
            except Exception as e:
                print(f"✗ 添加配方失败: {recipe['name']}, 错误: {e}")
        
        print(f"\n成功添加 {added_count} 个新配方到数据库")
        
        # 显示最终统计
        products = db.search_products()
        print(f"数据库现在总共有 {len(products)} 个配方")
    else:
        print("没有提取到任何配方")

if __name__ == "__main__":
    extract_all_pdf_recipes()
