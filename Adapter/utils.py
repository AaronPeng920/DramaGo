from hashlib import new
import os
# 支持的类型
support = ['.flac', '.mp3', '.wav']

"""
其他格式 转 wav
"""
def other2wav(src, output_dir, format = "wav"):
    basename = os.path.basename(src)
    name = os.path.splitext(basename)[0]
    filename = os.path.join(output_dir,name + "." + format)  # 输出的文件名

    cmd = 'ffmpeg -i "' + src + '" "' + filename + '"'
    os.system(cmd)  # 执行命令行

"""
文件重命名，去掉原文件名中的空格
"""
def rename(src):
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




