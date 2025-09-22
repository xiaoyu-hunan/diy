#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
导入所有配方到数据库
"""

from extract_pdf_data import CosmeticsDatabase
import additional_recipes
import advanced_recipes
import comprehensive_recipes
import extended_recipes
import professional_recipes
import specialized_recipes

def main():
    print("开始导入所有配方...")
    
    # 检查当前数据库状态
    db = CosmeticsDatabase()
    initial_count = len(db.search_products())
    print(f"导入前数据库中有 {initial_count} 个配方")
    
    # 导入各种配方
    try:
        print("\n1. 导入额外配方...")
        additional_recipes.add_additional_recipes()
        print("   ✓ 额外配方导入完成")
    except Exception as e:
        print(f"   ✗ 额外配方导入失败: {e}")
    
    try:
        print("\n2. 导入高级配方...")
        advanced_recipes.add_advanced_recipes()
        print("   ✓ 高级配方导入完成")
    except Exception as e:
        print(f"   ✗ 高级配方导入失败: {e}")
    
    try:
        print("\n3. 导入全面配方...")
        comprehensive_recipes.add_comprehensive_recipes()
        print("   ✓ 全面配方导入完成")
    except Exception as e:
        print(f"   ✗ 全面配方导入失败: {e}")
    
    try:
        print("\n4. 导入扩展配方...")
        extended_recipes.add_extended_recipes()
        print("   ✓ 扩展配方导入完成")
    except Exception as e:
        print(f"   ✗ 扩展配方导入失败: {e}")
    
    try:
        print("\n5. 导入专业配方...")
        professional_recipes.add_professional_recipes()
        print("   ✓ 专业配方导入完成")
    except Exception as e:
        print(f"   ✗ 专业配方导入失败: {e}")
    
    try:
        print("\n6. 导入专业配方...")
        specialized_recipes.add_specialized_recipes()
        print("   ✓ 专业配方导入完成")
    except Exception as e:
        print(f"   ✗ 专业配方导入失败: {e}")
    
    # 检查最终状态
    final_count = len(db.search_products())
    added_count = final_count - initial_count
    
    print(f"\n导入完成！")
    print(f"新增配方: {added_count} 个")
    print(f"数据库总配方数: {final_count} 个")
    
    # 显示分类统计
    products = db.search_products()
    categories = {}
    for product in products:
        cat = product['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\n分类统计:")
    print("-" * 30)
    for cat, count in sorted(categories.items()):
        print(f"{cat}: {count} 个配方")

if __name__ == "__main__":
    main()


