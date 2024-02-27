import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#html全体を取得
soup=BeautifulSoup(res.text,'html.parser')

#print(soup)

#タグで要素取得
ele=soup.find('title')
#要素のtextコンテントを表示
print(ele.text)

#要素を結果セット(ResultSet)として取得
imgs=soup.find_all('img')
for img in imgs:
    #属性にアクセスするにはgetメソッドを使う
    print(img.get('src'))
