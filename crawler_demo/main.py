import time
start=time.time()

import requests
from pyquery import PyQuery

#确定目标
u='https://pvp.qq.com/web201605/herolist.shtml'

#发送请求
html=requests.get(u).content
# print('状态码:{}'.format(response.status_code))

# if response.status_code != 200:
#     pass
# else:
#     print("服务器连接正常")

doc=PyQuery(html)
items=doc('.herolist>li').items()
# print(items)
for item in items:
    url=item.find('img').attr('src')
    # print(url)
    urls='http:'+url
    name=item.find('a').text()
    # print(name)
    url_content=requests.get(urls).content

    #保存数据
    with open('C:/data_work/studyWork/py-study/crawler_demo/download/'+name+'.jpg','wb') as file:
        file.write(url_content)
        print("正在下载%s......%s"%(name,urls))

print('下载完毕')

end=time.time()
print('图片爬取共计耗时{:.2f}秒'.format(end-start))