#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查数据库中的配方
"""

from extract_pdf_data import CosmeticsDatabase

def main():
    db = CosmeticsDatabase()
    products = db.search_products()
    
    print(f"数据库中现有 {len(products)} 个配方:")
    print("=" * 50)
    
    for i, product in enumerate(products, 1):
        print(f"{i:2d}. {product['name']} - {product['category']}")
        if product.get('description'):
            desc = product['description'][:60] + "..." if len(product['description']) > 60 else product['description']
            print(f"    描述: {desc}")
        print()
    
    # 按分类统计
    categories = {}
    for product in products:
        cat = product['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print("分类统计:")
    print("-" * 30)
    for cat, count in sorted(categories.items()):
        print(f"{cat}: {count} 个配方")

if __name__ == "__main__":
    main()


