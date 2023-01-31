import requests
import parsel

for page in range(1, 73):
    if page == 1:
        url = 'http://www.netbian.com/meinv/'
    else:
        url = f'http://www.netbian.com/meinv/index_{page}.htm'
    # 1. 发送请求
    print(f'===========================================正在爬取第{page}页内容===========================================')
    response = requests.get(url)
    # 乱码
    response.encoding = 'gbk'
    # 2. 获取数据
    html_data = response.text
    # 3. 解析数据 图片链接获取到 提取出来
    selector = parsel.Selector(html_data)
    img_list = selector.css('.list img::attr(src)').getall()
    for img_url in img_list:
        # 小图片 >>> 大图片
        img_url = img_url.replace('small', '')
        # http://img.netbian.com/file/2022/0416/small0003229mRl41650038602.jpg
        img_url = img_url[:-14] + '.jpg'
        # 图片名称 提取出来
        img_name = img_url.split('/')[-1]
        # 直接获取图片二进制数据
        img_data = requests.get(img_url).content
        print(img_name)
        # 保存数据
        with open(f'img/{img_name}', mode='wb') as f:
            f.write(img_data)
