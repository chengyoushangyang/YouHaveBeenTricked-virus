<h1 align="center">"你被骗了"病毒</h1>
<p align="center">
  <img src="https://img.shields.io/badge/python->=3.12-blue" alt="python"/>
  <img src="https://img.shields.io/badge/codesize-342KB-green" alt="codesize"/>
  <img src="https://img.shields.io/badge/language-python+batch-brightgreen" alt="language"/>
  <img src="https://img.shields.io/badge/license-Apache2.0-yellow" alt="last license"/>
  <img src="https://img.shields.io/badge/author-chengyoushangyang-orange" alt="author"/>
  <img src="https://img.shields.io/badge/作者(简体中文)-诚由上阳-orange" alt="作者(简体中文)"/>
</p>
<hr>

## 简单介绍
### YouHaveBeenTricked-virus是一个关于rickroll的恶搞病毒,通过各种弹窗以实现恶搞的效果
### 注意:该病毒不会对系统进行实质性的破坏,恶搞程序并非恶意病毒,如果因为其他原因导致系统出现损坏,本作者并不负责
### 如果出现BUG,可以提交[Issue](https://github.com/chengyoushangyang/YouHaveBeenTricked-virus/issues)

## 病毒效果
### 该病毒会产生如下效果:
- 篡改壁纸
- 修改音量
- 打开一个rickrock的网页
- 打开一个全是"你被骗了"文本的文本文件
- 大量弹窗
- 鼠标随机移动
- 打开几个cmd(命令提示符)
- 在桌面上生成50个写着"你被骗了"的文本文件
- 打开一个bat脚本(内容就是以树形结构显示C盘下所有文件及文件夹,俗称"扫盘")

## 使用

### 基本需求
#### 使用前先确定有没有满足下列需求:
- 操作系统为官方完整版的windows10及以上系统
- 操作系统中有notepad,cmd这些系统自带软件
- 操作系统中有edge,chrome等能浏览现代网页的浏览器(浏览器需要能正常访问bilibili)
- 操作系统已经联网,可访问Internet
#### 只有满足全部才能进行[简单运行](https://github.com/chengyoushangyang/YouHaveBeenTricked-virus#%E7%AE%80%E5%8D%95%E8%BF%90%E8%A1%8C)

### 简单运行
只需要下载[exe文件](https://github.com/chengyoushangyang/YouHaveBeenTricked-virus/releases/tag/rickroll),双击打开就行了

### 运行源码
#### 先安装[python](https://python.org/)3.12及以上版本(推荐python3.12)
#### (可选,推荐)安装visual studio code或其他IDE

#### 把项目clone到本地

#### 运行这些命令以安装第三方库:
```
pip install subprocess
```
```
pip install pathlib
```
```
pip install pyautogui
```
```
pip install pyvolume
```

#### 运行main.py
```
python main.py
```

## 自定义

### 由于本源码较烂,想要自定义只能自己往上面加代码

### 您可以查看os库的官方文档以添加内容
