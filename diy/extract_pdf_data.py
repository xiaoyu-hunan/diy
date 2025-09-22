#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF内容提取和数据库建立脚本
用于化妆品DIY网页项目
"""

import sqlite3
import os
import json
from typing import List, Dict, Any
import re

class CosmeticsDatabase:
    def __init__(self, db_path: str = "cosmetics_diy.db"):
        """初始化数据库连接"""
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """创建数据库表结构"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 创建产品表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # 创建原料表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            function TEXT,
            safety_info TEXT,
            hlb_value REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # 创建制作工序表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            step_number INTEGER,
            step_description TEXT,
            temperature TEXT,
            mixing_time TEXT,
            notes TEXT,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
        ''')
        
        # 创建配方表（产品-原料关系）
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS formulations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            ingredient_id INTEGER,
            amount TEXT,
            percentage REAL,
            unit TEXT,
            phase TEXT,
            FOREIGN KEY (product_id) REFERENCES products (id),
            FOREIGN KEY (ingredient_id) REFERENCES ingredients (id)
        )
        ''')
        
        # 创建功效表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS benefits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            benefit_name TEXT,
            description TEXT,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
        ''')
        
        # 创建使用方法表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usage_instructions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            instruction TEXT,
            frequency TEXT,
            precautions TEXT,
            storage_conditions TEXT,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
        ''')
        
        conn.commit()
        conn.close()
        print("数据库初始化完成！")
    
    def add_product(self, name: str, category: str, description: str = "") -> int:
        """添加产品"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO products (name, category, description) VALUES (?, ?, ?)",
                (name, category, description)
            )
            product_id = cursor.lastrowid
            if product_id == 0:  # 如果产品已存在，获取其ID
                cursor.execute("SELECT id FROM products WHERE name = ?", (name,))
                product_id = cursor.fetchone()[0]
            conn.commit()
            return product_id
        except Exception as e:
            print(f"添加产品时出错: {e}")
            return None
        finally:
            conn.close()
    
    def add_ingredient(self, name: str, function: str = "", safety_info: str = "", hlb_value: float = None) -> int:
        """添加原料"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO ingredients (name, function, safety_info, hlb_value) VALUES (?, ?, ?, ?)",
                (name, function, safety_info, hlb_value)
            )
            ingredient_id = cursor.lastrowid
            if ingredient_id == 0:  # 如果原料已存在，获取其ID
                cursor.execute("SELECT id FROM ingredients WHERE name = ?", (name,))
                ingredient_id = cursor.fetchone()[0]
            conn.commit()
            return ingredient_id
        except Exception as e:
            print(f"添加原料时出错: {e}")
            return None
        finally:
            conn.close()
    
    def add_formulation(self, product_id: int, ingredient_id: int, amount: str, percentage: float = None, unit: str = "", phase: str = ""):
        """添加配方"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO formulations (product_id, ingredient_id, amount, percentage, unit, phase) VALUES (?, ?, ?, ?, ?, ?)",
                (product_id, ingredient_id, amount, percentage, unit, phase)
            )
            conn.commit()
        except Exception as e:
            print(f"添加配方时出错: {e}")
        finally:
            conn.close()
    
    def add_recipe_step(self, product_id: int, step_number: int, step_description: str, temperature: str = "", mixing_time: str = "", notes: str = ""):
        """添加制作步骤"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO recipes (product_id, step_number, step_description, temperature, mixing_time, notes) VALUES (?, ?, ?, ?, ?, ?)",
                (product_id, step_number, step_description, temperature, mixing_time, notes)
            )
            conn.commit()
        except Exception as e:
            print(f"添加制作步骤时出错: {e}")
        finally:
            conn.close()
    
    def add_benefit(self, product_id: int, benefit_name: str, description: str = ""):
        """添加功效"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO benefits (product_id, benefit_name, description) VALUES (?, ?, ?)",
                (product_id, benefit_name, description)
            )
            conn.commit()
        except Exception as e:
            print(f"添加功效时出错: {e}")
        finally:
            conn.close()
    
    def add_usage_instruction(self, product_id: int, instruction: str, frequency: str = "", precautions: str = "", storage_conditions: str = ""):
        """添加使用方法"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO usage_instructions (product_id, instruction, frequency, precautions, storage_conditions) VALUES (?, ?, ?, ?, ?)",
                (product_id, instruction, frequency, precautions, storage_conditions)
            )
            conn.commit()
        except Exception as e:
            print(f"添加使用方法时出错: {e}")
        finally:
            conn.close()
    
    def search_products(self, keyword: str = "") -> List[Dict]:
        """搜索产品"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if keyword:
            cursor.execute(
                "SELECT id, name, category, description FROM products WHERE name LIKE ? OR description LIKE ?",
                (f"%{keyword}%", f"%{keyword}%")
            )
        else:
            cursor.execute("SELECT id, name, category, description FROM products ORDER BY name")
        
        products = []
        for row in cursor.fetchall():
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'description': row[3]
            })
        
        conn.close()
        return products
    
    def get_product_details(self, product_id: int) -> Dict:
        """获取产品详细信息"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 获取产品基本信息
        cursor.execute("SELECT name, category, description FROM products WHERE id = ?", (product_id,))
        product_info = cursor.fetchone()
        
        if not product_info:
            return None
        
        # 获取配方
        cursor.execute('''
        SELECT i.name, f.amount, f.percentage, f.unit, f.phase
        FROM formulations f
        JOIN ingredients i ON f.ingredient_id = i.id
        WHERE f.product_id = ?
        ORDER BY f.id
        ''', (product_id,))
        ingredients = []
        for row in cursor.fetchall():
            ingredients.append({
                'name': row[0],
                'amount': row[1],
                'percentage': row[2],
                'unit': row[3],
                'phase': row[4]
            })
        
        # 获取制作步骤
        cursor.execute('''
        SELECT step_number, step_description, temperature, mixing_time, notes
        FROM recipes
        WHERE product_id = ?
        ORDER BY step_number
        ''', (product_id,))
        steps = []
        for row in cursor.fetchall():
            steps.append({
                'step_number': row[0],
                'description': row[1],
                'temperature': row[2],
                'mixing_time': row[3],
                'notes': row[4]
            })
        
        # 获取功效
        cursor.execute("SELECT benefit_name, description FROM benefits WHERE product_id = ?", (product_id,))
        benefits = []
        for row in cursor.fetchall():
            benefits.append({
                'name': row[0],
                'description': row[1]
            })
        
        # 获取使用方法
        cursor.execute("SELECT instruction, frequency, precautions, storage_conditions FROM usage_instructions WHERE product_id = ?", (product_id,))
        usage = []
        for row in cursor.fetchall():
            usage.append({
                'instruction': row[0],
                'frequency': row[1],
                'precautions': row[2],
                'storage_conditions': row[3]
            })
        
        conn.close()
        
        return {
            'id': product_id,
            'name': product_info[0],
            'category': product_info[1],
            'description': product_info[2],
            'ingredients': ingredients,
            'steps': steps,
            'benefits': benefits,
            'usage': usage
        }

