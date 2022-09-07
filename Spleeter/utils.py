import os

"""
分离音频
@src: 原音频文件路径
@output_dir: 分离后的输出目录
@stems: 分离的音轨数量，默认是 2 个
"""
def separate(src, output_dir, stems = 2):
    cmd_command = "spleeter separate -p " + "spleeter:" + str(stems) + "stems -o " + output_dir + " " + src
    os.system(cmd_command)







