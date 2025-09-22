#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
化妆品DIY配方库统计报告
"""

from extract_pdf_data import CosmeticsDatabase

def generate_statistics():
    """生成配方库统计报告"""
    db = CosmeticsDatabase()
    
    print("=" * 60)
    print("🌿 化妆品DIY配方库 - 完整统计报告")
    print("=" * 60)
    
    # 获取所有产品
    products = db.search_products()
    
    # 按分类统计
    categories = {}
    for product in products:
        category = product['category']
        categories[category] = categories.get(category, 0) + 1
    
    print(f"\n📊 配方总数: {len(products)} 个")
    print("\n📂 分类统计:")
    for category, count in categories.items():
        icon = {
            '护肤品': '🧴',
            '面膜': '🧖‍♀️', 
            '护发产品': '💇‍♀️',
            '精油': '🌿'
        }.get(category, '📦')
        print(f"  {icon} {category}: {count} 个配方")
    
    # 按功效统计
    print("\n✨ 功效统计:")
    benefit_count = {}
    for product in products:
        detail = db.get_product_details(product['id'])
        for benefit in detail['benefits']:
            benefit_name = benefit['name']
            benefit_count[benefit_name] = benefit_count.get(benefit_name, 0) + 1
    
    # 显示前10个功效
    sorted_benefits = sorted(benefit_count.items(), key=lambda x: x[1], reverse=True)
    for i, (benefit, count) in enumerate(sorted_benefits[:10]):
        print(f"  {i+1:2d}. {benefit}: {count} 个配方")
    
    # 原料统计
    print("\n🧪 常用原料统计:")
    ingredient_count = {}
    for product in products:
        detail = db.get_product_details(product['id'])
        for ingredient in detail['ingredients']:
            ingredient_name = ingredient['name']
            ingredient_count[ingredient_name] = ingredient_count.get(ingredient_name, 0) + 1
    
    # 显示前15个常用原料
    sorted_ingredients = sorted(ingredient_count.items(), key=lambda x: x[1], reverse=True)
    for i, (ingredient, count) in enumerate(sorted_ingredients[:15]):
        print(f"  {i+1:2d}. {ingredient}: {count} 次使用")
    
    # 详细分类展示
    print("\n📋 详细配方列表:")
    for category in sorted(categories.keys()):
        category_products = [p for p in products if p['category'] == category]
        icon = {
            '护肤品': '🧴',
            '面膜': '🧖‍♀️', 
            '护发产品': '💇‍♀️',
            '精油': '🌿'
        }.get(category, '📦')
        
        print(f"\n  {icon} {category} ({len(category_products)} 个):")
        for product in category_products:
            print(f"    • {product['name']}")
    
    # 制作难度统计
    print("\n🎯 制作难度分析:")
    easy_count = 0
    medium_count = 0
    hard_count = 0
    
    for product in products:
        detail = db.get_product_details(product['id'])
        step_count = len(detail['steps'])
        ingredient_count = len(detail['ingredients'])
        
        if step_count <= 3 and ingredient_count <= 4:
            easy_count += 1
        elif step_count <= 5 and ingredient_count <= 6:
            medium_count += 1
        else:
            hard_count += 1
    
    print(f"  🟢 简单 (≤3步, ≤4原料): {easy_count} 个")
    print(f"  🟡 中等 (4-5步, 5-6原料): {medium_count} 个")
    print(f"  🔴 复杂 (>5步, >6原料): {hard_count} 个")
    
    # 推荐配方
    print("\n⭐ 推荐配方:")
    recommendations = [
        ("薰衣草保湿面霜", "适合初学者的经典配方"),
        ("茶树精油祛痘凝胶", "针对痘痘肌肤的明星产品"),
        ("燕麦蜂蜜去角质磨砂膏", "温和去角质，适合敏感肌肤"),
        ("薄荷清凉洗发水", "天然护发，清爽控油"),
        ("薰衣草舒缓按摩油", "放松身心，促进睡眠")
    ]
    
    for name, description in recommendations:
        print(f"  • {name}: {description}")
    
    print("\n" + "=" * 60)
    print("🎉 配方库建设完成！")
    print("💡 现在你可以在浏览器中访问 http://localhost:5000 查看所有配方")
    print("🔍 支持按名称、成分、功效搜索，按分类浏览")
    print("📱 响应式设计，手机和电脑都能完美使用")
    print("=" * 60)

if __name__ == "__main__":
    generate_statistics()
