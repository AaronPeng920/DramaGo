from utils import *
import os

"""
将其他的音频格式转为 wav
以及处理 RIFF ID 的错误问题
"""


'''
获取输入文件夹内的所有音频文件，并返回文件名全路径的列表
'''
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] in support:
                filename = os.path.join(root, file)
                newname = rename(filename)
                L.append(newname)
    return L

if __name__ == '__main__':
    wav_dir = "/Volumes/LenovoDisk/粤剧1000数据集/粤剧1000"  # 需要转换为 wav 的文件所在的文件夹
    output_dir = "/Volumes/LenovoDisk/粤剧1000数据集/粤剧1000TIFF"    # 转换后的文件存储的位置

    wav_files = file_name(wav_dir)  # 获取文件夹内的所有语音文件
    # 对每一个文件进行操作
    for filename in wav_files:
        print(filename)
        type = filename.split('.')[-1]
        if '.'+type in support:
            other2wav(filename, output_dir)
        else:
            print("暂不支持将 " + type + " 类型的文件转换成 wav")
            

