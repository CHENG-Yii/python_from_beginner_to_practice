#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
import matplotlib
import matplotlib.pyplot as plt

#  绘制折线图
squares = [1,4,9,16,25]
plt.plot(squares, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squar of value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values, squares, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squar of value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()


# 绘制散点图
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]
plt.scatter(x_values,y_values, edgecolor='none', s=100)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# 自动计算数据
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=10)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# 颜色映射
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, 
            edgecolor='none', s=10)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()












