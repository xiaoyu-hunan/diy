#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
专业配方数据库 - 基于化妆品制造学等专业PDF文件
"""

from extract_pdf_data import CosmeticsDatabase

def add_professional_recipes():
    """添加专业级配方"""
    db = CosmeticsDatabase()
    
    # 基于"化妆品制造学.pdf"的专业配方
    professional_recipes = [
        {
            "name": "氨基酸泡沫洁面慕斯",
            "category": "护肤品",
            "description": "专业氨基酸泡沫洁面慕斯，温和清洁不伤肌肤屏障",
            "ingredients": [
                {"name": "氨基酸表面活性剂", "amount": "25g", "percentage": 25.0, "unit": "g", "phase": "表面活性剂"},
                {"name": "椰油酰胺丙基甜菜碱", "amount": "10g", "percentage": 10.0, "unit": "g", "phase": "表面活性剂"},
                {"name": "纯净水", "amount": "55g", "percentage": 55.0, "unit": "g", "phase": "水相"},
                {"name": "甘油", "amount": "8g", "percentage": 8.0, "unit": "g", "phase": "保湿剂"},
                {"name": "透明质酸", "amount": "2g", "percentage": 2.0, "unit": "g", "phase": "保湿剂"},
                {"name": "防腐剂", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用蒸馏水或纯净水"},
                {"step_number": 2, "description": "加入氨基酸表面活性剂并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入椰油酰胺丙基甜菜碱", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "增加泡沫丰富度"},
                {"step_number": 4, "description": "加入甘油和透明质酸", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解"},
                {"step_number": 5, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "充分混合"}
            ],
            "benefits": [
                {"name": "温和清洁", "description": "氨基酸表面活性剂温和不刺激"},
                {"name": "丰富泡沫", "description": "产生细腻丰富的泡沫"},
                {"name": "保湿", "description": "多重保湿成分保持肌肤水润"}
            ],
            "usage": [
                {"instruction": "湿润面部后取适量轻柔按摩，产生丰富泡沫后用温水洗净", "frequency": "早晚各一次", "precautions": "避免接触眼部", "storage_conditions": "阴凉干燥处，开封后6个月内使用"}
            ]
        },
        {
            "name": "神经酰胺修复面霜",
            "category": "护肤品",
            "description": "神经酰胺修复面霜，修复肌肤屏障深层滋润",
            "ingredients": [
                {"name": "神经酰胺", "amount": "3g", "percentage": 3.0, "unit": "g", "phase": "活性成分"},
                {"name": "乳木果油", "amount": "30g", "percentage": 30.0, "unit": "g", "phase": "油相"},
                {"name": "荷荷巴油", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "12g", "percentage": 12.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "35g", "percentage": 35.0, "unit": "g", "phase": "水相"},
                {"name": "维生素E", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将乳木果油、荷荷巴油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70-80°C", "mixing_time": "10-15分钟", "notes": "持续搅拌形成乳液"},
                {"step_number": 4, "description": "冷却至40°C后加入神经酰胺", "temperature": "40°C", "mixing_time": "3-5分钟", "notes": "避免高温破坏活性成分"},
                {"step_number": 5, "description": "最后加入维生素E", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "抗氧化保护"}
            ],
            "benefits": [
                {"name": "修复屏障", "description": "神经酰胺修复肌肤屏障功能"},
                {"name": "深层滋润", "description": "多重油脂深层滋润肌肤"},
                {"name": "抗敏感", "description": "减少肌肤敏感反应"}
            ],
            "usage": [
                {"instruction": "洁面后取适量轻柔按摩至吸收", "frequency": "早晚各一次", "precautions": "适合敏感肌肤使用", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "角鲨烷保湿精华油",
            "category": "护肤品",
            "description": "角鲨烷保湿精华油，模拟人体皮脂深层滋养",
            "ingredients": [
                {"name": "角鲨烷", "amount": "40ml", "percentage": 80.0, "unit": "ml", "phase": "油相"},
                {"name": "荷荷巴油", "amount": "8ml", "percentage": 16.0, "unit": "ml", "phase": "油相"},
                {"name": "维生素E", "amount": "2ml", "percentage": 4.0, "unit": "ml", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将角鲨烷倒入深色玻璃瓶", "temperature": "室温", "mixing_time": "", "notes": "使用深色玻璃瓶避免光照"},
                {"step_number": 2, "description": "加入荷荷巴油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "轻轻摇晃混合"},
                {"step_number": 3, "description": "最后加入维生素E", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃使成分均匀分布"}
            ],
            "benefits": [
                {"name": "深层滋养", "description": "角鲨烷模拟人体皮脂，深层滋养"},
                {"name": "长效保湿", "description": "形成保护膜，长效保湿"},
                {"name": "温和不刺激", "description": "适合所有肌肤类型"}
            ],
            "usage": [
                {"instruction": "洁面后取2-3滴轻拍于面部至吸收", "frequency": "早晚各一次", "precautions": "适合所有肌肤类型", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "多肽紧致眼霜",
            "category": "护肤品",
            "description": "多肽紧致眼霜，减少眼部细纹紧致眼周肌肤",
            "ingredients": [
                {"name": "六胜肽", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "活性成分"},
                {"name": "乳木果油", "amount": "25g", "percentage": 50.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "10g", "percentage": 20.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "10g", "percentage": 20.0, "unit": "g", "phase": "水相"},
                {"name": "维生素E", "amount": "2滴", "percentage": 0.4, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将乳木果油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70-80°C", "mixing_time": "10-15分钟", "notes": "持续搅拌形成霜状"},
                {"step_number": 4, "description": "冷却至40°C后加入六胜肽", "temperature": "40°C", "mixing_time": "3-5分钟", "notes": "避免高温破坏活性成分"},
                {"step_number": 5, "description": "最后加入维生素E", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "抗氧化保护"}
            ],
            "benefits": [
                {"name": "紧致眼周", "description": "六胜肽紧致眼周肌肤"},
                {"name": "减少细纹", "description": "改善眼部细纹"},
                {"name": "深层滋润", "description": "乳木果油深层滋润眼周"}
            ],
            "usage": [
                {"instruction": "洁面后取米粒大小轻柔点涂于眼周", "frequency": "早晚各一次", "precautions": "避免接触眼球", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        },
        {
            "name": "硅油护发精华",
            "category": "护发产品",
            "description": "硅油护发精华，顺滑发丝增加光泽",
            "ingredients": [
                {"name": "环五聚二甲基硅氧烷", "amount": "80ml", "percentage": 80.0, "unit": "ml", "phase": "油相"},
                {"name": "荷荷巴油", "amount": "15ml", "percentage": 15.0, "unit": "ml", "phase": "油相"},
                {"name": "维生素E", "amount": "5ml", "percentage": 5.0, "unit": "ml", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将环五聚二甲基硅氧烷倒入容器", "temperature": "室温", "mixing_time": "", "notes": "使用干净容器"},
                {"step_number": 2, "description": "加入荷荷巴油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "轻轻摇晃混合"},
                {"step_number": 3, "description": "最后加入维生素E", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃使成分均匀分布"}
            ],
            "benefits": [
                {"name": "顺滑发丝", "description": "硅油使发丝更加顺滑"},
                {"name": "增加光泽", "description": "提升头发光泽度"},
                {"name": "减少毛躁", "description": "减少头发毛躁"}
            ],
            "usage": [
                {"instruction": "洗发后取适量涂抹于发梢，避免接触头皮", "frequency": "每次洗发后", "precautions": "避免接触头皮", "storage_conditions": "阴凉干燥处，开封后6个月内使用"}
            ]
        },
        {
            "name": "茶树精油控油爽肤水",
            "category": "护肤品",
            "description": "茶树精油控油爽肤水，调节皮脂分泌收缩毛孔",
            "ingredients": [
                {"name": "茶树精油", "amount": "8滴", "percentage": 1.6, "unit": "滴", "phase": "精油"},
                {"name": "纯净水", "amount": "45ml", "percentage": 90.0, "unit": "ml", "phase": "水相"},
                {"name": "金缕梅提取物", "amount": "3ml", "percentage": 6.0, "unit": "ml", "phase": "活性成分"},
                {"name": "甘油", "amount": "2ml", "percentage": 4.0, "unit": "ml", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用蒸馏水或纯净水"},
                {"step_number": 2, "description": "加入金缕梅提取物并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保充分混合"},
                {"step_number": 4, "description": "最后加入茶树精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃混合"}
            ],
            "benefits": [
                {"name": "控油", "description": "茶树精油调节皮脂分泌"},
                {"name": "收缩毛孔", "description": "金缕梅收缩毛孔"},
                {"name": "抗菌", "description": "茶树精油具有抗菌作用"}
            ],
            "usage": [
                {"instruction": "洁面后轻拍于面部，可重复使用", "frequency": "早晚各一次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        },
        {
            "name": "乳糖酸去角质精华",
            "category": "护肤品",
            "description": "乳糖酸去角质精华，温和去角质改善肌肤质地",
            "ingredients": [
                {"name": "乳糖酸", "amount": "5ml", "percentage": 10.0, "unit": "ml", "phase": "活性成分"},
                {"name": "纯净水", "amount": "35ml", "percentage": 70.0, "unit": "ml", "phase": "水相"},
                {"name": "透明质酸", "amount": "3g", "percentage": 6.0, "unit": "g", "phase": "保湿剂"},
                {"name": "甘油", "amount": "5ml", "percentage": 10.0, "unit": "ml", "phase": "保湿剂"},
                {"name": "维生素E", "amount": "2滴", "percentage": 0.4, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用蒸馏水或纯净水"},
                {"step_number": 2, "description": "加入透明质酸并搅拌至完全溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解避免结块"},
                {"step_number": 3, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"},
                {"step_number": 4, "description": "加入乳糖酸", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合，注意浓度控制"},
                {"step_number": 5, "description": "最后加入维生素E", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "抗氧化保护"}
            ],
            "benefits": [
                {"name": "温和去角质", "description": "乳糖酸温和去除老化角质"},
                {"name": "改善质地", "description": "促进细胞更新，改善肌肤质地"},
                {"name": "保湿", "description": "多重保湿成分保持肌肤水润"}
            ],
            "usage": [
                {"instruction": "洁面后取2-3滴轻拍于面部", "frequency": "每周2-3次", "precautions": "使用后必须防晒，敏感肌肤慎用", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        },
        {
            "name": "薰衣草洋甘菊舒缓喷雾",
            "category": "精油",
            "description": "薰衣草洋甘菊舒缓喷雾，缓解肌肤不适舒缓敏感",
            "ingredients": [
                {"name": "纯净水", "amount": "90ml", "percentage": 90.0, "unit": "ml", "phase": "水相"},
                {"name": "薰衣草精油", "amount": "8滴", "percentage": 0.8, "unit": "滴", "phase": "精油"},
                {"name": "洋甘菊精油", "amount": "4滴", "percentage": 0.4, "unit": "滴", "phase": "精油"},
                {"name": "金缕梅提取物", "amount": "5ml", "percentage": 5.0, "unit": "ml", "phase": "活性成分"},
                {"name": "甘油", "amount": "5ml", "percentage": 5.0, "unit": "ml", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入喷雾瓶", "temperature": "室温", "mixing_time": "", "notes": "使用干净的喷雾瓶"},
                {"step_number": 2, "description": "加入金缕梅提取物并摇晃", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入甘油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合"},
                {"step_number": 4, "description": "加入薰衣草精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃混合"},
                {"step_number": 5, "description": "最后加入洋甘菊精油", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保精油完全分散"}
            ],
            "benefits": [
                {"name": "舒缓敏感", "description": "薰衣草和洋甘菊舒缓敏感肌肤"},
                {"name": "抗炎", "description": "减少肌肤炎症反应"},
                {"name": "保湿", "description": "甘油保持肌肤水润"}
            ],
            "usage": [
                {"instruction": "洁面后或需要时喷洒于面部", "frequency": "根据需要", "precautions": "避开眼部，敏感肌肤适用", "storage_conditions": "阴凉干燥处，使用前摇匀"}
            ]
        },
        {
            "name": "胜肽抗衰老面膜",
            "category": "面膜",
            "description": "胜肽抗衰老面膜，促进胶原蛋白生成减少细纹",
            "ingredients": [
                {"name": "五胜肽", "amount": "3g", "percentage": 6.0, "unit": "g", "phase": "活性成分"},
                {"name": "透明质酸", "amount": "10g", "percentage": 20.0, "unit": "g", "phase": "保湿剂"},
                {"name": "海藻粉", "amount": "20g", "percentage": 40.0, "unit": "g", "phase": "基质"},
                {"name": "纯净水", "amount": "15g", "percentage": 30.0, "unit": "g", "phase": "水相"},
                {"name": "甘油", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将海藻粉倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "确保容器无菌"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "加入透明质酸并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解"},
                {"step_number": 4, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"},
                {"step_number": 5, "description": "最后加入五胜肽", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "避免过度搅拌"}
            ],
            "benefits": [
                {"name": "抗衰老", "description": "五胜肽促进胶原蛋白生成"},
                {"name": "减少细纹", "description": "改善肌肤质地，减少细纹"},
                {"name": "深层保湿", "description": "透明质酸深层保湿"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，20分钟后洗净", "frequency": "每周2-3次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "迷迭香薄荷控油洗发水",
            "category": "护发产品",
            "description": "迷迭香薄荷控油洗发水，深层清洁控油去屑",
            "ingredients": [
                {"name": "椰子油起泡剂", "amount": "120ml", "percentage": 48.0, "unit": "ml", "phase": "表面活性剂"},
                {"name": "纯净水", "amount": "100ml", "percentage": 40.0, "unit": "ml", "phase": "水相"},
                {"name": "迷迭香精油", "amount": "12滴", "percentage": 0.48, "unit": "滴", "phase": "精油"},
                {"name": "薄荷精油", "amount": "8滴", "percentage": 0.32, "unit": "滴", "phase": "精油"},
                {"name": "甘油", "amount": "15ml", "percentage": 6.0, "unit": "ml", "phase": "保湿剂"},
                {"name": "防腐剂", "amount": "4滴", "percentage": 0.16, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将椰子油起泡剂倒入容器", "temperature": "室温", "mixing_time": "", "notes": "使用干净容器"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入甘油并搅拌", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保充分溶解"},
                {"step_number": 4, "description": "加入迷迭香精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合"},
                {"step_number": 5, "description": "加入薄荷精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保精油均匀分布"},
                {"step_number": 6, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "充分混合"}
            ],
            "benefits": [
                {"name": "深层清洁", "description": "温和清洁头皮和头发"},
                {"name": "控油", "description": "迷迭香和薄荷调节皮脂分泌"},
                {"name": "去屑", "description": "具有去屑功效"},
                {"name": "清爽", "description": "薄荷带来清凉感受"}
            ],
            "usage": [
                {"instruction": "湿发后取适量按摩头皮和头发", "frequency": "每周2-3次", "precautions": "避开眼部，如进入眼睛立即冲洗", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        }
    ]
    
    print(f"开始添加 {len(professional_recipes)} 个专业配方到数据库...")
    
    # 添加所有配方到数据库
    added_count = 0
    for recipe in professional_recipes:
        try:
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
                
                added_count += 1
                print(f"✓ 已添加配方: {recipe['name']}")
        except Exception as e:
            print(f"✗ 添加配方失败: {recipe['name']}, 错误: {e}")
    
    print(f"\n专业配方添加完成！成功添加了 {added_count} 个配方")
    
    # 显示最终统计信息
    products = db.search_products()
    categories = {}
    for product in products:
        category = product['category']
        categories[category] = categories.get(category, 0) + 1
    
    print("\n最终配方统计:")
    for category, count in categories.items():
        print(f"- {category}: {count} 个配方")
    
    print(f"\n总计: {len(products)} 个配方")

if __name__ == "__main__":
    add_professional_recipes()
