from utils import fileFormat
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

if __name__ == "__main__":
    wavdir = r"/Volumes/LenovoDisk/参考数据集/GTZAN/waves"

    files = file_name(wavdir)
    count = 0
    for file in files:
        fileFormat(file)
        count += 1
    print("[状态]处理了",count,"个文件.")


