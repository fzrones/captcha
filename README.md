### 安装依赖

```shell
pip3 install -r requirements.txt
pip3 install model
```

### 解压数据

将extracted_letter_images.zip和generated_captcha_images.zip解压到当前文件夹下，其中包含验证码10000张和拆分后的单个字母数张

* generated_captcha_images.zip 10000张验证码数据
* extracted_letter_images.zip 拆分后的单个字母



如果不想下载数据，可以直接解压数据后进行以下操作，如果想手动下载数据，请创建generated_captcha_images和extracted_letter_images文件夹后，运行download_captchas.py后，再运行captchas_split.py进行图片分割

### 模型训练

```shell
python3 train_model.py
```

训练成功后，成功率为99.996%，模型已上传

### 图片预测

```shell
python3 get_captchas_label.py
```

此代码通过网上下载图片到temp目录下，然后进行图片切割，将切割后的图片以1.jpeg～4.jpeg的形式保存到当前目录下，再依次进行送入模型，通过模型训练后，输出预测值，并拼接出验证码。

### 模型介绍

* 第一层 
* 卷积层  5*5卷积核  20个  输入shape为20\*20\*1的灰度图像
* 激活函数为relu 
* maxpool 步长为2，大小为2的池化层
* 第二层
* 卷积层  5*5卷积核  50个
* 激活函数为relu
* maxpool 步长为2，大小为2的池化层
* 第三层
* 全链接层 500个
* 激活函数为relu
* 第四层
* 全链接层 10个 即输出的标签
* 激活函数softmax

