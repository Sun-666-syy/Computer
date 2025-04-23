from gevent import monkey
import csv
monkey.patch_all()
import gevent
import openpyxl
import requests
import time
import random

finishPage = 0
allList = []
page = 1


def comment(sightId, page):
    # 圆明园 url = 'https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=3580&index=1&page=1&pageSize=10&'
    # 宝塔山 url = 'https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=6172&index=1&page=1&pageSize=10&tagType=1'
    # 岳麓山 url = 'https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=9317&index=1&page=1&pageSize=10&tagType=0'
    # 北京奥林匹克公园 url = 'https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=2883&index=1&page=1&pageSize=10&tagType=0'
    # 红旗渠 url = 'https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=1630&index=1&page=1&pageSize=10&tagType=0'
    # 满洲里国门景区 url = 'https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=222&index=1&page=1&pageSize=10&tagType=0'

    url = "https://piao.qunar.com/ticket/detailLight/sightCommentList.json"
    params = {
        "sightId": str(sightId),
        "index": str(page),
        "page": str(page),
        "pageSize": "10",
        "tagType": "0",
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    }
    res = requests.get(url=url, headers=headers, params=params, timeout=1) # 等待服务器响应的最长时间为1秒
    # 判断服务器返回数据是否正确
    while res.text[1] == "r":
        res = requests.get(url=url, headers=headers, params=params, timeout=1)
    else:
        pass

    results = res.json()["data"]

    for result in results["commentList"]:
        # Check if the content is '用户未点评，系统默认好评。'
        if result["content"] != '用户未点评，系统默认好评。':
            # 评论者id
            author = result["author"]
            # 评论日期
            publishedDate = result["date"]
            # 总评分
            score = result["score"]
            # 图片数量
            # imgNum = len(result["imgs"])
            # 评论内容
            text = result["content"]
            commentList = [author, publishedDate, score, text]
            allList.append(commentList)
            print(commentList)
    # time.sleep(5)
    # time.sleep(random.randint(1, 3))


# def storage(name, reviewsList):
#     header = ['评论者ID', '评论日期', '总评分', '图片数量', '文本评论']
#     wb = openpyxl.Workbook()
#     sheet = wb.active
#     sheet.title = "commentInfo"
#     sheet.append(header)
#     for reviewList in reviewsList:
#         sheet.append(reviewList)
#     wb.save("存储/去哪儿 " + name + "'s " + 'comment.xlsx')
def storage(name, reviewsList):
    header = ['author', 'date', 'score', 'comment']
    with open(name + '评论信息.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for reviewList in reviewsList:
            writer.writerow(reviewList)

if __name__ == "__main__":
    taskList = []
    for i in range(1, 1000):
        try:
            #     task = gevent.spawn(comment,191026,i)
            #     taskList.append(task)
            # gevent.joinall(taskList)
            comment(222, i)
        except:
            pass
    storage("满洲里国门", allList)
    print(len(allList))
