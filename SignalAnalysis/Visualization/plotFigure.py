# - * - coding: utf-8 - * -
from spectrumFigure import *
from spectrogramFigure import *
from waveformFigure import *
import os

'''
获取输入文件夹内的所有 wav 文件，并返回文件名全路径的列表
'''
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.wav':
                filename = os.path.join(root, file)
                L.append(filename)
    return L

if __name__ == "__main__":
    songdir = "/Users/aaronpeng/Desktop/戏曲/实验分析/GTZAN伴奏"
    wavformdir = "/Users/aaronpeng/Desktop/戏曲/DramaGo/Statistic/实验分析/GTZAN伴奏/waveform"
    specdir = "/Users/aaronpeng/Desktop/戏曲/DramaGo/Statistic/实验分析/GTZAN伴奏/spectrum"
    spectdir = "/Users/aaronpeng/Desktop/戏曲/DramaGo/Statistic/实验分析/GTZAN伴奏/spectrogram"
    index = 0
    files = file_name(songdir)
    result = {}
    for file in files:
        result[index] = file
        displayWaveform(file,wavformdir+"/"+str(index)+".jpg")
        displaySpectrum(file,specdir+"/"+str(index)+".jpg")
        displaySpectrogram(file,spectdir+"/"+str(index)+".jpg")
        index += 1
print(result)



    
    
