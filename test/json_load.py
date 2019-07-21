import json
with open(r"C:\Users\mi\PycharmProjects\mySpider\mySpider\music.txt","r") as f:


    data = json.load(f)    #里面必须是一个字典 [,,,,,,] 在后面手动添加一个"]"吧

for i in range(0,len(data)):
    print(data[i])
