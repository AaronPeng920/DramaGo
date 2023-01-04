import os
from utils import separate

'''
获取输入文件夹内的所有 wav 文件，并返回文件名全路径的列表
'''
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file[0] == '.':
                continue
            # if os.path.splitext(file)[1] == '.wav':
            filename = os.path.join(root, file)
            L.append(filename)
    return L

if __name__ == '__main__':
    wav_dir = "/Users/aaronpeng/Desktop/Adobe/音频材料"  # 需要进行分离的所有问 wav 文件所在的文件夹
    output_dir = "/Users/aaronpeng/Desktop/Adobe/test"    # 结果输出的文件夹
    wav_files = file_name(wav_dir)  # 获取文件夹内的所有语音文件
    # 对每一个文件进行操作
    for filename in wav_files:
        # 进行分离
        print("正在处理:",filename)
        separate(filename, output_dir)
        