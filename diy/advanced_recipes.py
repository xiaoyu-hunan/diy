#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高级配方数据库 - 完善配方库，添加更多专业级配方
"""

from extract_pdf_data import CosmeticsDatabase

def add_advanced_recipes():
    """添加高级专业配方"""
    db = CosmeticsDatabase()
    
    # 高级专业配方
    advanced_recipes = [
        {
            "name": "辅酶Q10抗衰老面霜",
            "category": "护肤品",
            "description": "辅酶Q10抗衰老面霜，强效抗氧化延缓肌肤衰老",
            "ingredients": [
                {"name": "辅酶Q10", "amount": "2g", "percentage": 2.0, "unit": "g", "phase": "活性成分"},
                {"name": "乳木果油", "amount": "30g", "percentage": 30.0, "unit": "g", "phase": "油相"},
                {"name": "荷荷巴油", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "30g", "percentage": 30.0, "unit": "g", "phase": "水相"},
                {"name": "维生素E", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将乳木果油、荷荷巴油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70-80°C", "mixing_time": "10-15分钟", "notes": "持续搅拌形成乳液"},
                {"step_number": 4, "description": "冷却至40°C后加入辅酶Q10", "temperature": "40°C", "mixing_time": "3-5分钟", "notes": "避免高温破坏活性成分"},
                {"step_number": 5, "description": "最后加入维生素E", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "抗氧化保护"}
            ],
            "benefits": [
                {"name": "强效抗氧化", "description": "辅酶Q10具有强效抗氧化作用"},
                {"name": "延缓衰老", "description": "减少自由基损伤，延缓肌肤衰老"},
                {"name": "深层滋润", "description": "多重油脂深层滋润肌肤"}
            ],
            "usage": [
                {"instruction": "洁面后取适量轻柔按摩至吸收", "frequency": "早晚各一次", "precautions": "适合成熟肌肤使用", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "玻尿酸微针面膜",
            "category": "面膜",
            "description": "玻尿酸微针面膜，深层补水紧致肌肤",
            "ingredients": [
                {"name": "透明质酸", "amount": "15g", "percentage": 30.0, "unit": "g", "phase": "活性成分"},
                {"name": "海藻粉", "amount": "20g", "percentage": 40.0, "unit": "g", "phase": "基质"},
                {"name": "纯净水", "amount": "12g", "percentage": 24.0, "unit": "g", "phase": "水相"},
                {"name": "甘油", "amount": "3g", "percentage": 6.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将海藻粉倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "确保容器无菌"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "加入透明质酸并搅拌", "temperature": "室温", "mixing_time": "10-15分钟", "notes": "充分溶解"},
                {"step_number": 4, "description": "最后加入甘油", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"}
            ],
            "benefits": [
                {"name": "深层补水", "description": "透明质酸深层补水"},
                {"name": "紧致肌肤", "description": "海藻粉紧致肌肤"},
                {"name": "改善细纹", "description": "减少细纹和皱纹"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，25分钟后洗净", "frequency": "每周2-3次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "熊果苷美白淡斑精华",
            "category": "护肤品",
            "description": "熊果苷美白淡斑精华，抑制黑色素淡化色斑",
            "ingredients": [
                {"name": "熊果苷", "amount": "3g", "percentage": 6.0, "unit": "g", "phase": "活性成分"},
                {"name": "纯净水", "amount": "35g", "percentage": 70.0, "unit": "g", "phase": "水相"},
                {"name": "透明质酸", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"},
                {"name": "甘油", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"},
                {"name": "维生素C", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "活性成分"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用蒸馏水或纯净水"},
                {"step_number": 2, "description": "加入熊果苷并搅拌至溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解"},
                {"step_number": 3, "description": "加入透明质酸并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解避免结块"},
                {"step_number": 4, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"},
                {"step_number": 5, "description": "最后加入维生素C", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "轻轻搅拌避免氧化"}
            ],
            "benefits": [
                {"name": "美白淡斑", "description": "熊果苷抑制黑色素生成"},
                {"name": "提亮肤色", "description": "维生素C提亮肤色"},
                {"name": "抗氧化", "description": "强效抗氧化延缓衰老"}
            ],
            "usage": [
                {"instruction": "洁面后取2-3滴轻拍于面部，重点涂抹色斑部位", "frequency": "晚上使用", "precautions": "白天使用需防晒，敏感肌肤慎用", "storage_conditions": "冷藏保存，开封后1个月内使用"}
            ]
        },
        {
            "name": "咖啡因眼部精华",
            "category": "护肤品",
            "description": "咖啡因眼部精华，减少眼部浮肿淡化黑眼圈",
            "ingredients": [
                {"name": "咖啡因", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "活性成分"},
                {"name": "纯净水", "amount": "35g", "percentage": 70.0, "unit": "g", "phase": "水相"},
                {"name": "透明质酸", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"},
                {"name": "甘油", "amount": "6g", "percentage": 12.0, "unit": "g", "phase": "保湿剂"},
                {"name": "维生素K", "amount": "1g", "percentage": 2.0, "unit": "g", "phase": "活性成分"},
                {"name": "防腐剂", "amount": "2滴", "percentage": 0.4, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用蒸馏水或纯净水"},
                {"step_number": 2, "description": "加入咖啡因并搅拌至溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解"},
                {"step_number": 3, "description": "加入透明质酸并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解避免结块"},
                {"step_number": 4, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"},
                {"step_number": 5, "description": "加入维生素K", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "轻轻搅拌"},
                {"step_number": 6, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "充分混合"}
            ],
            "benefits": [
                {"name": "减少浮肿", "description": "咖啡因减少眼部浮肿"},
                {"name": "淡化黑眼圈", "description": "维生素K淡化黑眼圈"},
                {"name": "紧致眼周", "description": "改善眼周肌肤松弛"}
            ],
            "usage": [
                {"instruction": "洁面后取1-2滴轻拍于眼周，避免接触眼球", "frequency": "早晚各一次", "precautions": "避免接触眼球", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        },
        {
            "name": "水杨酸去角质面膜",
            "category": "面膜",
            "description": "水杨酸去角质面膜，深层清洁毛孔去除死皮",
            "ingredients": [
                {"name": "水杨酸", "amount": "3g", "percentage": 6.0, "unit": "g", "phase": "活性成分"},
                {"name": "海藻粉", "amount": "25g", "percentage": 50.0, "unit": "g", "phase": "基质"},
                {"name": "纯净水", "amount": "20g", "percentage": 40.0, "unit": "g", "phase": "水相"},
                {"name": "甘油", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将海藻粉倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "确保容器无菌"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "加入水杨酸并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解，注意浓度控制"},
                {"step_number": 4, "description": "最后加入甘油", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"}
            ],
            "benefits": [
                {"name": "深层清洁", "description": "水杨酸深层清洁毛孔"},
                {"name": "去角质", "description": "去除老化角质"},
                {"name": "控油", "description": "调节皮脂分泌"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，10-15分钟后洗净", "frequency": "每周1-2次", "precautions": "避开眼部，敏感肌肤慎用，使用后必须防晒", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "玫瑰果籽油抗衰老精华",
            "category": "护肤品",
            "description": "玫瑰果籽油抗衰老精华，富含维C和必需脂肪酸",
            "ingredients": [
                {"name": "玫瑰果籽油", "amount": "30ml", "percentage": 60.0, "unit": "ml", "phase": "油相"},
                {"name": "荷荷巴油", "amount": "15ml", "percentage": 30.0, "unit": "ml", "phase": "油相"},
                {"name": "维生素E", "amount": "5ml", "percentage": 10.0, "unit": "ml", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将玫瑰果籽油倒入深色玻璃瓶", "temperature": "室温", "mixing_time": "", "notes": "使用深色玻璃瓶避免光照"},
                {"step_number": 2, "description": "加入荷荷巴油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "轻轻摇晃混合"},
                {"step_number": 3, "description": "最后加入维生素E", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃使成分均匀分布"}
            ],
            "benefits": [
                {"name": "抗衰老", "description": "玫瑰果籽油富含维C和必需脂肪酸"},
                {"name": "修复肌肤", "description": "促进肌肤修复和再生"},
                {"name": "改善疤痕", "description": "淡化疤痕和妊娠纹"}
            ],
            "usage": [
                {"instruction": "洁面后取2-3滴轻拍于面部至吸收", "frequency": "早晚各一次", "precautions": "适合所有肌肤类型", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "绿茶抗氧化爽肤水",
            "category": "护肤品",
            "description": "绿茶抗氧化爽肤水，强效抗氧化舒缓肌肤",
            "ingredients": [
                {"name": "绿茶提取物", "amount": "10g", "percentage": 20.0, "unit": "g", "phase": "活性成分"},
                {"name": "纯净水", "amount": "35g", "percentage": 70.0, "unit": "g", "phase": "水相"},
                {"name": "甘油", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用蒸馏水或纯净水"},
                {"step_number": 2, "description": "加入绿茶提取物并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解"},
                {"step_number": 3, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"}
            ],
            "benefits": [
                {"name": "强效抗氧化", "description": "绿茶多酚具有强效抗氧化作用"},
                {"name": "舒缓肌肤", "description": "缓解肌肤不适"},
                {"name": "抗炎", "description": "减少肌肤炎症反应"}
            ],
            "usage": [
                {"instruction": "洁面后轻拍于面部，可重复使用", "frequency": "早晚各一次", "precautions": "避免接触眼部", "storage_conditions": "阴凉干燥处，开封后2个月内使用"}
            ]
        },
        {
            "name": "阿甘油深层滋养面霜",
            "category": "护肤品",
            "description": "阿甘油深层滋养面霜，富含维E和必需脂肪酸",
            "ingredients": [
                {"name": "阿甘油", "amount": "35g", "percentage": 35.0, "unit": "g", "phase": "油相"},
                {"name": "乳木果油", "amount": "25g", "percentage": 25.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "乳化剂"},
                {"name": "纯净水", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "水相"},
                {"name": "维生素E", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "抗氧化剂"},
                {"name": "薰衣草精油", "amount": "2滴", "percentage": 0.2, "unit": "滴", "phase": "精油"}
            ],
            "steps": [
                {"step_number": 1, "description": "将阿甘油、乳木果油和蜂蜡隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "70-80°C", "mixing_time": "3-5分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "70-80°C", "mixing_time": "10-15分钟", "notes": "持续搅拌形成乳液"},
                {"step_number": 4, "description": "冷却至40°C后加入维生素E", "temperature": "40°C", "mixing_time": "2-3分钟", "notes": "轻轻搅拌"},
                {"step_number": 5, "description": "最后加入薰衣草精油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "增加香味"}
            ],
            "benefits": [
                {"name": "深层滋养", "description": "阿甘油富含维E和必需脂肪酸"},
                {"name": "修复肌肤", "description": "促进肌肤修复和愈合"},
                {"name": "舒缓放松", "description": "薰衣草精油舒缓身心"}
            ],
            "usage": [
                {"instruction": "洁面后取适量轻柔按摩至吸收", "frequency": "早晚各一次", "precautions": "适合所有肌肤类型", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "珍珠粉美白面膜",
            "category": "面膜",
            "description": "珍珠粉美白面膜，天然美白提亮肤色",
            "ingredients": [
                {"name": "珍珠粉", "amount": "20g", "percentage": 40.0, "unit": "g", "phase": "活性成分"},
                {"name": "海藻粉", "amount": "20g", "percentage": 40.0, "unit": "g", "phase": "基质"},
                {"name": "纯净水", "amount": "8g", "percentage": 16.0, "unit": "g", "phase": "水相"},
                {"name": "蜂蜜", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将珍珠粉和海藻粉混合", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合粉末"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "最后加入蜂蜜", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "增加粘性和保湿效果"}
            ],
            "benefits": [
                {"name": "天然美白", "description": "珍珠粉具有天然美白功效"},
                {"name": "提亮肤色", "description": "改善肌肤暗沉"},
                {"name": "深层滋养", "description": "海藻粉提供丰富营养"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，20分钟后洗净", "frequency": "每周2-3次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "茶树精油控油洁面凝胶",
            "category": "护肤品",
            "description": "茶树精油控油洁面凝胶，深层清洁控油祛痘",
            "ingredients": [
                {"name": "茶树精油", "amount": "10滴", "percentage": 1.0, "unit": "滴", "phase": "精油"},
                {"name": "芦荟凝胶", "amount": "60g", "percentage": 60.0, "unit": "g", "phase": "基质"},
                {"name": "透明质酸", "amount": "5g", "percentage": 5.0, "unit": "g", "phase": "保湿剂"},
                {"name": "甘油", "amount": "10g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"},
                {"name": "纯净水", "amount": "25g", "percentage": 25.0, "unit": "g", "phase": "水相"},
                {"name": "防腐剂", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将芦荟凝胶倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用纯天然芦荟凝胶"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入透明质酸并搅拌至溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解避免结块"},
                {"step_number": 4, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"},
                {"step_number": 5, "description": "加入茶树精油", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 6, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "充分混合"}
            ],
            "benefits": [
                {"name": "深层清洁", "description": "芦荟凝胶温和清洁肌肤"},
                {"name": "控油祛痘", "description": "茶树精油控油祛痘"},
                {"name": "抗菌消炎", "description": "茶树精油具有抗菌消炎作用"}
            ],
            "usage": [
                {"instruction": "湿润面部后取适量轻柔按摩，然后用温水洗净", "frequency": "早晚各一次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        }
    ]
    
    print(f"开始添加 {len(advanced_recipes)} 个高级配方到数据库...")
    
    # 添加所有配方到数据库
    added_count = 0
    for recipe in advanced_recipes:
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
    
    print(f"\n高级配方添加完成！成功添加了 {added_count} 个配方")
    
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
    add_advanced_recipes()
