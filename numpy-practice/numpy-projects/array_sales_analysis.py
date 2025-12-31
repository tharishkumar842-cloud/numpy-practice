import numpy as np

sales = np.array([
    [50, 60, 55, 70, 65, 80, 75],
    [40, 45, 50, 55, 60, 65, 70],
    [30, 35, 40, 45, 50, 55, 60],
    [20, 25, 30, 35, 40, 45, 50]
])

total_per_product = np.sum(sales, axis=1)

total_per_day = np.sum(sales, axis=0)


print("Total sales per product:", total_per_product)
print("Total sales per day:", total_per_day)
print("Product with maximum total sales:", np.argmax(total_per_product))
print("Days where total sales exceeded 200:", total_per_day >200)

