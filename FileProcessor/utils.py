import os
"""
文件重命名
@filename: 类别.索引.wav
将 Gtzan 的类别视作其文件名，赋予新的类别 western, 即 western.文件名.索引.wav
的格式
"""
def fileFormat(filename):
    path, name = os.path.split(filename)
    name = "western." + name
    newname = os.path.join(path,name)
    print(newname)
    os.rename(filename,newname)


