# - * - coding: utf-8 - * -
from turtle import color
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random

plt.figure(dpi=600) # 将显示的所有图分辨率调高
matplotlib.rc("font",family='SimHei') # 显示中文
matplotlib.rcParams['axes.unicode_minus']=False # 显示符号

import random
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color
    
"""
随机产生 n 个颜色
"""
def randomColor(n):
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    rst = []
    for i in range(n):
        color = ""
        for j in range(6):
            color += colorArr[random.randint(0,14)]
        color = '#' + color
        rst.append(color)
    return rst

class BarPloter:
    def __init__(self, ticks, data, figsize=(10,7)):
        self.data = data    # 数值
        self.ticks = ticks    # 横轴标题
        self.figsize = figsize    # 表格大小
        self.colors = randomColor(len(data))    # 随机颜色

    def changeTicks(self, ticks):
        self.ticks = ticks

    def plot(self):
        plt.figure(figsize=self.figsize)
        plt.bar(self.ticks, self.data, color=self.colors)
        for a,b in zip(self.ticks, self.data):    # 显示条形的数值
            plt.text(a,b,
             b,
             ha='center', 
             va='bottom',
            )
        plt.show()

    def savefig(self,path):
        plt.figure(figsize=self.figsize)
        plt.bar(self.ticks, self.data, color=self.colors)
        for a,b in zip(self.ticks, self.data):    # 显示条形的数值
            plt.text(a,b,
             b,
             ha='center', 
             va='bottom',
            )
        plt.savefig(path)

if __name__ == '__main__':
    data = [0.97, 0.96, 0.98, 0.965]
    labels = ['GD+COD','GAD+COAD','GAD+COD','GD+COAD']
    bar = BarPloter(labels, data)
    bar.savefig('Statistic/paperFig/二分类准确率.png')


