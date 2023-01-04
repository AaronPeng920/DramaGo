from hashlib import new
import os
import random
import shutil
# 支持的类型
support = ['.flac', '.mp3', '.wav']

def other2wav(src, output_dir, format = "wav"):
    """
    其他格式 转 wav
    """
    basename = os.path.basename(src)
    name = os.path.splitext(basename)[0]
    filename = os.path.join(output_dir,name + "." + format)  # 输出的文件名

    cmd = 'ffmpeg -y -i "' + src + '" "' + filename + '"'    # -y 参数设置的是不询问就自动覆盖同名的文件
    os.system(cmd)  # 执行命令行

def rename(src):
    """
    文件重命名，去掉原文件名中的空格
    """
    srcname = src
    path, name = os.path.split(src)
    name = ''.join(name.split())
    lst = name.split('.')
    type = lst[-1]
    newfilename = ''.join(lst[:-1]) + '.' + type
    newname =  os.path.join(path,newfilename)
    if srcname != newname:
        os.rename(srcname,newname)
        return newname
    else:
        return srcname

def randomChoose(src_dir, output_dir, num):
    """
    从 src_dir 中完全随机选择 num 个文件拷贝到 output_dir 中
    选择的文件信息写入到 '../Statistic/copyfile.txt'
    """
    count = 0
    filenames = []
    log_path = './Statistic/copyfile.txt'

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            filenames.append(os.path.join(root,file))   # 获取所有的文件名
    
    random.shuffle(filenames)    # 打乱所有的文件名

    with open(log_path, 'w') as f:
        for file in filenames:
            basename = os.path.basename(file)
            newname = os.path.join(output_dir, basename)
            f.write(file + " -> " + newname + "\n")
            shutil.copyfile(file, newname)
            count += 1
            if count >= num:
                print("从", src_dir, "中选择了", num, "个文件到", output_dir)
                f.write("从 " + src_dir + " 中选择了 " + str(num) + " 个文件到 " + output_dir + "\n")
                break


