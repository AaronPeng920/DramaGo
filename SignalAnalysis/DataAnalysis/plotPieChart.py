# - * - coding: utf-8 - * -
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

class PiePloter:
    def __init__(self, data, labels, figsize=(6,9)):
        self.data = data
        self.labels = labels
        self.colors = randomColor(len(data))
        self.explodes = [0] * len(data)
        self.figsize = figsize

    def changeColor(self, colors):
        self.colors = colors

    def changeExplode(self, explodes):
        self.explodes = explodes
        
    def plot(self):
        plt.figure(figsize=self.figsize)
        plt.pie(self.data,     # 数据
        labels=self.labels,    # 数据标签
        explode=self.explodes,  # 突出的饼块，越大突出越多
        colors=self.colors,     # 每块对应的颜色
        autopct = '%3.2f%%',  # 数值类型，保留 2 位小数
        shadow=False,   # 无阴影设置
        startangle=90,   # 逆时针起始角度设置
        pctdistance=0.6   # 数值到远心的距离，单位是半径的倍数
        )
        plt.axis('equal')    # x,y 轴刻度一直保证为饼形
        plt.legend(loc='upper left')  # 加上图例
        plt.show()

    def savefig(self, path):
        plt.figure(figsize=self.figsize)
        plt.pie(self.data,     # 数据
        labels=self.labels,    # 数据标签
        explode=self.explodes,  # 突出的饼块，越大突出越多
        colors=self.colors,     # 每块对应的颜色
        autopct = '%3.2f%%',  # 数值类型，保留 2 位小数
        shadow=False,   # 无阴影设置
        startangle=90,   # 逆时针起始角度设置
        pctdistance=0.6   # 数值到远心的距离，单位是半径的倍数
        )
        plt.axis('equal')    # x,y 轴刻度一直保证为饼形
        plt.legend(loc='upper left')  # 加上图例
        plt.savefig(path)


if __name__ == '__main__':
    data = [228, 394, 1, 5, 48, 5, 160, 74, 57, 28]
    labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    pie = PiePloter(data, labels)
    pie.plot()



