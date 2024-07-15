# 短语背诵小程序

## 介绍
这是一个用于英语短语背诵和测试的桌面应用程序。你可以添加新的词汇，进行随机测试，并查看词汇的统计信息。

## 功能
- 添加新的中英文词组
- 随机测试你的英语词汇
- 查看词汇的测试统计信息
- 支持选择不同的词汇库

## 安装步骤

### 1. 克隆项目

```bash
git clone <你的仓库地址>
cd vocab_test
```

### 2. 安装依赖
运行以下命令以安装所需的Python包：

```bash
pip install -r requirements.txt
```

### 3. 运行安装脚本
运行 install.py 脚本以安装依赖并选择是否创建可执行文件：

```bash
python install.py
```

在提示时输入 y 以创建可执行文件，或输入 n 以跳过此步骤。

## 使用方法
### 1. 启动应用程序
如果你创建了可执行文件，运行`dist/main.exe ` 启动应用程序。

如果没有创建可执行文件，运行以下命令启动应用程序：

```bash
python main.py
```

### 2. 添加新词汇
在主界面中输入新的中文和对应的英文词组，然后点击“添加词汇”按钮。

### 3. 随机测试
点击“开始随机测试”按钮进行随机测试。输入英文翻译并提交答案。

### 4. 查看统计信息
点击“查看统计信息”按钮查看每个词组的测试次数和错误率。

### 5. 切换词汇库
在主界面使用下拉菜单选择不同的词汇库，或新建一个词汇库。


# Phrase Memorization Mini-Program

## Introduction

This is a desktop application for memorizing and testing English phrases. You can add new vocabulary, perform random tests, and view vocabulary statistics

## Features
- Add new Chinese and English phrases
- Randomly test your English vocabulary
- View statistics of vocabulary tests
- Support selecting different vocabulary librarie

## Installation Steps

### 1. Clone

```bash
git clone <your repository URL>
cd vocab_test
```

### 2. Install dependencies
Run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Run the installation script
Run the `install.py` script to install dependencies and choose whether to create an executable file:
```bash
python install.py
```

Enter y when prompted to create an executable file, or enter n to skip this step.


## Usage
### 1. Start the application
If you created an executable file, run `dist/main.exe` to start the application.

If you did not create an executable file, run the following command to start the application:

```bash
python main.py
```

### 2. Add new vocabulary
Enter new Chinese and corresponding English phrases in the main interface, then click the "Add Vocabulary" button.

### 3. Random test
Click the "Start Random Test" button to perform a random test. Enter the English translation and submit your answer.

### 4. View statistics
Click the "View Statistics" button to see the test count and error rate for each phrase.

### 5. Switch vocabulary library
Use the dropdown menu in the main interface to select a different vocabulary library or create a new one.
