import os
from utils import separate

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
    wav_dir = "/Volumes/LenovoDisk/戏曲/豫剧/sources"  # 需要进行分离的所有问 wav 文件所在的文件夹
    output_dir = "/Volumes/LenovoDisk/戏曲/豫剧/slience_remove"    # 结果输出的文件夹
    wav_files = file_name(wav_dir)  # 获取文件夹内的所有语音文件
    # 对每一个文件进行操作
    for filename in wav_files:
        # 进行分离
        separate(filename, output_dir)
        