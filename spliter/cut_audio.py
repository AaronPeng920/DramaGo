from unicodedata import category
from utils import audiocut
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
    wav_dir = "Audios/slience_remove"  # 需要切分的 wav 文件所在的文件夹
    output_dir = "Audios/audio_cut"    # 切分后的文件存储的位置
    category = "yuju"  # 处理的音频种类

    stafilename = os.path.join("Statistic",category+".txt") # 统计数据文件名称
    writecontent = []  # 统计数据
    wav_files = file_name(wav_dir)  # 获取文件夹内的所有语音文件
    # 对每一个文件进行操作
    for filename in wav_files:
        # 切分
        cutNum = audiocut(filename, output_dir, category)
        writecontent.append(filename + "," + str(cutNum) + "\n")
    with open(stafilename,"w") as f:
        f.writelines(writecontent)

        