############################################
# 将 spleeter 后的结果中的人声和伴奏分别提取出来 #
# 并集中到一处                               #
############################################
import os
import shutil

"""
分别提取人声和伴奏并整合到一个文件爱你就爱，参数 type 可以有以下取值
type = "a", accompaniment, 所有的伴奏
type = "v", vocals, 所有的人声
type = "b", both, 人声和伴奏均移动
@return: 提取移动的数量
注意此函数会对文件进行重命名, 由原来的 "accompaniment.wav" 变成 "原文件名.accompaniment.wav", voclas 同理
"""
def extractMerge(dir_path, acc_path, vocals_path, type="a"):
    file_dirs = [f.path for f in os.scandir(dir_path) if f.is_dir()]    # 获取所有的子目录绝对路径，一个原始音频就是一个目录
    acc_count = 0
    vocal_count = 0
    for file_dir in file_dirs:
        wav_file = os.path.split(file_dir)[-1]  # 原始音频的文件名
        if type=="a" or type=="b":
            old_name = os.path.join(file_dir,"accompaniment.wav")
            new_name = os.path.join(acc_path,wav_file+".accompaniment.wav")
            shutil.move(old_name, new_name)
            acc_count += 1
        if type=="v" or type=="b":
            old_name = os.path.join(file_dir,"vocals.wav")
            new_name = os.path.join(vocals_path,wav_file+".vocals.wav")
            shutil.move(old_name, new_name)
            vocal_count += 1
    return acc_count, vocal_count


if __name__ == "__main__":
    dir_path = "/Volumes/LenovoDisk/戏曲数据集/分离的粤剧/guidang_output"     # 待提取合并的文件夹的路径
    accompany_dir = "/Volumes/LenovoDisk/戏曲数据集/粤剧批次6伴奏"     # 存放所有伴奏的文件夹
    vocals_dir = "/Volumes/LenovoDisk/戏曲数据集/粤剧批次6人声"   # 存放所有人声的文件夹


    acc_count, vocal_count = extractMerge(dir_path, accompany_dir, vocals_dir,"b")
    print("[提示]共移动了 %s 个人声文件和 %s 个伴奏文件" % (vocal_count, acc_count))




