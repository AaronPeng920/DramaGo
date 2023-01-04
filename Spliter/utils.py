import os
import wave
import numpy as np
import pylab as plt
import librosa
import soundfile as sf

"""
索引转为指定位数的字符串，不足则前补 '0'，默认总长度是 5 位
"""
def filenameGenerator(index, length = 5):
    return str(index).rjust(length, '0')

"""
切分音频成为若干个指定长度的片段
@filename: 文件路径
@outdir: 输出的位置
@category: 音频所属的类别
@cuttime: 切分的时间，默认 30s
@overlaprate: 窗口重叠率 [0,1)
"""
def audiocut(filename, outdir, category, cuttime = 30, overlaprate = 0):
    path, name = os.path.split(filename)
    f = wave.open(r"" + filename, 'rb')
    params = f.getparams() # 读取音频文件信息
    nchannels, sampwidth, framerate, nframes = params[:4] # 声道数, 量化位数, 采样频率, 采样点数
    str_data = f.readframes(nframes)
    f.close()

    wave_data = np.frombuffer(str_data, dtype=np.short)
    # 根据声道数对音频进行转换
    if nchannels > 1:
        wave_data.shape = -1, 2
        wave_data = wave_data.T
        temp_data = wave_data.T
    else:
        wave_data = wave_data.T
        temp_data = wave_data.T

    CutFrameNum = int(framerate * cuttime) # 每个片段的采样数
    OverlapFrameNum = int(framerate * cuttime * overlaprate)  # 重叠部分的采样数
    
    cutNum = nframes // CutFrameNum # 得到的音频片段数
    stepNum = int(CutFrameNum) 
    StepTotalNum = 0  # 当前进行到的采样数

    for j in range(int(cutNum)):
        outfilename = '.'.join((category, name.split('.')[0], filenameGenerator(j), "wav"))
        FileName = os.path.join(outdir,outfilename)
        temp_dataTemp = temp_data[stepNum * j:stepNum * (j + 1)]
        temp_dataTemp = temp_data[stepNum * (j):stepNum * (j + 1)]
        stepTotalNum = (j + 1) * stepNum
        temp_dataTemp.shape = 1, -1
        temp_dataTemp = temp_dataTemp.astype(np.short)
        f = wave.open(FileName, 'wb') # 打开 WAV 文档
        # 配置声道数、量化位数和取样频率
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        f.writeframes(temp_dataTemp.tobytes()) # 将 wav_data 转换为二进制数据写入文件
        f.close()
    
    # 返回切分得到的片段数
    return cutNum
    
def audiocutplus(filename, outdir, category, cuttime = 30, overlaprate = 0):
    path, name = os.path.split(filename)
    f = wave.open(r"" + filename, 'rb')
    params = f.getparams() # 读取音频文件信息
    nchannels, sampwidth, framerate, nframes = params[:4] # 声道数, 量化位数, 采样频率, 采样点数
    str_data = f.readframes(nframes)
    f.close()

    wave_data = np.frombuffer(str_data, dtype=np.short)
    # 根据声道数对音频进行转换
    if nchannels > 1:
        wave_data.shape = -1, 2
        wave_data = wave_data.T
        temp_data = wave_data.T
    else:
        wave_data = wave_data.T
        temp_data = wave_data.T

    CutFrameNum = int(framerate * cuttime) # 每个片段的采样数
    OverlapFrameNum = framerate * cuttime * overlaprate  # 重叠部分的采样数
    ShiftFrameNum = int(framerate * cuttime * (1-overlaprate))   # 偏移的采样数

    if nframes>=CutFrameNum:
        cutNum = 1+(nframes-CutFrameNum)//ShiftFrameNum
    else:
        cutNum = 0
    
    
    # cutNum = nframes // CutFrameNum # 得到的音频片段数
    stepNum = int(CutFrameNum) 
    StepTotalNum = 0  # 当前进行到的采样数

    for j in range(int(cutNum)):
        outfilename = '.'.join((category, name.split('.')[0], filenameGenerator(j), "wav"))
        FileName = os.path.join(outdir,outfilename)
        # temp_dataTemp = temp_data[stepNum * j:stepNum * (j + 1)]
        temp_dataTemp = temp_data[ShiftFrameNum * j:ShiftFrameNum * j + CutFrameNum]
        stepTotalNum = (j + 1) * stepNum
        temp_dataTemp.shape = 1, -1
        temp_dataTemp = temp_dataTemp.astype(np.short)
        f = wave.open(FileName, 'wb') # 打开 WAV 文档
        # 配置声道数、量化位数和取样频率
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        f.writeframes(temp_dataTemp.tobytes()) # 将 wav_data 转换为二进制数据写入文件
        f.close()
    
    # 返回切分得到的片段数
    return cutNum


