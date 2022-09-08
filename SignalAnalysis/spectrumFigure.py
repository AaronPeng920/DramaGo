# - * - coding: utf-8 - * -
import librosa
import librosa.display
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

"""
单通道频域波形图，频域波形
x 轴: 频率
y 轴：振幅
"""

plt.figure(dpi=600) # 将显示的所有图分辨率调高
matplotlib.rc("font",family='SimHei') # 显示中文
matplotlib.rcParams['axes.unicode_minus']=False # 显示符号

# 显示语音频域谱线
def displaySpectrum(filepath, savepath): 
    """
    :filepath 音频文件路径
    :savepath 绘制的图的保存路径
    """
    x, sr = librosa.load(filepath, sr=16000)
    print("[频域谱线]采样点数 %s, 采样率 %s" % (len(x), sr))
    # ft = librosa.stft(x)
    # magnitude = np.abs(ft)  # 对fft的结果直接取模（取绝对值），得到幅度magnitude
    # frequency = np.angle(ft)  # (0, 16000, 121632)

    ft = fft(x)
    # print(len(ft), type(ft), np.max(ft), np.min(ft))
    magnitude = np.absolute(ft)  # 对fft的结果直接取模（取绝对值），得到幅度magnitude
    frequency = np.linspace(0, sr, len(magnitude))  # (0, 16000, 121632)

    # print(len(magnitude), type(magnitude), np.max(magnitude), np.min(magnitude))
    # print(len(frequency), type(frequency), np.max(frequency), np.min(frequency))

    # plot spectrum，限定[:40000]
    # plt.figure(figsize=(18, 8))
    plt.plot(frequency[:40000], magnitude[:40000])  # magnitude spectrum
    plt.title("语音信号频域谱线")
    plt.xlabel("频率（赫兹）")
    plt.ylabel("幅度")
    plt.savefig(savepath, dpi=600)

    # # plot spectrum，不限定 [对称]
    # plt.figure(figsize=(18, 8))
    # plt.plot(frequency, magnitude)  # magnitude spectrum
    # plt.title("语音信号频域谱线")
    # plt.xlabel("频率（赫兹）")
    # plt.ylabel("幅度")
    # plt.show()