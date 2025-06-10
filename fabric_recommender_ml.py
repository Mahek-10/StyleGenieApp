def recommend_fabric_rule(fabric_type, season="Summer", style="Casual"):
    fabrics = {
        ("Shirt", "Summer", "Casual"): "Cotton",
        ("Shirt", "Winter", "Formal"): "Flannel",
        ("Pants", "Winter", "Formal"): "Wool",
        ("Jacket", "Winter", "Casual"): "Leather",
        ("Dress", "Summer", "Formal"): "Silk",
        ("Dress", "Winter", "Casual"): "Velvet",
        ("Pants", "Summer", "Casual"): "Linen",
        ("Jacket", "Summer", "Formal"): "Tweed"
    }
    key = (fabric_type, season, style)
    return f"Recommended fabric: {fabrics.get(key, 'Linen')}"
