import requests
import json
from bs4 import BeautifulSoup

### 订阅链接
subscribe_url = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxNzM5NDkzNg==&action=getalbum&album_id=1618004719539437574&scene=173&subscene=10000&sessionid=0&enterid=1632961928&from_msgid=2247529045&from_itemidx=1&count=3&nolastread=1#wechat_redirect"

### 存储要下载的url链接，其实就是微信公众号链接
link_urls = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

idx = 0


def download_url():
    response = requests.get(url=subscribe_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    first_li = soup.find_all('li')[0]
    print(first_li.get('data-title'))
    link_urls.append(first_li.get('data-link'))
    begin_msgid = first_li.get('data-msgid')
    begin_itemidx = first_li.get('data-itemidx')
    ## 土豆微信公众号表情json接口 ###
    url = "https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzAxNzM5NDkzNg==&album_id=1618004719539437574&count=10&" \
          "begin_msgid={}&begin_itemidx={}" \
          "&uin=&key=&pass_ticket=&wxtoken=&devicetype=&clientversion=&__biz=MzAxNzM5NDkzNg%3D%3D&appmsg_token=&x5=0&f=json"
    while True:
        response = requests.get(url=url.format(begin_msgid, begin_itemidx), headers=headers)
        rec_json = json.loads(response.text)
        if 'article_list' not in rec_json['getalbum_resp']:
            break
        article_list = rec_json['getalbum_resp']['article_list']
        for article in article_list:
            print(article['title'])
            link_urls.append(article['url'])
        begin_msgid = article_list[-1]['msgid']
        begin_itemidx = article_list[-1]['itemidx']
    print(len(link_urls))


def download_image(image_url):
    global idx
    # image_url = link_urls[0]
    response = requests.get(url=image_url, headers=headers)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find_all('img'))
    for image_ in soup.find_all('img'):
        gif_url = image_.get('data-src')
        # print(gif_url)
        if gif_url != None and gif_url.find('gif', -3) != -1:
            print(gif_url)
            response = requests.get(url=gif_url, headers=headers)
            image_content = response.content
            with open('cat/{}.gif'.format(idx), 'wb+') as f:
                f.write(image_content)
                idx += 1


def main():
    download_url()
    for url in link_urls:
        download_image(url)
    print('finish!!!!!')


if __name__ == '__main__':
    main()
