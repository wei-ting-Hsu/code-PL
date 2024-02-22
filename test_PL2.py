import pandas as pd
import numpy as np

df_audlt = pd.read_csv('adult.csv')
audlt_income = df_audlt['Income']

print(df_audlt)

# 計算平均值
mean_value = audlt_income.mean()
print("平均值：")
print(mean_value)

# 計算標準差
std_value = audlt_income.std()
print("標準差：")
print(std_value)

# 計算中位數
median_value = audlt_income.median()
print("中位數：")
print(median_value)