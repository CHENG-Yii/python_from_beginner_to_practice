#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 同时掷两个骰子
import pygal

from die import Die

# 创建两个骰子
die_1 = Die()
die_2 = Die(10)

# 投掷骰子多次，并把结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist=pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = range(2, max_result + 1)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')
