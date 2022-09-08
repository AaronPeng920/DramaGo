# - * - coding: utf-8 - * -
import librosa
import librosa.display
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

"""
单通道频谱图，基于短时傅里叶变换
x 轴: 时间
y 轴：频率
色彩：给定时刻给定频率下的振幅
"""

plt.figure(dpi=600) # 将显示的所有图分辨率调高
matplotlib.rc("font",family='SimHei') # 显示中文
matplotlib.rcParams['axes.unicode_minus']=False # 显示符号

# 频谱图
def displaySpectrogram(filepath, savepath):
    """
    :filepath 音频文件路径
    :savepath 绘制的图的保存路径
    """
    x, sr = librosa.load(filepath, sr=16000)

    # compute power spectrogram with stft(short-time fourier transform):
    # 基于stft，计算power spectrogram
    spectrogram = librosa.amplitude_to_db(librosa.stft(x))

    # show
    librosa.display.specshow(spectrogram, y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('语音信号对数谱图')
    plt.xlabel('时长（秒）')
    plt.ylabel('频率（赫兹）')
    plt.savefig(savepath, dpi=600)
