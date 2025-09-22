#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
特殊功效配方数据库 - 添加季节性、特殊功效配方
"""

from extract_pdf_data import CosmeticsDatabase

def add_specialized_recipes():
    """添加特殊功效配方"""
    db = CosmeticsDatabase()
    
    # 特殊功效配方
    specialized_recipes = [
        {
            "name": "夏日清爽防晒面霜",
            "category": "护肤品",
            "description": "夏日清爽防晒面霜，天然防晒清爽不油腻",
            "ingredients": [
                {"name": "氧化锌", "amount": "10g", "percentage": 10.0, "unit": "g", "phase": "防晒剂"},
                {"name": "乳木果油", "amount": "25g", "percentage": 25.0, "unit": "g", "phase": "油相"},
                {"name": "荷荷巴油", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "12g", "percentage": 12.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "35g", "percentage": 35.0, "unit": "g", "phase": "水相"},
                {"name": "薄荷精油", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "精油"}
            ],
            "steps": [
                {"step_number": 1, "description": "将乳木果油、荷荷巴油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70-80°C", "mixing_time": "10-15分钟", "notes": "持续搅拌形成乳液"},
                {"step_number": 4, "description": "冷却至40°C后加入氧化锌", "temperature": "40°C", "mixing_time": "5-10分钟", "notes": "充分混合防晒剂"},
                {"step_number": 5, "description": "最后加入薄荷精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "增加清爽感"}
            ],
            "benefits": [
                {"name": "天然防晒", "description": "氧化锌提供物理防晒"},
                {"name": "清爽不油腻", "description": "薄荷精油带来清爽感受"},
                {"name": "保湿", "description": "多重保湿成分保持肌肤水润"}
            ],
            "usage": [
                {"instruction": "外出前30分钟涂抹于面部和身体暴露部位", "frequency": "每2-3小时补涂", "precautions": "避免接触眼部，游泳后需重新涂抹", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "冬季深层滋养面霜",
            "category": "护肤品",
            "description": "冬季深层滋养面霜，强效保湿抵御干燥",
            "ingredients": [
                {"name": "乳木果油", "amount": "40g", "percentage": 40.0, "unit": "g", "phase": "油相"},
                {"name": "椰子油", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "水相"},
                {"name": "维生素E", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "抗氧化剂"},
                {"name": "薰衣草精油", "amount": "2滴", "percentage": 0.2, "unit": "滴", "phase": "精油"}
            ],
            "steps": [
                {"step_number": 1, "description": "将乳木果油、椰子油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70-80°C", "mixing_time": "10-15分钟", "notes": "持续搅拌形成乳液"},
                {"step_number": 4, "description": "冷却至40°C后加入维生素E", "temperature": "40°C", "mixing_time": "2-3分钟", "notes": "轻轻搅拌"},
                {"step_number": 5, "description": "最后加入薰衣草精油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "增加香味"}
            ],
            "benefits": [
                {"name": "深层滋养", "description": "多重油脂深层滋养肌肤"},
                {"name": "强效保湿", "description": "抵御冬季干燥"},
                {"name": "修复肌肤", "description": "修复干燥受损肌肤"}
            ],
            "usage": [
                {"instruction": "洁面后取适量轻柔按摩至吸收", "frequency": "早晚各一次", "precautions": "适合干燥肌肤使用", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "敏感肌肤舒缓面膜",
            "category": "面膜",
            "description": "敏感肌肤舒缓面膜，温和舒缓减少敏感",
            "ingredients": [
                {"name": "洋甘菊提取物", "amount": "15g", "percentage": 30.0, "unit": "g", "phase": "活性成分"},
                {"name": "燕麦粉", "amount": "20g", "percentage": 40.0, "unit": "g", "phase": "基质"},
                {"name": "纯净水", "amount": "12g", "percentage": 24.0, "unit": "g", "phase": "水相"},
                {"name": "蜂蜜", "amount": "3g", "percentage": 6.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将洋甘菊提取物和燕麦粉混合", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合粉末"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "最后加入蜂蜜", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "增加粘性和保湿效果"}
            ],
            "benefits": [
                {"name": "舒缓敏感", "description": "洋甘菊舒缓敏感肌肤"},
                {"name": "温和清洁", "description": "燕麦粉温和清洁"},
                {"name": "保湿", "description": "蜂蜜提供天然保湿"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，15分钟后洗净", "frequency": "每周2-3次", "precautions": "避开眼部，适合敏感肌肤", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "男士控油洁面凝胶",
            "category": "护肤品",
            "description": "男士控油洁面凝胶，深层清洁控油去角质",
            "ingredients": [
                {"name": "茶树精油", "amount": "8滴", "percentage": 0.8, "unit": "滴", "phase": "精油"},
                {"name": "薄荷精油", "amount": "5滴", "percentage": 0.5, "unit": "滴", "phase": "精油"},
                {"name": "芦荟凝胶", "amount": "70g", "percentage": 70.0, "unit": "g", "phase": "基质"},
                {"name": "透明质酸", "amount": "3g", "percentage": 3.0, "unit": "g", "phase": "保湿剂"},
                {"name": "纯净水", "amount": "25g", "percentage": 25.0, "unit": "g", "phase": "水相"},
                {"name": "防腐剂", "amount": "2滴", "percentage": 0.2, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将芦荟凝胶倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用纯天然芦荟凝胶"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入透明质酸并搅拌至溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解避免结块"},
                {"step_number": 4, "description": "加入茶树精油", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 5, "description": "加入薄荷精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保精油均匀分布"},
                {"step_number": 6, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "充分混合"}
            ],
            "benefits": [
                {"name": "深层清洁", "description": "芦荟凝胶温和清洁肌肤"},
                {"name": "控油", "description": "茶树和薄荷精油控油"},
                {"name": "清爽", "description": "薄荷带来清凉感受"}
            ],
            "usage": [
                {"instruction": "湿润面部后取适量轻柔按摩，然后用温水洗净", "frequency": "早晚各一次", "precautions": "避开眼部", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        },
        {
            "name": "孕妇安全保湿面霜",
            "category": "护肤品",
            "description": "孕妇安全保湿面霜，温和安全适合孕期使用",
            "ingredients": [
                {"name": "乳木果油", "amount": "35g", "percentage": 35.0, "unit": "g", "phase": "油相"},
                {"name": "荷荷巴油", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "25g", "percentage": 25.0, "unit": "g", "phase": "水相"},
                {"name": "维生素E", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将乳木果油、荷荷巴油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70-80°C", "mixing_time": "10-15分钟", "notes": "持续搅拌形成乳液"},
                {"step_number": 4, "description": "冷却至室温后加入维生素E", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "轻轻搅拌"}
            ],
            "benefits": [
                {"name": "安全温和", "description": "所有成分均对孕妇安全"},
                {"name": "深层保湿", "description": "多重保湿成分深层滋润"},
                {"name": "预防妊娠纹", "description": "保持肌肤弹性"}
            ],
            "usage": [
                {"instruction": "洁面后取适量轻柔按摩至吸收", "frequency": "早晚各一次", "precautions": "适合孕妇使用，避免使用精油", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "痘痘肌肤专用面膜",
            "category": "面膜",
            "description": "痘痘肌肤专用面膜，深层清洁消炎祛痘",
            "ingredients": [
                {"name": "茶树精油", "amount": "8滴", "percentage": 1.6, "unit": "滴", "phase": "精油"},
                {"name": "海藻粉", "amount": "30g", "percentage": 60.0, "unit": "g", "phase": "基质"},
                {"name": "纯净水", "amount": "15g", "percentage": 30.0, "unit": "g", "phase": "水相"},
                {"name": "蜂蜜", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将海藻粉倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "确保容器无菌"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "加入蜂蜜并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 4, "description": "最后加入茶树精油", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"}
            ],
            "benefits": [
                {"name": "深层清洁", "description": "海藻粉吸附毛孔污垢"},
                {"name": "消炎祛痘", "description": "茶树精油消炎祛痘"},
                {"name": "控油", "description": "调节皮脂分泌"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，避开眼部，15分钟后洗净", "frequency": "每周2-3次", "precautions": "敏感肌肤慎用，避免接触眼部", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "成熟肌肤抗衰老精华",
            "category": "护肤品",
            "description": "成熟肌肤抗衰老精华，多重抗衰老成分",
            "ingredients": [
                {"name": "视黄醇", "amount": "1g", "percentage": 2.0, "unit": "g", "phase": "活性成分"},
                {"name": "辅酶Q10", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "活性成分"},
                {"name": "纯净水", "amount": "35g", "percentage": 70.0, "unit": "g", "phase": "水相"},
                {"name": "透明质酸", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"},
                {"name": "甘油", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"},
                {"name": "维生素E", "amount": "2滴", "percentage": 0.4, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用蒸馏水或纯净水"},
                {"step_number": 2, "description": "加入透明质酸并搅拌至完全溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解避免结块"},
                {"step_number": 3, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"},
                {"step_number": 4, "description": "加入视黄醇", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "避免高温破坏活性成分"},
                {"step_number": 5, "description": "加入辅酶Q10", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "轻轻搅拌"},
                {"step_number": 6, "description": "最后加入维生素E", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "抗氧化保护"}
            ],
            "benefits": [
                {"name": "多重抗衰老", "description": "视黄醇和辅酶Q10多重抗衰老"},
                {"name": "减少细纹", "description": "改善肌肤质地，减少细纹"},
                {"name": "深层保湿", "description": "透明质酸深层保湿"}
            ],
            "usage": [
                {"instruction": "洁面后取2-3滴轻拍于面部至吸收", "frequency": "晚上使用", "precautions": "白天使用需防晒，孕妇禁用", "storage_conditions": "冷藏保存，开封后1个月内使用"}
            ]
        },
        {
            "name": "儿童温和洗发水",
            "category": "护发产品",
            "description": "儿童温和洗发水，温和不刺激适合儿童使用",
            "ingredients": [
                {"name": "椰子油起泡剂", "amount": "100ml", "percentage": 40.0, "unit": "ml", "phase": "表面活性剂"},
                {"name": "纯净水", "amount": "130ml", "percentage": 52.0, "unit": "ml", "phase": "水相"},
                {"name": "甘油", "amount": "15ml", "percentage": 6.0, "unit": "ml", "phase": "保湿剂"},
                {"name": "洋甘菊精油", "amount": "3滴", "percentage": 0.12, "unit": "滴", "phase": "精油"},
                {"name": "防腐剂", "amount": "3滴", "percentage": 0.12, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将椰子油起泡剂倒入容器", "temperature": "室温", "mixing_time": "", "notes": "使用干净容器"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入甘油并搅拌", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保充分溶解"},
                {"step_number": 4, "description": "加入洋甘菊精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合"},
                {"step_number": 5, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "充分混合"}
            ],
            "benefits": [
                {"name": "温和不刺激", "description": "适合儿童娇嫩肌肤"},
                {"name": "深层清洁", "description": "温和清洁头发"},
                {"name": "舒缓", "description": "洋甘菊精油舒缓头皮"}
            ],
            "usage": [
                {"instruction": "湿发后取适量轻柔按摩头发，然后用温水洗净", "frequency": "每周2-3次", "precautions": "避免接触眼部，如进入眼睛立即冲洗", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        },
        {
            "name": "运动后舒缓喷雾",
            "category": "精油",
            "description": "运动后舒缓喷雾，缓解肌肉疲劳清新提神",
            "ingredients": [
                {"name": "纯净水", "amount": "85ml", "percentage": 85.0, "unit": "ml", "phase": "水相"},
                {"name": "薄荷精油", "amount": "15滴", "percentage": 1.5, "unit": "滴", "phase": "精油"},
                {"name": "薰衣草精油", "amount": "10滴", "percentage": 1.0, "unit": "滴", "phase": "精油"},
                {"name": "尤加利精油", "amount": "5滴", "percentage": 0.5, "unit": "滴", "phase": "精油"},
                {"name": "甘油", "amount": "5ml", "percentage": 5.0, "unit": "ml", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入喷雾瓶", "temperature": "室温", "mixing_time": "", "notes": "使用干净的喷雾瓶"},
                {"step_number": 2, "description": "加入甘油并摇晃", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入薄荷精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃混合"},
                {"step_number": 4, "description": "加入薰衣草精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃混合"},
                {"step_number": 5, "description": "最后加入尤加利精油", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保精油完全分散"}
            ],
            "benefits": [
                {"name": "缓解疲劳", "description": "薄荷和薰衣草缓解肌肉疲劳"},
                {"name": "清新提神", "description": "尤加利精油清新提神"},
                {"name": "舒缓肌肉", "description": "多重精油舒缓肌肉"}
            ],
            "usage": [
                {"instruction": "运动后喷洒于身体或面部，避开眼部", "frequency": "根据需要", "precautions": "避免接触眼部，敏感肌肤慎用", "storage_conditions": "阴凉干燥处，使用前摇匀"}
            ]
        },
        {
            "name": "夜间修复睡眠面膜",
            "category": "面膜",
            "description": "夜间修复睡眠面膜，夜间修复深层滋养",
            "ingredients": [
                {"name": "薰衣草精油", "amount": "5滴", "percentage": 1.0, "unit": "滴", "phase": "精油"},
                {"name": "乳木果油", "amount": "30g", "percentage": 60.0, "unit": "g", "phase": "油相"},
                {"name": "荷荷巴油", "amount": "15g", "percentage": 30.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "乳化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将乳木果油、荷荷巴油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "冷却至40°C后加入薰衣草精油", "temperature": "40°C", "mixing_time": "2-3分钟", "notes": "轻轻搅拌"}
            ],
            "benefits": [
                {"name": "夜间修复", "description": "夜间深层修复肌肤"},
                {"name": "促进睡眠", "description": "薰衣草精油促进睡眠"},
                {"name": "深层滋养", "description": "多重油脂深层滋养"}
            ],
            "usage": [
                {"instruction": "睡前洁面后涂抹于面部，无需清洗，第二天早晨洗净", "frequency": "每晚使用", "precautions": "避免接触眼部", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        }
    ]
    
    print(f"开始添加 {len(specialized_recipes)} 个特殊功效配方到数据库...")
    
    # 添加所有配方到数据库
    added_count = 0
    for recipe in specialized_recipes:
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
    
    print(f"\n特殊功效配方添加完成！成功添加了 {added_count} 个配方")
    
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
    add_specialized_recipes()
