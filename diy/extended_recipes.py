#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
扩展配方数据库 - 基于43个DIY护肤品配方等PDF文件
"""

from extract_pdf_data import CosmeticsDatabase

def add_extended_recipes():
    """添加更多扩展配方"""
    db = CosmeticsDatabase()
    
    # 基于"43个DIY护肤品配方.pdf"的更多配方
    extended_skincare = [
        {
            "name": "金盏花舒缓面霜",
            "category": "护肤品",
            "description": "金盏花舒缓面霜，适合敏感肌肤的温和护理",
            "ingredients": [
                {"name": "金盏花浸泡油", "amount": "30g", "percentage": 30.0, "unit": "g", "phase": "油相"},
                {"name": "乳木果油", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "30g", "percentage": 30.0, "unit": "g", "phase": "水相"},
                {"name": "维生素E", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将金盏花浸泡油、乳木果油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "确保完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "持续搅拌形成乳液"},
                {"step_number": 4, "description": "冷却至40°C后加入维生素E", "temperature": "40°C", "mixing_time": "2-3分钟", "notes": "轻轻搅拌"}
            ],
            "benefits": [
                {"name": "舒缓敏感", "description": "金盏花具有舒缓敏感肌肤的功效"},
                {"name": "深层保湿", "description": "多重保湿成分深层滋润"},
                {"name": "修复肌肤", "description": "促进肌肤修复和愈合"}
            ],
            "usage": [
                {"instruction": "洁面后取适量轻柔按摩至吸收", "frequency": "早晚各一次", "precautions": "适合敏感肌肤使用", "storage_conditions": "阴凉干燥处，开封后6个月内使用"}
            ]
        },
        {
            "name": "珍珠粉美白面膜",
            "category": "面膜",
            "description": "天然珍珠粉美白面膜，提亮肤色淡化色斑",
            "ingredients": [
                {"name": "珍珠粉", "amount": "20g", "percentage": 40.0, "unit": "g", "phase": "活性成分"},
                {"name": "蜂蜜", "amount": "20g", "percentage": 40.0, "unit": "g", "phase": "基质"},
                {"name": "牛奶", "amount": "10g", "percentage": 20.0, "unit": "g", "phase": "水相"}
            ],
            "steps": [
                {"step_number": 1, "description": "将珍珠粉倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用细珍珠粉效果更好"},
                {"step_number": 2, "description": "加入蜂蜜并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "加入牛奶并充分混合", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保充分混合"}
            ],
            "benefits": [
                {"name": "美白提亮", "description": "珍珠粉具有美白提亮功效"},
                {"name": "淡化色斑", "description": "减少黑色素沉淀"},
                {"name": "滋润保湿", "description": "蜂蜜和牛奶双重保湿"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，15-20分钟后洗净", "frequency": "每周2-3次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "黄瓜补水爽肤水",
            "category": "护肤品",
            "description": "天然黄瓜爽肤水，清爽补水舒缓肌肤",
            "ingredients": [
                {"name": "黄瓜汁", "amount": "60ml", "percentage": 75.0, "unit": "ml", "phase": "水相"},
                {"name": "纯净水", "amount": "15ml", "percentage": 18.75, "unit": "ml", "phase": "水相"},
                {"name": "甘油", "amount": "5ml", "percentage": 6.25, "unit": "ml", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将黄瓜榨汁并过滤", "temperature": "室温", "mixing_time": "", "notes": "去除黄瓜渣滓"},
                {"step_number": 2, "description": "加入纯净水稀释", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入甘油并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"}
            ],
            "benefits": [
                {"name": "清爽补水", "description": "黄瓜汁提供天然补水"},
                {"name": "舒缓肌肤", "description": "缓解肌肤不适"},
                {"name": "收缩毛孔", "description": "紧致肌肤，收缩毛孔"}
            ],
            "usage": [
                {"instruction": "洁面后轻拍于面部，可重复使用", "frequency": "早晚各一次", "precautions": "避免接触眼部", "storage_conditions": "冷藏保存，3天内使用完"}
            ]
        },
        {
            "name": "杏仁油润肤乳",
            "category": "护肤品",
            "description": "杏仁油润肤乳，温和滋润全身肌肤",
            "ingredients": [
                {"name": "甜杏仁油", "amount": "40g", "percentage": 40.0, "unit": "g", "phase": "油相"},
                {"name": "椰子油", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "10g", "percentage": 10.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "25g", "percentage": 25.0, "unit": "g", "phase": "水相"},
                {"name": "薰衣草精油", "amount": "5滴", "percentage": 0.5, "unit": "滴", "phase": "精油"}
            ],
            "steps": [
                {"step_number": 1, "description": "将甜杏仁油、椰子油和蜂蜡隔水加热", "temperature": "70°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70°C", "mixing_time": "10-15分钟", "notes": "持续搅拌形成乳液"},
                {"step_number": 4, "description": "冷却至室温后加入薰衣草精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "轻轻搅拌"}
            ],
            "benefits": [
                {"name": "深层滋润", "description": "杏仁油深层滋润肌肤"},
                {"name": "温和不刺激", "description": "适合敏感肌肤使用"},
                {"name": "舒缓放松", "description": "薰衣草精油舒缓身心"}
            ],
            "usage": [
                {"instruction": "沐浴后取适量涂抹全身", "frequency": "每日一次", "precautions": "适合全身使用", "storage_conditions": "阴凉干燥处，开封后6个月内使用"}
            ]
        },
        {
            "name": "草莓维C亮白面膜",
            "category": "面膜",
            "description": "草莓维C亮白面膜，天然维C提亮肤色",
            "ingredients": [
                {"name": "新鲜草莓", "amount": "30g", "percentage": 60.0, "unit": "g", "phase": "活性成分"},
                {"name": "蜂蜜", "amount": "15g", "percentage": 30.0, "unit": "g", "phase": "基质"},
                {"name": "酸奶", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将草莓捣碎成泥状", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "去除草莓籽"},
                {"step_number": 2, "description": "加入蜂蜜并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入酸奶并调匀", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "调至适合涂抹的稠度"}
            ],
            "benefits": [
                {"name": "维C亮白", "description": "草莓富含天然维C"},
                {"name": "提亮肤色", "description": "改善肌肤暗沉"},
                {"name": "滋润保湿", "description": "蜂蜜和酸奶双重保湿"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，15分钟后洗净", "frequency": "每周1-2次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "薄荷清凉洗发水",
            "category": "护发产品",
            "description": "薄荷清凉洗发水，清爽控油去屑",
            "ingredients": [
                {"name": "椰子油起泡剂", "amount": "120ml", "percentage": 48.0, "unit": "ml", "phase": "表面活性剂"},
                {"name": "纯净水", "amount": "100ml", "percentage": 40.0, "unit": "ml", "phase": "水相"},
                {"name": "薄荷精油", "amount": "15滴", "percentage": 0.6, "unit": "滴", "phase": "精油"},
                {"name": "茶树精油", "amount": "8滴", "percentage": 0.32, "unit": "滴", "phase": "精油"},
                {"name": "甘油", "amount": "15ml", "percentage": 6.0, "unit": "ml", "phase": "保湿剂"},
                {"name": "防腐剂", "amount": "4滴", "percentage": 0.16, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将椰子油起泡剂倒入容器", "temperature": "室温", "mixing_time": "", "notes": "使用干净容器"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入甘油并搅拌", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保充分溶解"},
                {"step_number": 4, "description": "加入薄荷精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合"},
                {"step_number": 5, "description": "加入茶树精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保精油均匀分布"},
                {"step_number": 6, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "充分混合"}
            ],
            "benefits": [
                {"name": "清爽控油", "description": "薄荷成分清爽控油"},
                {"name": "去屑抗菌", "description": "茶树精油去屑抗菌"},
                {"name": "深层清洁", "description": "温和清洁头皮和头发"}
            ],
            "usage": [
                {"instruction": "湿发后取适量按摩头皮和头发", "frequency": "每周2-3次", "precautions": "避开眼部，如进入眼睛立即冲洗", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        },
        {
            "name": "玫瑰花瓣护发素",
            "category": "护发产品",
            "description": "玫瑰花瓣护发素，滋养修复受损发质",
            "ingredients": [
                {"name": "玫瑰花瓣浸泡油", "amount": "50ml", "percentage": 50.0, "unit": "ml", "phase": "油相"},
                {"name": "乳木果油", "amount": "20ml", "percentage": 20.0, "unit": "ml", "phase": "油相"},
                {"name": "蜂蜡", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "10ml", "percentage": 10.0, "unit": "ml", "phase": "水相"},
                {"name": "玫瑰精油", "amount": "5滴", "percentage": 0.5, "unit": "滴", "phase": "精油"}
            ],
            "steps": [
                {"step_number": 1, "description": "将玫瑰花瓣浸泡油和乳木果油混合", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合基础油"},
                {"step_number": 2, "description": "加入蜂蜡并隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 3, "description": "加入纯净水", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 4, "description": "冷却至40°C后加入玫瑰精油", "temperature": "40°C", "mixing_time": "2-3分钟", "notes": "轻轻搅拌"}
            ],
            "benefits": [
                {"name": "滋养修复", "description": "玫瑰精华滋养修复受损发质"},
                {"name": "深层滋润", "description": "多重油脂深层滋润"},
                {"name": "改善发质", "description": "让头发更加柔顺有光泽"}
            ],
            "usage": [
                {"instruction": "洗发后涂抹于发梢，停留5-10分钟后洗净", "frequency": "每周1-2次", "precautions": "避免接触头皮", "storage_conditions": "阴凉干燥处，开封后6个月内使用"}
            ]
        },
        {
            "name": "薰衣草安神枕边喷雾",
            "category": "精油",
            "description": "薰衣草安神枕边喷雾，促进睡眠缓解压力",
            "ingredients": [
                {"name": "纯净水", "amount": "80ml", "percentage": 80.0, "unit": "ml", "phase": "水相"},
                {"name": "薰衣草精油", "amount": "20滴", "percentage": 2.0, "unit": "滴", "phase": "精油"},
                {"name": "洋甘菊精油", "amount": "10滴", "percentage": 1.0, "unit": "滴", "phase": "精油"},
                {"name": "乳化剂", "amount": "2ml", "percentage": 2.0, "unit": "ml", "phase": "乳化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入喷雾瓶", "temperature": "室温", "mixing_time": "", "notes": "使用干净的喷雾瓶"},
                {"step_number": 2, "description": "加入乳化剂并摇晃", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合乳化剂"},
                {"step_number": 3, "description": "加入薰衣草精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃混合"},
                {"step_number": 4, "description": "最后加入洋甘菊精油", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保精油完全分散"}
            ],
            "benefits": [
                {"name": "促进睡眠", "description": "薰衣草精油促进深度睡眠"},
                {"name": "缓解压力", "description": "放松身心，缓解紧张情绪"},
                {"name": "净化空气", "description": "清新空气，改善睡眠环境"}
            ],
            "usage": [
                {"instruction": "睡前喷洒在枕头和床单上", "frequency": "每晚使用", "precautions": "避免接触眼部", "storage_conditions": "阴凉干燥处，使用前摇匀"}
            ]
        },
        {
            "name": "柠檬蜂蜜去角质霜",
            "category": "护肤品",
            "description": "柠檬蜂蜜去角质霜，温和去除死皮提亮肤色",
            "ingredients": [
                {"name": "细海盐", "amount": "30g", "percentage": 50.0, "unit": "g", "phase": "磨砂剂"},
                {"name": "蜂蜜", "amount": "20g", "percentage": 33.3, "unit": "g", "phase": "保湿剂"},
                {"name": "柠檬汁", "amount": "8ml", "percentage": 13.3, "unit": "ml", "phase": "活性成分"},
                {"name": "橄榄油", "amount": "2ml", "percentage": 3.3, "unit": "ml", "phase": "油相"}
            ],
            "steps": [
                {"step_number": 1, "description": "将细海盐倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用细海盐避免刺激"},
                {"step_number": 2, "description": "加入蜂蜜并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "加入柠檬汁", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合"},
                {"step_number": 4, "description": "最后加入橄榄油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "增加润滑性"}
            ],
            "benefits": [
                {"name": "温和去角质", "description": "海盐温和去除死皮"},
                {"name": "提亮肤色", "description": "柠檬汁提亮肤色"},
                {"name": "滋润保湿", "description": "蜂蜜和橄榄油深层滋润"}
            ],
            "usage": [
                {"instruction": "湿润肌肤后轻柔按摩2-3分钟，然后用温水洗净", "frequency": "每周1-2次", "precautions": "敏感肌肤慎用，避免用力过猛", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "乳木果油护手霜",
            "category": "护肤品",
            "description": "乳木果油护手霜，深层滋润手部肌肤",
            "ingredients": [
                {"name": "乳木果油", "amount": "40g", "percentage": 40.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "乳化剂"},
                {"name": "椰子油", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "油相"},
                {"name": "纯净水", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "水相"},
                {"name": "维生素E", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将乳木果油、椰子油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70-80°C", "mixing_time": "10-15分钟", "notes": "持续搅拌形成霜状"},
                {"step_number": 4, "description": "冷却至40°C后加入维生素E", "temperature": "40°C", "mixing_time": "2-3分钟", "notes": "轻轻搅拌"}
            ],
            "benefits": [
                {"name": "深层滋润", "description": "乳木果油深层滋润手部肌肤"},
                {"name": "修复干燥", "description": "修复干燥粗糙的手部肌肤"},
                {"name": "长效保湿", "description": "形成保护膜，长效保湿"}
            ],
            "usage": [
                {"instruction": "洗手后取适量涂抹双手，轻柔按摩至吸收", "frequency": "每日多次", "precautions": "适合手部使用", "storage_conditions": "阴凉干燥处，开封后6个月内使用"}
            ]
        }
    ]
    
    print(f"开始添加 {len(extended_skincare)} 个扩展配方到数据库...")
    
    # 添加所有配方到数据库
    for recipe in extended_skincare:
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
            
            print(f"✓ 已添加配方: {recipe['name']}")
    
    print(f"\n扩展配方添加完成！新增了 {len(extended_skincare)} 个配方")
    
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
    add_extended_recipes()
