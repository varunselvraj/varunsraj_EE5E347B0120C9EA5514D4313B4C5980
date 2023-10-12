def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage
products = ["apple", "banana", "orange", "apple", "grape", "apple"]
target_product = "apple"
result = linear_search_product(products, target_product)
if result:
    print(f"The product '{target_product}' found at indices: {result}")
else:
    print(f"The product '{target_product}' not found in the list.")