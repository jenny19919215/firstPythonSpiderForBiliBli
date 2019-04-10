from bs4 import BeautifulSoup
import requests
import json
import pprint
import math
import sys





if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    target = 'https://api.bilibili.com/x/v2/reply'
    for i in range(19):
        video_url_params = {
            'jsonp': 'jsonp',
            'pn': i+1,  # 页数从0开始的所以要+1
            'type': '1',
            'oid': 20218451,  # 视频id
            'sort': '0',
        }

        repliesall = requests.get(target, params=video_url_params,headers=headers).json()['data']['replies']
        if repliesall is not None:
            print(i);
            for replies in repliesall:
                # 循环获得次视频下面的评论
                content = replies['content']['message']
                # 返回评论内容
                with open(r'd:\wb.txt', 'a', encoding='utf-8') as f:
                    f.write(content + '\n')



        #print(repliesall)
    #json_text = json.loads(req.text)
    #print(json_text)
    #commentsNum = json_text["data"]["page"]["count"]
    #print(commentsNum)
   # bf = BeautifulSoup(html,'html.parser')
   # texts = bf.find_all('p', class_='text')
   # bf.find_all()
    #print(texts)
    #print(bf.p)