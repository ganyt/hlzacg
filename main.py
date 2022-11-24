import json
import os

def path_exists_make(path):#创建文件夹
    # path: 需要判断的路径
 
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
for line in open("./touchod.json"):
    #JSON文件不是标准的JSON，但是一行一行读就行
    jsonstr = json.loads(line)
    url = jsonstr["url"]
    path = jsonstr["filepath"]
    nfile = jsonstr["filename"]
    filepath = "/disk/download"+path
    path_exists_make(filepath)
    #download(filepath,nfile,url)
    #下载方法自行实现