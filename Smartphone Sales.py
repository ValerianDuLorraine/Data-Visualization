#import database
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#biggest phone brands
brands = ["Apple", "Samsung", "Xiaomi", "Oppo", "Vivo", "Huawei", "Others"]

#sales figures 
Q1_2018 = [52.2, 78.2, 28.1, 24.2, 18.9, 39.3, 121.7]
Q1_2020 = [40.0, 58.6, 29.7, 22.3, 21.6, 49.0, 66.6]
years = ["2018", "2020"]

#total sales
sales_2018 = sum(Q1_2018)
sales_2020 = sum(Q1_2020)
sales = [sales_2018, sales_2020]

#2018 market share
plt.pie(Q1_2018, labels = brands)
plt.show() 
#2020 market share
plt.pie(Q1_2020, labels = brands)
plt.show() 
#total sales 2018 vs 2020
plt.bar(years,sales)
plt.show()
