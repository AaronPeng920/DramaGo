from utils import slience_ffmpeg
from utils import slience
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

if __name__ == '__main__':
    wav_dir = "/Volumes/LenovoDisk/戏曲数据集/粤剧/原粤剧伴奏十分钟/粤剧伴奏批次1"  # 需要去除空白的 wav 文件所在的文件夹
    output_dir = "/Volumes/LenovoDisk/戏曲数据集/粤剧/原粤剧伴奏十分钟去静音"    # 去除空白后的文件存储的位置

    wav_files = file_name(wav_dir)  # 获取文件夹内的所有语音文件
    # 对每一个文件进行操作
    for filename in wav_files:
        # 去除静音段
        slience_data = slience_ffmpeg(filename, output_dir)
        # 这里得到的就是去除静音后的数据，默认 fs 为 16k,大家可以在此基础上继续进行开发
