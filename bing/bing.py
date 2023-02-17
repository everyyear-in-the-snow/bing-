import requests

if __name__ == "__main__":
    # 添加代理
    # proxies = {
    #     'https': 'https://127.0.0.1:    ',
    #     'http': 'http://127.0.0.1:    '
    # }

    # 指定url
    url = 'https://www.bing.com/search?'
    key = input("输入关键字：")
    para = {
        'q' : key
    }

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46'
    }

    # 发起请求
    response = requests.get(url=url,params=para, headers=headers, timeout=6)
    # get方法回返回一个响应对象
    # 获取响应数据
    response.encoding = response.apparent_encoding

    page = response.text

    # text返回的是字符串形式的响应数据
    print(page)

    # 持久化存储
    f = open('bing.html','w', encoding='utf-8')
    f.write(page)
    f.close()

    # with open('google.html', 'w', encoding='utf-8-sig') as fp:
    #     fp.write(page)
    print('finish!')