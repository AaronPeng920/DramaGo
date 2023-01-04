from unicodedata import category
from utils import audiocut
from utils import audiocutplus
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
    wav_dir = "/Volumes/LenovoDisk/戏曲数据集/粤剧/原粤剧去静音"  # 需要切分的 wav 文件所在的文件夹
    output_dir = "/Volumes/LenovoDisk/戏曲数据集/粤剧/原粤剧一分钟"    # 切分后的文件存储的位置
    category = "yueju"  # 处理的音频种类

    stafilename = os.path.join("Statistic",category+".txt") # 统计数据文件名称
    writecontent = []  # 统计数据
    wav_files = file_name(wav_dir)  # 获取文件夹内的所有语音文件
    # 对每一个文件进行操作
    for filename in wav_files:
        # 切分
        # cutNum = audiocut(filename, output_dir, category)
        try:
            cutNum = audiocutplus(filename, output_dir, category, 600)
            writecontent.append(filename + "," + str(cutNum) + "\n")
        except Exception as e:
            print(filename + "[Error]")
            continue
    with open(stafilename,"w") as f:
        f.writelines(writecontent)

# origin =  '/Users/aaronpeng/青花瓷.wav'
# output_dir =  '/Users/aaronpeng/Desktop/temp' 
# cutNum = audiocut(origin, output_dir, 'qinghuaci')