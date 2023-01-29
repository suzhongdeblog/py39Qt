> 标题:Python Qt 图形界面编程 - PySide2 PyQt5 PyQt PySide（应用桌面开发）
> 视频地址:https://www.bilibili.com/video/BV1kg411x7D1/?p=23&spm_id_from=pageDriver&vd_source=8819e00094cf938fc14638b7bf59509b

### 将项目打包成exe文件
1. 安装pyinstaller

```shell script
# 如果安装失败，用管理员权限安装
pip install pyinstaller 
```

2. 打包程序
       2.1 将ico图片、和代码同一文件夹
       2.2 Win+R，cmd进入管理员界面 cd切换到代码目录
   	2.3 输入打包命令

   ```shell
   pyinstaller -F -p G:\workingDirectory\pythonTag\py39Qt\ChengLin\utils v2.py
   ```

   ​        -F 表示打包(F 大写)
   ​        -w 取消控制台显示(w 小写)
   ​        -i 有错误也继续执行(i 小写)
   ​        ico图片路径（绝对路径）
   ​        最后是代码名称
   ​    2.4 如果程序里面有图片，需要将图片复制到exe文件同一级文件夹，否则程序无法正常运行
   ​    注意：
   ​    	文件路径千万不要有中文，否则会出现一些编码方面的错误。

