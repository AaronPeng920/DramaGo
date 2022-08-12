# 戏曲数据集获取

## 一、创建环境以及安装依赖

1. 事先安装 Anaconda，可以在命令行输入：

```shell
conda -V
```

显示版本号，则可以使用 conda。在一些情况下，需要给 conda 添加国内源镜像加速，换源方式参考 https://zhuanlan.zhihu.com/p/434356947

2. 创建一个名称为 _opera_ 的虚拟环境（可以自拟名称），使用到的 _python_ 版本为 3.9:

```shell
conda create -n opera python=3.9
```

安装过程中会出现 **Proceed ([y]/n)?**，输入 **y** 后回车即可。

3. 激活虚拟环境

```shell
conda activate opera
```

这里出现的 _opera_ 是上一步创建的虚拟环境名称

4. 安装需要的依赖包

```shell
librosa
soundfile
numpy
scipy
matplotlab
```

## 二、数据的处理和数据集的获取

> 本项目用到的所有原始数据位于 **百度网盘/戏曲新分类** 下，账号和密码可以在微信群里获取。

### （一）去除音频静音

> 目前 _mute_remove_ 模块仅支持 **.wav** 文件，其他文件类型暂未测试，当目录中含有多种类型的音频文件时，只对 **.wav** 文件进行处理

> 静音去除的原理是找到连续的大于 10 个静音帧并删除（由 **mute_remove/utils line 25** 中的 **frame_threshold** 参数指定，如果你觉得去除不干净，可以尝试减小这个参数）

1. 将所有需要去除静音的 **.wav** 文件存放在 **Audios/sources** 中
2. 在 **mute_remove/removeMute.py** 中，找到 **__main__**，其中有两个参数 **wav_dir** 和 **output_dir**，将它们分别改成 **Audios/sources** 和 **Audios/slience_remove**，也就是原音频所在的位置和去除静音后音频存放的位置
3. 执行 python 文件 **mute_remove/removeMute.py**，如果你在命令行中，可以将此项目作为工作目录，执行：

```python
python3 mute_remove/removeMute.py
```

### （二）分割片段

> 将音频切割成 30s 长的片段，为了便于后续的使用，会改变切割后音频的命名。例如对于一个名称为 **a.wav** 的 **粤剧**，设将其分为 100 个片段（如果最后一个片段不足指定长度会舍弃），分割后的各个片段的名称会是 **yueju.a.00000.wav** 到 **yueju.a.00099.wav**，分别是 **类别.文件名.片段序号.wav**。

1. 上一步得到的文件存放在 **Audios/slience_remove** 中，找到 **spliter/cut_audio** 文件，其中 **main** 中含有两个参数，分别是 **wav_dir** 和 **output_dir**，将它们分别改成  **Audios/slience_remove** 和 **Audios/audio_cut**，也就是去除静音后的音频所在的位置和切分后的音频片段存放的位置，将 **category** 改为操作的剧种的名称拼音，如 **粤剧(yueju)**；
2. 执行 python 文件 **spliter/cut_audio.py**，如果你在命令行中，可以将此项目作为工作目录，执行：

```python
python3 spliter/cut_audio.py
```

### （三）人声和伴奏的分类

​	暂时不作处理，根据需要进行操作





