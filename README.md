# 戏曲数据集获取

## 一、创建环境以及安装依赖

1. 事先安装 Anaconda，可以在命令行输入：

```shell
conda -V
```

显示版本号，则可以使用 conda。在一些情况下，需要给 conda 添加国内源镜像加速，换源方式参考 [conda 添加国内源](https://zhuanlan.zhihu.com/p/434356947)

2. 创建一个名称为 _opera_ 的虚拟环境（可以自拟名称），使用到的 _python_ 版本为 3.7:

```shell
conda create -n opera python=3.7
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
matplotlib
```

5. 安装媒体处理工具 **ffmpeg** 并将其加入到 **环境变量**，Windows 10 可以参考 [Windows 10 安装 FFmpeg 并设置环境变量](https://blog.csdn.net/Chanssl/article/details/83050959) ，MacOS 可以参考 [在 Mac 上为 FFmpeg 配置环境变量](https://zhuanlan.zhihu.com/p/137556439)。安装之后，可以在命令行输入：

```shell
ffmpeg
```

如果出现版本号以及其他提示信息，则说明安装成功。

## 二、数据的处理和数据集的获取

> 本项目用到的所有原始数据位于 **百度网盘/戏曲新分类** 下，账号和密码可以在微信群里获取

### （一）格式转换

> 对于 **flac** 等格式的音频，目前无法被 **librosa** 读取，为了避免后期出现问题，统一将音频格式转换为 **wav**，由于文件名命名可能对后期造成的影响，故在其中对文件名进行去空格和去除 . 符号。<font color='red'>**不论原音频格式如何（包括 wav），均建议执行此步，以便规范化文件名**</font>

1. 在 **Adapter/converter** 中，找到 **__main__**，其中有两个参数 **wav_dir** 和 **output_dir**，将其改为需要转换的音频所在的文件夹以及转换后存储到的文件夹，如果原始的音频较大存在硬盘/磁盘中，可以将将 **wav_dir** 设置为磁盘/硬盘中的存储地址，将 **output_dir** 设置为 **Audios/sources**，承接去除静音的第一步；
2. 执行 python 文件 **Adapter/converter.py**，如果你在命令行中，可以将此项目作为工作目录，执行：

```python
python3 Adapter/converter.py
```

### （二）去除音频静音

> 目前 _mute_remove_ 模块仅支持 **.wav** 文件，其他文件类型暂未测试，当目录中含有多种类型的音频文件时，只对 **.wav** 文件进行处理

> 静音去除的原理是找到连续的大于 10 个静音帧并删除（由 **mute_remove/utils line 25** 中的 **frame_threshold** 参数指定，如果你觉得去除不干净，可以尝试减小这个参数）

1. 将所有需要去除静音的 **.wav** 文件存放在 **Audios/sources** 中
2. 在 **Mute_remove/removeMute.py** 中，找到 **__main__**，其中有两个参数 **wav_dir** 和 **output_dir**，将它们分别改成 **Audios/sources** 和 **Audios/slience_remove**，也就是原音频所在的位置和去除静音后音频存放的位置
3. 执行 python 文件 **Mute_remove/removeMute.py**，如果你在命令行中，可以将此项目作为工作目录，执行：

```python
python3 Mute_remove/removeMute.py
```

### （三）分割片段

> 将音频切割成 30s 长的片段，为了便于后续的使用，会改变切割后音频的命名。例如对于一个名称为 **a.wav** 的 **粤剧**，设将其分为 100 个片段（如果最后一个片段不足指定长度会舍弃），分割后的各个片段的名称会是 **yueju.a.00000.wav** 到 **yueju.a.00099.wav**，分别是 **类别.文件名.片段序号.wav**。

1. 上一步得到的文件存放在 **Audios/slience_remove** 中，找到 **Spliter/cut_audio** 文件，其中 **main** 中含有两个参数，分别是 **wav_dir** 和 **output_dir**，将它们分别改成  **Audios/slience_remove** 和 **Audios/audio_cut**，也就是去除静音后的音频所在的位置和切分后的音频片段存放的位置，将 **category** 改为操作的剧种的名称拼音，如 **粤剧(yueju)**；
2. 执行 python 文件 **Spliter/cut_audio.py**，如果你在命令行中，可以将此项目作为工作目录，执行：

```python
python3 Spliter/cut_audio.py
```

### （四）人声和伴奏的分离

> 使用到的分离工具是 _spleeter_，需要事先安装，已经安装好的，不必再次安装。如果需要安装，参见 Github 的 [spleeter](https://github.com/deezer/spleeter) 中的 "Quick Start(快速开始)" 部分的**前两步**即可。第三步和第四步是测试安装是否成功，暂不需要。
>
> 使用到的 spleeter 命令格式是：
>
> `spleeter -p 分轨数量 -o 输出目录 音频文件路径`
>
> 分轨数量可以选择：
>
> * `spleeter:2stems`：默认，2 个轨道，人声和伴奏
> * `spleeter:4stems`：4 个轨道，人声 + 鼓点 + 贝斯 + 其他
> * `spleeter:5stems`：5 个轨道，人声 + 鼓点 + 贝斯 + 钢琴 + 其他
>
> 我们需要用到的是两个轨道。
>
> **需要注意的是，当前工作目录对程序是否下载预训练模型至关重要，需要确保当前工作目录下含有 `pretrained_models` 这个文件夹，并且这个文件夹下含有模型文件，这样 spleeter 不会重复下载模型**

1. 根据情况选择是否安装 spleeter，如果在虚拟环境中安装了 spleeter，请激活虚拟环境再执行 python 代码

2. 在 Github spleeter 项目右边的 “Releases - +1 releases” 中下载我们需要用到的 `2stems.tar.gz`，放置在 `DramaGo/Spleeter/pretrained_models/2stems` 下并解压

3. 在命令行中 `cd` 到 `Spleeter` 这个文件夹：`cd Spleeter`。

4. 对 `separate.py` 文件的两个变量 `wav_dir` 和 `output_dir` 进行更改，分别用待分离的所有 wav 所在的文件夹，和结果输出到的文件夹表示
5. 执行 `separate.py`：

```python
python ./separate.py
```

6. 事先创建两个文件夹，分别用来保存所有的伴奏和所有的人声；
7. 进行人声和伴奏的分别提取和合并，在 `extract_merge.py` 中更改三个参数，`dir_path` 改为上一步 spleeter 后的保存的文件夹，它下面有很多子目录，每首曲子就是一个子目录，每个子目录下分别是 `accompaniment.wav` 和 `vocals.wav`；`accompany_dir` 改为**事先创建**的保存所有的伴奏的文件夹；`vocals_dir` 改为**事先创建**的保存所有人声的文件夹；执行  `extract_merge.py`：

```
python ./extract_merge.py
```

8. 将保存所有伴奏的文件夹更名为 `粤剧批次?伴奏`，将保存所有人声的文件夹更名为 `粤剧批次?人声`，其中 `?` 表示你所处理的批次，之后将两个文件夹压缩即可
9. 经过上一步操作，spleeter 产生结果的目录经过文件的移动均变成了空文件夹，可以将其删除







