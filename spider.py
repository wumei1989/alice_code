import requests
from bs4 import BeautifulSoup

url = "https://baike.baidu.com/item/%E5%AE%89%E4%B8%9C%E5%B0%BC%E5%A5%A5%C2%B7%E5%8F%A4%E7%89%B9%E9%9B%B7%E6%96%AF/3939809?fr=api_baidu_opex_festival"  # 你要爬取的网址

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding  # 自动识别编码

soup = BeautifulSoup(response.text, "html.parser")

# 获取网页标题
title = soup.title.string
print("网页标题:", title)

# 获取所有链接
for link in soup.find_all("a"):
    href = link.get("href")
    print(href)