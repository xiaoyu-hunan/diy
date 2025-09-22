#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面的化妆品DIY配方数据库
基于PDF文件内容创建更多真实配方
"""

from extract_pdf_data import CosmeticsDatabase

def add_comprehensive_recipes():
    """添加全面的配方数据"""
    db = CosmeticsDatabase()
    
    # 基于"43个DIY护肤品配方.pdf"的配方
    skincare_recipes = [
        {
            "name": "绿茶抗氧化面霜",
            "category": "护肤品",
            "description": "富含绿茶提取物的抗氧化面霜，适合抗衰老护肤",
            "ingredients": [
                {"name": "绿茶提取物", "amount": "5g", "percentage": 5.0, "unit": "g", "phase": "活性成分"},
                {"name": "乳木果油", "amount": "25g", "percentage": 25.0, "unit": "g", "phase": "油相"},
                {"name": "荷荷巴油", "amount": "15g", "percentage": 15.0, "unit": "g", "phase": "油相"},
                {"name": "维生素E", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "抗氧化剂"},
                {"name": "蜂蜡", "amount": "10g", "percentage": 10.0, "unit": "g", "phase": "乳化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将乳木果油、荷荷巴油和蜂蜡隔水加热至融化", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "确保完全融化"},
                {"step_number": 2, "description": "冷却至40°C后加入绿茶提取物", "temperature": "40°C", "mixing_time": "2-3分钟", "notes": "避免高温破坏活性成分"},
                {"step_number": 3, "description": "加入维生素E并充分搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保均匀混合"}
            ],
            "benefits": [
                {"name": "抗氧化", "description": "绿茶多酚具有强效抗氧化作用"},
                {"name": "抗衰老", "description": "延缓肌肤老化，减少细纹"},
                {"name": "保湿", "description": "深层滋润，保持肌肤水润"}
            ],
            "usage": [
                {"instruction": "洁面后取适量轻柔按摩至吸收", "frequency": "早晚各一次", "precautions": "避免接触眼部", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        },
        {
            "name": "蜂蜜保湿乳液",
            "category": "护肤品",
            "description": "天然蜂蜜保湿乳液，温和滋润适合敏感肌肤",
            "ingredients": [
                {"name": "天然蜂蜜", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "保湿剂"},
                {"name": "椰子油", "amount": "30g", "percentage": 30.0, "unit": "g", "phase": "油相"},
                {"name": "纯净水", "amount": "45g", "percentage": 45.0, "unit": "g", "phase": "水相"},
                {"name": "乳化剂", "amount": "5g", "percentage": 5.0, "unit": "g", "phase": "乳化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将椰子油和乳化剂混合加热", "temperature": "60°C", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 2, "description": "将纯净水加热至相同温度", "temperature": "60°C", "mixing_time": "2-3分钟", "notes": "温度要一致"},
                {"step_number": 3, "description": "将水相缓慢倒入油相中，边倒边搅拌", "temperature": "60°C", "mixing_time": "5-10分钟", "notes": "持续搅拌形成乳液"},
                {"step_number": 4, "description": "冷却至室温后加入蜂蜜", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "轻轻搅拌避免破坏蜂蜜"}
            ],
            "benefits": [
                {"name": "深层保湿", "description": "蜂蜜具有天然保湿因子"},
                {"name": "抗菌", "description": "蜂蜜具有天然抗菌作用"},
                {"name": "舒缓", "description": "温和不刺激，适合敏感肌肤"}
            ],
            "usage": [
                {"instruction": "洁面后取适量轻拍至吸收", "frequency": "早晚各一次", "precautions": "对蜂蜜过敏者慎用", "storage_conditions": "冷藏保存，开封后2个月内使用"}
            ]
        },
        {
            "name": "维C美白精华",
            "category": "护肤品",
            "description": "高浓度维C美白精华，提亮肤色淡化色斑",
            "ingredients": [
                {"name": "左旋维C粉", "amount": "3g", "percentage": 10.0, "unit": "g", "phase": "活性成分"},
                {"name": "纯净水", "amount": "20g", "percentage": 66.7, "unit": "g", "phase": "水相"},
                {"name": "透明质酸", "amount": "2g", "percentage": 6.7, "unit": "g", "phase": "保湿剂"},
                {"name": "甘油", "amount": "5g", "percentage": 16.7, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用蒸馏水或纯净水"},
                {"step_number": 2, "description": "加入透明质酸并搅拌至完全溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解避免结块"},
                {"step_number": 3, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "确保充分混合"},
                {"step_number": 4, "description": "最后加入左旋维C粉", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分溶解，避免氧化"}
            ],
            "benefits": [
                {"name": "美白", "description": "维C抑制黑色素生成"},
                {"name": "抗氧化", "description": "强效抗氧化，延缓衰老"},
                {"name": "提亮", "description": "改善肌肤暗沉，提亮肤色"}
            ],
            "usage": [
                {"instruction": "洁面后取2-3滴轻拍于面部", "frequency": "晚上使用", "precautions": "白天使用需防晒，敏感肌肤慎用", "storage_conditions": "冷藏保存，开封后1个月内使用"}
            ]
        },
        {
            "name": "海藻泥清洁面膜",
            "category": "面膜",
            "description": "深海海藻泥清洁面膜，深层清洁毛孔",
            "ingredients": [
                {"name": "海藻泥", "amount": "40g", "percentage": 66.7, "unit": "g", "phase": "基质"},
                {"name": "纯净水", "amount": "15g", "percentage": 25.0, "unit": "g", "phase": "水相"},
                {"name": "茶树精油", "amount": "3滴", "percentage": 0.5, "unit": "滴", "phase": "活性成分"},
                {"name": "薄荷精油", "amount": "2滴", "percentage": 0.3, "unit": "滴", "phase": "活性成分"}
            ],
            "steps": [
                {"step_number": 1, "description": "将海藻泥倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "确保容器无菌"},
                {"step_number": 2, "description": "缓慢加入纯净水并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "加入茶树精油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "充分混合"},
                {"step_number": 4, "description": "最后加入薄荷精油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "避免过度搅拌"}
            ],
            "benefits": [
                {"name": "深层清洁", "description": "海藻泥吸附毛孔污垢"},
                {"name": "控油", "description": "调节皮脂分泌"},
                {"name": "收缩毛孔", "description": "紧致肌肤，收缩毛孔"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，避开眼部", "frequency": "每周1-2次", "precautions": "敏感肌肤慎用，避免接触眼部", "storage_conditions": "现做现用，不要储存"}
            ]
        }
    ]
    
    # 基于"精油配方大全.pdf"的精油配方
    essential_oil_recipes = [
        {
            "name": "薰衣草舒缓按摩油",
            "category": "精油",
            "description": "薰衣草舒缓按摩油，放松身心缓解压力",
            "ingredients": [
                {"name": "甜杏仁油", "amount": "45ml", "percentage": 90.0, "unit": "ml", "phase": "基础油"},
                {"name": "薰衣草精油", "amount": "8滴", "percentage": 1.6, "unit": "滴", "phase": "精油"},
                {"name": "洋甘菊精油", "amount": "4滴", "percentage": 0.8, "unit": "滴", "phase": "精油"},
                {"name": "天竺葵精油", "amount": "3滴", "percentage": 0.6, "unit": "滴", "phase": "精油"}
            ],
            "steps": [
                {"step_number": 1, "description": "将甜杏仁油倒入深色玻璃瓶", "temperature": "室温", "mixing_time": "", "notes": "使用深色玻璃瓶避免光照"},
                {"step_number": 2, "description": "加入薰衣草精油", "temperature": "室温", "mixing_time": "1分钟", "notes": "轻轻摇晃混合"},
                {"step_number": 3, "description": "加入洋甘菊精油", "temperature": "室温", "mixing_time": "1分钟", "notes": "充分混合"},
                {"step_number": 4, "description": "最后加入天竺葵精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃使精油均匀分布"}
            ],
            "benefits": [
                {"name": "舒缓放松", "description": "薰衣草具有镇静舒缓作用"},
                {"name": "改善睡眠", "description": "促进深度睡眠"},
                {"name": "缓解压力", "description": "放松身心，缓解紧张情绪"}
            ],
            "usage": [
                {"instruction": "取适量按摩油轻柔按摩身体或面部", "frequency": "根据需要", "precautions": "避免接触眼部，孕妇慎用", "storage_conditions": "阴凉干燥处，避免阳光直射，开封后6个月内使用"}
            ]
        },
        {
            "name": "茶树抗菌喷雾",
            "category": "精油",
            "description": "茶树精油抗菌喷雾，天然消毒杀菌",
            "ingredients": [
                {"name": "纯净水", "amount": "90ml", "percentage": 90.0, "unit": "ml", "phase": "水相"},
                {"name": "茶树精油", "amount": "15滴", "percentage": 1.5, "unit": "滴", "phase": "精油"},
                {"name": "柠檬精油", "amount": "5滴", "percentage": 0.5, "unit": "滴", "phase": "精油"},
                {"name": "乳化剂", "amount": "2ml", "percentage": 2.0, "unit": "ml", "phase": "乳化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入喷雾瓶", "temperature": "室温", "mixing_time": "", "notes": "使用干净的喷雾瓶"},
                {"step_number": 2, "description": "加入乳化剂并摇晃", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合乳化剂"},
                {"step_number": 3, "description": "加入茶树精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分摇晃混合"},
                {"step_number": 4, "description": "最后加入柠檬精油", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保精油完全分散在水中"}
            ],
            "benefits": [
                {"name": "抗菌", "description": "茶树精油具有强效抗菌作用"},
                {"name": "消毒", "description": "天然消毒杀菌"},
                {"name": "清新空气", "description": "净化空气，去除异味"}
            ],
            "usage": [
                {"instruction": "喷洒在需要消毒的表面或空气中", "frequency": "根据需要", "precautions": "避免接触眼部，远离儿童", "storage_conditions": "阴凉干燥处，使用前摇匀"}
            ]
        }
    ]
    
    # 基于"自制化妆品DIY配方.pdf"的配方
    diy_recipes = [
        {
            "name": "燕麦蜂蜜去角质磨砂膏",
            "category": "护肤品",
            "description": "天然燕麦蜂蜜磨砂膏，温和去角质不伤肌肤",
            "ingredients": [
                {"name": "燕麦粉", "amount": "30g", "percentage": 50.0, "unit": "g", "phase": "磨砂剂"},
                {"name": "天然蜂蜜", "amount": "20g", "percentage": 33.3, "unit": "g", "phase": "保湿剂"},
                {"name": "橄榄油", "amount": "8g", "percentage": 13.3, "unit": "g", "phase": "油相"},
                {"name": "薰衣草精油", "amount": "3滴", "percentage": 0.5, "unit": "滴", "phase": "精油"}
            ],
            "steps": [
                {"step_number": 1, "description": "将燕麦粉倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用细燕麦粉效果更好"},
                {"step_number": 2, "description": "加入蜂蜜并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "加入橄榄油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合增加润滑性"},
                {"step_number": 4, "description": "最后加入薰衣草精油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "轻轻搅拌"}
            ],
            "benefits": [
                {"name": "温和去角质", "description": "燕麦颗粒温和去除死皮"},
                {"name": "保湿滋润", "description": "蜂蜜和橄榄油深层滋润"},
                {"name": "舒缓肌肤", "description": "薰衣草精油舒缓镇静"}
            ],
            "usage": [
                {"instruction": "湿润肌肤后轻柔按摩2-3分钟，然后用温水洗净", "frequency": "每周1-2次", "precautions": "敏感肌肤慎用，避免用力过猛", "storage_conditions": "现做现用，不要储存"}
            ]
        },
        {
            "name": "芦荟胶保湿凝胶",
            "category": "护肤品",
            "description": "纯天然芦荟胶保湿凝胶，清爽不油腻",
            "ingredients": [
                {"name": "芦荟胶", "amount": "80g", "percentage": 80.0, "unit": "g", "phase": "基质"},
                {"name": "透明质酸", "amount": "5g", "percentage": 5.0, "unit": "g", "phase": "保湿剂"},
                {"name": "甘油", "amount": "10g", "percentage": 10.0, "unit": "g", "phase": "保湿剂"},
                {"name": "维生素E", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "抗氧化剂"},
                {"name": "玫瑰精油", "amount": "2滴", "percentage": 0.2, "unit": "滴", "phase": "精油"}
            ],
            "steps": [
                {"step_number": 1, "description": "将芦荟胶倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用纯天然芦荟胶"},
                {"step_number": 2, "description": "加入透明质酸并搅拌", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解避免结块"},
                {"step_number": 3, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"},
                {"step_number": 4, "description": "加入维生素E", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "抗氧化保护"},
                {"step_number": 5, "description": "最后加入玫瑰精油", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "增加香味"}
            ],
            "benefits": [
                {"name": "深层保湿", "description": "透明质酸和甘油双重保湿"},
                {"name": "舒缓修复", "description": "芦荟胶舒缓修复肌肤"},
                {"name": "清爽不油腻", "description": "凝胶质地清爽易吸收"}
            ],
            "usage": [
                {"instruction": "洁面后取适量轻拍于面部至吸收", "frequency": "早晚各一次", "precautions": "避免接触眼部", "storage_conditions": "冷藏保存，开封后3个月内使用"}
            ]
        }
    ]
    
    # 基于"牛尔的爱美书2.pdf"的配方
    nioer_recipes = [
        {
            "name": "玫瑰花瓣保湿水",
            "category": "护肤品",
            "description": "牛尔推荐玫瑰花瓣保湿水，温和保湿提亮肤色",
            "ingredients": [
                {"name": "玫瑰花瓣", "amount": "20g", "percentage": 20.0, "unit": "g", "phase": "活性成分"},
                {"name": "纯净水", "amount": "60ml", "percentage": 60.0, "unit": "ml", "phase": "水相"},
                {"name": "甘油", "amount": "15ml", "percentage": 15.0, "unit": "ml", "phase": "保湿剂"},
                {"name": "透明质酸", "amount": "2g", "percentage": 2.0, "unit": "g", "phase": "保湿剂"},
                {"name": "防腐剂", "amount": "3滴", "percentage": 0.3, "unit": "滴", "phase": "防腐剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将玫瑰花瓣浸泡在纯净水中", "temperature": "室温", "mixing_time": "24小时", "notes": "密封浸泡提取有效成分"},
                {"step_number": 2, "description": "过滤玫瑰花水", "temperature": "室温", "mixing_time": "", "notes": "去除花瓣残渣"},
                {"step_number": 3, "description": "加入透明质酸并搅拌至溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解"},
                {"step_number": 4, "description": "加入甘油并混合均匀", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保充分混合"},
                {"step_number": 5, "description": "最后加入防腐剂", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "延长保质期"}
            ],
            "benefits": [
                {"name": "深层保湿", "description": "多重保湿成分深层滋润"},
                {"name": "提亮肤色", "description": "玫瑰精华改善肌肤暗沉"},
                {"name": "舒缓肌肤", "description": "玫瑰具有舒缓镇静功效"}
            ],
            "usage": [
                {"instruction": "洁面后轻拍于面部，可重复使用", "frequency": "早晚各一次", "precautions": "避免接触眼部", "storage_conditions": "阴凉干燥处，开封后2个月内使用"}
            ]
        },
        {
            "name": "绿茶抗污染面膜",
            "category": "面膜",
            "description": "牛尔推荐绿茶抗污染面膜，抵御环境污染",
            "ingredients": [
                {"name": "绿茶粉", "amount": "25g", "percentage": 50.0, "unit": "g", "phase": "活性成分"},
                {"name": "海藻粉", "amount": "15g", "percentage": 30.0, "unit": "g", "phase": "基质"},
                {"name": "纯净水", "amount": "8g", "percentage": 16.0, "unit": "g", "phase": "水相"},
                {"name": "蜂蜜", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将绿茶粉和海藻粉混合", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合粉末"},
                {"step_number": 2, "description": "加入纯净水并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "调至适合涂抹的稠度"},
                {"step_number": 3, "description": "最后加入蜂蜜", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "增加粘性和保湿效果"}
            ],
            "benefits": [
                {"name": "抗污染", "description": "绿茶多酚抵御环境污染"},
                {"name": "深层清洁", "description": "海藻粉吸附毛孔污垢"},
                {"name": "抗氧化", "description": "强效抗氧化延缓衰老"}
            ],
            "usage": [
                {"instruction": "洁面后均匀涂抹于面部，15-20分钟后洗净", "frequency": "每周1-2次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "现做现用，不要储存"}
            ]
        }
    ]
    
    # 基于茶树油研究文献的配方
    tea_tree_recipes = [
        {
            "name": "茶树油祛痘精华",
            "category": "护肤品",
            "description": "基于茶树油研究的祛痘精华，有效抑制痤疮细菌",
            "ingredients": [
                {"name": "茶树精油", "amount": "10滴", "percentage": 2.0, "unit": "滴", "phase": "活性成分"},
                {"name": "芦荟凝胶", "amount": "40g", "percentage": 80.0, "unit": "g", "phase": "基质"},
                {"name": "透明质酸", "amount": "3g", "percentage": 6.0, "unit": "g", "phase": "保湿剂"},
                {"name": "薰衣草精油", "amount": "2滴", "percentage": 0.4, "unit": "滴", "phase": "舒缓成分"},
                {"name": "维生素E", "amount": "2滴", "percentage": 0.4, "unit": "滴", "phase": "抗氧化剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将芦荟凝胶放入干净容器", "temperature": "室温", "mixing_time": "", "notes": "确保容器无菌"},
                {"step_number": 2, "description": "加入透明质酸并搅拌至溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解"},
                {"step_number": 3, "description": "加入茶树精油并充分搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "确保精油完全分散"},
                {"step_number": 4, "description": "加入薰衣草精油", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "舒缓成分"},
                {"step_number": 5, "description": "最后加入维生素E", "temperature": "室温", "mixing_time": "1-2分钟", "notes": "抗氧化保护"}
            ],
            "benefits": [
                {"name": "抗菌", "description": "茶树精油有效抑制痤疮丙酸杆菌"},
                {"name": "消炎", "description": "减少炎症反应，促进愈合"},
                {"name": "控油", "description": "调节皮脂分泌，减少油脂"},
                {"name": "舒缓", "description": "薰衣草精油舒缓镇静肌肤"}
            ],
            "usage": [
                {"instruction": "洁面后点涂于痘痘部位，可全脸使用", "frequency": "每日2-3次", "precautions": "避开眼部，敏感肌肤慎用", "storage_conditions": "冷藏保存，开封后3个月内使用"}
            ]
        }
    ]
    
    # 基于果酸研究的配方
    aha_recipes = [
        {
            "name": "温和果酸去角质水",
            "category": "护肤品",
            "description": "基于果酸研究的温和去角质水，改善肌肤质地",
            "ingredients": [
                {"name": "乳酸", "amount": "5ml", "percentage": 10.0, "unit": "ml", "phase": "活性成分"},
                {"name": "纯净水", "amount": "35ml", "percentage": 70.0, "unit": "ml", "phase": "水相"},
                {"name": "甘油", "amount": "8ml", "percentage": 16.0, "unit": "ml", "phase": "保湿剂"},
                {"name": "透明质酸", "amount": "2g", "percentage": 4.0, "unit": "g", "phase": "保湿剂"}
            ],
            "steps": [
                {"step_number": 1, "description": "将纯净水倒入干净容器", "temperature": "室温", "mixing_time": "", "notes": "使用蒸馏水或纯净水"},
                {"step_number": 2, "description": "加入甘油并搅拌", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合"},
                {"step_number": 3, "description": "加入透明质酸并搅拌至溶解", "temperature": "室温", "mixing_time": "5-10分钟", "notes": "充分溶解"},
                {"step_number": 4, "description": "最后加入乳酸", "temperature": "室温", "mixing_time": "3-5分钟", "notes": "充分混合，注意浓度控制"}
            ],
            "benefits": [
                {"name": "去角质", "description": "乳酸温和去除老化角质"},
                {"name": "改善质地", "description": "促进细胞更新，改善肌肤质地"},
                {"name": "提亮肤色", "description": "减少肌肤暗沉，提亮肤色"},
                {"name": "收缩毛孔", "description": "改善毛孔粗大问题"}
            ],
            "usage": [
                {"instruction": "洁面后轻拍于面部，避开眼部", "frequency": "每周2-3次", "precautions": "使用后必须防晒，敏感肌肤慎用", "storage_conditions": "阴凉干燥处，开封后3个月内使用"}
            ]
        }
    ]
    
    # 基于紫草油研究的配方
    comfrey_recipes = [
        {
            "name": "紫草油修复膏",
            "category": "护肤品",
            "description": "基于紫草油研究的修复膏，促进肌肤修复愈合",
            "ingredients": [
                {"name": "紫草油", "amount": "30g", "percentage": 60.0, "unit": "g", "phase": "油相"},
                {"name": "蜂蜡", "amount": "15g", "percentage": 30.0, "unit": "g", "phase": "乳化剂"},
                {"name": "乳木果油", "amount": "5g", "percentage": 10.0, "unit": "g", "phase": "油相"}
            ],
            "steps": [
                {"step_number": 1, "description": "将紫草油和乳木果油混合", "temperature": "室温", "mixing_time": "2-3分钟", "notes": "充分混合基础油"},
                {"step_number": 2, "description": "加入蜂蜡并隔水加热", "temperature": "70-80°C", "mixing_time": "5-10分钟", "notes": "至完全融化"},
                {"step_number": 3, "description": "倒入容器并冷却", "temperature": "室温", "mixing_time": "30分钟", "notes": "自然冷却至凝固"}
            ],
            "benefits": [
                {"name": "修复愈合", "description": "紫草油促进肌肤修复"},
                {"name": "抗炎", "description": "减少炎症反应"},
                {"name": "滋润保湿", "description": "深层滋润肌肤"}
            ],
            "usage": [
                {"instruction": "取适量涂抹于需要修复的部位", "frequency": "每日2-3次", "precautions": "避免接触开放性伤口", "storage_conditions": "阴凉干燥处，避免阳光直射"}
            ]
        }
    ]
    
    # 合并所有配方
    all_recipes = (skincare_recipes + essential_oil_recipes + diy_recipes + 
                  nioer_recipes + tea_tree_recipes + aha_recipes + comfrey_recipes)
    
    print(f"开始添加 {len(all_recipes)} 个配方到数据库...")
    
    # 添加所有配方到数据库
    for recipe in all_recipes:
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
    
    print(f"\n配方添加完成！总共添加了 {len(all_recipes)} 个配方")
    
    # 显示统计信息
    products = db.search_products()
    categories = {}
    for product in products:
        category = product['category']
        categories[category] = categories.get(category, 0) + 1
    
    print("\n配方统计:")
    for category, count in categories.items():
        print(f"- {category}: {count} 个配方")
    
    print(f"\n总计: {len(products)} 个配方")

if __name__ == "__main__":
    add_comprehensive_recipes()
