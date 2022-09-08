# - * - coding: utf-8 - * -
import librosa
import librosa.display
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

"""
单通道音频波形图，时域波形
x 轴: 时间
y 轴：振幅
"""

plt.figure(dpi=600) # 将显示的所有图分辨率调高
matplotlib.rc("font",family='SimHei') # 显示中文
matplotlib.rcParams['axes.unicode_minus']=False # 显示符号

# 显示语音时域波形
def displayWaveform(filepath, savepath): 
    """
    :filepath 音频文件路径
    :savepath 绘制的图的保存路径
    """
    samples, sr = librosa.load(filepath, sr=16000)
    # samples = samples[6000:16000]

    print("[时域波形]采样点数 %s, 采样率 %s" % (len(samples), sr))
    time = np.arange(0, len(samples)) * (1.0 / sr)

    plt.plot(time, samples)
    plt.title("语音信号时域波形")
    plt.xlabel("时长（秒）")
    plt.ylabel("振幅")
    # plt.savefig("your dir\语音信号时域波形图", dpi=600)
    plt.savefig(savepath, dpi=600)


