from typing import Any, Dict, List, Optional


def sort_products_by_price(products: List[Dict[str, Any]], category: Optional[str] = None) -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей и сортирует продукты по убыванию стоимости в переданной категории"""
    if category:
        filtered_products = [product for product in products if product.get("category") == category]
    else:
        filtered_products = products

    sorted_products = sorted(filtered_products, key=lambda x: x.get("price", 0), reverse=True)
    return sorted_products


def orders_stats(orders):
    pass