def parse_pdf_content():
    """
    解析PDF内容的示例函数
    由于无法直接读取PDF，这里提供示例数据结构
    """
    db = CosmeticsDatabase()
    
    # 示例数据 - 基于常见的DIY护肤品配方
    sample_recipes = [
        {
            "name": "薰衣草保湿面霜",
            "category": "护肤品",
            "description": "适合干性皮肤的保湿面霜，具有舒缓功效",
            "ingredients": [
                {"name": "椰子油", "amount": "30g", "percentage": 30.0, "unit": "g", "phase": "油相"},
                {"name": "乳木果油", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "油相"},
                {"name": "薰衣草精油", "amount": "5滴", "percentage": 0.5, "unit": "滴", "phase": "精油相"},
                {"name": "维生素E", "amount": "2滴", "percentage": 0.2, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将椰子油和乳木果油放入玻璃碗中", "temperature": "室温", "mixing_time": "", "notes": "确保容器干净"},
                {"step_number": 2, "description": "隔水加热至完全融化", "temperature": "60-70°C", "mixing_time": "5-10分钟", "notes": "不要过热"},
                {"step_number": 3, "description": "冷却至室温后加入薰衣草精油", "temperature": "室温", "mixing_time": "", "notes": "轻轻搅拌"},
                {"step_number": 4, "description": "加入维生素E并搅拌均匀", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保充分混合"}
            ],
            "benefits": [
                {"name": "保湿", "description": "深层滋润肌肤，防止水分流失"},
                {"name": "舒缓", "description": "薰衣草精油具有舒缓镇静功效"}
            ],
            "usage": [
                {"instruction": "洁面后取适量涂抹于面部", "frequency": "早晚各一次", "precautions": "避免接触眼部", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "茶树精油祛痘凝胶",
            "category": "护肤品",
            "description": "针对痘痘肌肤的祛痘凝胶，具有抗菌消炎功效",
            "ingredients": [
                {"name": "芦荟凝胶", "amount": "50g", "percentage": 83.3, "unit": "g", "phase": "基质"},
                {"name": "茶树精油", "amount": "8滴", "percentage": 1.3, "unit": "滴", "phase": "活性成分"},
                {"name": "薰衣草精油", "amount": "2滴", "percentage": 0.3, "unit": "滴", "phase": "活性成分"}
            ],
            "steps": [
                {"step_number": 1, "description": "将芦荟凝胶放入干净容器中", "temperature": "室温", "mixing_time": "", "notes": "确保容器无菌"},
                {"step_number": 2, "description": "加入茶树精油并充分搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保精油完全分散"},
                {"step_number": 3, "description": "加入薰衣草精油并混合均匀", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "避免过度搅拌"}
            ],
            "benefits": [
                {"name": "抗菌", "description": "茶树精油具有强效抗菌作用"},
                {"name": "消炎", "description": "减少炎症反应，促进愈合"},
                {"name": "控油", "description": "调节皮脂分泌"}
            ],
            "usage": [
                {"instruction": "清洁后点涂于痘痘部位", "frequency": "每日2-3次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "冷藏保存，开封后3个月内使用"}
            ]
        },
        {
            "name": "玫瑰保湿精华液",
            "category": "护肤品",
            "description": "富含玫瑰精华的保湿精华液，适合所有肌肤类型",
            "ingredients": [
                {"name": "玫瑰纯露", "amount": "40ml", "percentage": 80.0, "unit": "ml", "phase": "水相"},
                {"name": "透明质酸", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "保湿剂"},
                {"name": "甘油", "amount": "5ml", "percentage": 10.0, "unit": "ml", "phase": "保湿剂"},
                {"name": "玫瑰精油", "amount": "3滴", "percentage": 0.6, "unit": "滴", "phase": "精油相"},
                {"name": "防腐剂", "amount": "2滴", "percentage": 0.4, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将玫瑰纯露倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用玻璃容器"},
                {"step_number": 2, "description": "加入透明质酸并搅拌至完全溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分搅拌避免结块"},
                {"step_number": 3, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保充分混合"},
                {"step_number": 4, "description": "加入玫瑰精油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "轻轻搅拌"},
                {"step_number": 5, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1分钟", "notes": "确保均匀分布"}
            ],
            "benefits": [
                {"name": "深层保湿", "description": "透明质酸和甘油双重保湿"},
                {"name": "抗衰老", "description": "玫瑰精华具有抗氧化功效"},
                {"name": "舒缓肌肤", "description": "玫瑰成分温和舒缓"}
            ],
            "usage": [
                {"instruction": "洁面后使用，取2-3滴轻拍于面部", "frequency": "早晚各一次", "precautions": "避开眼部", "storage_conditions": "阴凉干燥处，开封后6个月内使用"}
            ]
        },
        {
            "name": "柠檬美白面膜",
            "category": "面膜",
            "description": "天然柠檬美白面膜，具有提亮肤色功效",
            "ingredients": [
                {"name": "柠檬汁", "amount": "15ml", "percentage": 30.0, "unit": "ml", "phase": "活性成分"},
                {"name": "蜂蜜", "amount": "25g", "percentage": 50.0, "unit": "g", "phase": "基质"},
                {"name": "燕麦粉", "amount": "10g", "percentage": 20.0, "unit": "g", "phase": "磨砂剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将蜂蜜倒入碗中", "temperature": "室温", "mixing_time": "", "notes": "使用天然蜂蜜"},
                {"step_number": 2, "description": "加入柠檬汁并搅拌", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "最后加入燕麦粉调成糊状", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "调至适合涂抹的稠度"}
            ],
            "benefits": [
                {"name": "美白", "description": "柠檬维生素C具有美白功效"},
                {"name": "去角质", "description": "燕麦粉温和去角质"},
                {"name": "保湿", "description": "蜂蜜提供天然保湿"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，避开眼部", "frequency": "每周2-3次", "precautions": "敏感肌肤慎用，避免阳光照射", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "薄荷清爽洗发水",
            "category": "护发产品",
            "description": "天然薄荷洗发水，清洁头皮，控油去屑",
            "ingredients": [
                {"name": "椰子油起泡剂", "amount": "100ml", "percentage": 40.0, "unit": "ml", "phase": "表面活性剂"},
                {"name": "纯净水", "amount": "120ml", "percentage": 48.0, "unit": "ml", "phase": "水相"},
                {"name": "薄荷精油", "amount": "10滴", "percentage": 0.4, "unit": "滴", "phase": "精油相"},
                {"name": "茶树精油", "amount": "5滴", "percentage": 0.2, "unit": "滴", "phase": "精油相"},
                {"name": "甘油", "amount": "10ml", "percentage": 4.0, "unit": "ml", "phase": "保湿剂"},
                {"name": "防腐剂", "amount": "3滴", "percentage": 0.12, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将椰子油起泡剂倒入容器", "temperature": "室温", "mixing_time": "", "notes": "使用干净容器"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入甘油并搅拌", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保充分溶解"},
                {"step_number": 4, "description": "加入薄荷精油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "轻轻搅拌"},
                {"step_number": 5, "description": "加入茶树精油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "确保精油均匀分布"},
                {"step_number": 6, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1分钟", "notes": "充分混合"}
            ],
            "benefits": [
                {"name": "深层清洁", "description": "温和清洁头皮和头发"},
                {"name": "控油", "description": "薄荷成分调节头皮油脂分泌"},
                {"name": "去屑", "description": "茶树精油具有抗菌去屑功效"},
                {"name": "清爽", "description": "薄荷带来清凉感受"}
            ],
            "usage": [
                {"instruction": "湿发后取适量按摩头皮和头发", "frequency": "每周2-3次", "precautions": "避开眼部，如进入眼睛立即冲洗", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        }
    ]
    
    # 添加示例数据到数据库
    for recipe in sample_recipes:
        # 添加产品
        product_id = db.add_product(recipe["name"], recipe["category"], recipe["description"])
        
        if product_id:
            # 添加原料和配方
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
            
            # 添加功效
            for benefit in recipe["benefits"]:
                db.add_benefit(product_id, benefit["name"], benefit["description"])
            
            # 添加使用方法
            for usage in recipe["usage"]:
                db.add_usage_instruction(
                    product_id, usage["instruction"], usage["frequency"],
                    usage["precautions"], usage["storage_conditions"]
                )
            
            print(f"已添加产品: {recipe['name']}")

if __name__ == "__main__":
    print("开始建立化妆品DIY数据库...")
    parse_pdf_content()
    print("数据库建立完成！")
    
    # 测试搜索功能
    db = CosmeticsDatabase()
    products = db.search_products()
    print(f"\n数据库中共有 {len(products)} 个产品:")
    for product in products:
        print(f"- {product['name']} ({product['category']})")
