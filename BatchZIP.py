"""
将文件夹内的文件分成批次存放在另一个文件夹中，压缩文件夹
"""

import os
import random
import shutil
import zipfile

'''
获取输入文件夹内的所有 wav 文件，并返回文件名全路径的列表
'''
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.wav' and file[0] != '.':
                filename = os.path.join(root, file)
                L.append(filename)
    return L

"""
获取文件夹下所有的子文件夹, 返回所有文件夹的绝对路径
"""
def get_dirs(input_dir):
    dbtype_list = os.listdir(input_dir)
    rst = []
    for dbtype in dbtype_list:
        if not os.path.isfile(os.path.join(input_dir,dbtype)) and dbtype[0] != '.':
            rst.append(os.path.join(input_dir,dbtype))
    return rst


"""
将 input_dir 中的文件每 num 个分批存放在 output_dir 中
@output_dir: 输出的文件夹
@input_dir: 输入文件存放的文件夹
@num: 每个批次含有的文件数量
@description: 每次批次文件夹的描述即文件名
@return: 文件总数量和批次数量以及每个批次的文件数量
"""
def batch(output_dir, input_dir, num, description="批次"):
    files = file_name(input_dir)
    file_count = len(files)
    if(file_count%num==0):
        batch_count = file_count // num
    else:
        batch_count = file_count // num + 1
    random.shuffle(files)  # 打乱列表
    # 拷贝文件
    for i in range(batch_count):
        batchfiles = files[i*num:(i+1)*num]  # 该批次的所有文件
        dstpath = os.path.join(output_dir,description+str(i))
        os.makedirs(dstpath) # 创建批次文件夹
        for f in batchfiles:
            path, name = os.path.split(f)  # name 是文件名
            dstname = os.path.join(dstpath,name)
            shutil.copyfile(f,dstname)
    print("[结果]文件共 {} 个, 分成 {} 个批次, 每个批次最多 {} 个文件".format(file_count,batch_count,num))
    return file_count,batch_count,num

"""
压缩文件夹到指定目录
"""
def zipall(input_dir, output_dir):
    dirs = get_dirs(input_dir)
    count = len(dirs)
    for dir in dirs:
        path, name = os.path.split(dir)  # 文件夹的名字
        finalname = os.path.join(output_dir,name+".zip")
        zipf = zipfile.ZipFile(finalname,'w')
        zipf.write(dir,finalname)
    print('共压缩 {} 个文件'.format(count))
    return count


if __name__ == '__main__':
    input_dir = "/Volumes/LenovoDisk/戏曲数据集/粤剧/原粤剧伴奏一分钟去静音"
    batch_dir = "/Volumes/LenovoDisk/戏曲数据集/粤剧/原粤剧伴奏一分钟去静音500分批压缩"
    batch(batch_dir, input_dir, 500, "粤剧伴奏去静音一分钟片段500分批")
    zipall(batch_dir,batch_dir)
    



    








