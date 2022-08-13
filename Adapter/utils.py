import os
# 支持的类型
support = ['.flac']

def flac2wav(src, output_dir, format = "wav"):
    basename = os.path.basename(src)
    name = os.path.splitext(basename)[0]
    filename = os.path.join(output_dir,name + "." + format)  # 输出的文件名

    cmd = 'ffmpeg -i ' + src + ' ' + filename
    os.system(cmd)  # 执行命令行





