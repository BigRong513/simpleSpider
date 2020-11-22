# -*- coding = utf-8 -*-
# @Time : 2020/4/6 7:30
# @Author : BigRong
# @File : Spider.py
# @Software : PyCharm

import requests
import os
# 用r.status_code检查返回值（200 is correct, 404 or other is error
# 用r.text r.encoding, r.apparent_encoding r.content解析返回内容

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        #print(r.status_code)
        #print(type(r))
        #print(r.headers)
        #print(r.text)
        #print(r.encoding)
        #print(r.apparent_encoding)
        r.encoding = r.apparent_encoding

        return (r.text)
    except:
        return "产生异常"

def getJingdongContent():
    try:
        r = requests.get("https://item.jd.com/100012015134.html#crumb-wrap")
        print(r.status_code)
        print(r.encoding)
        print(r.text)
    except:
        print("爬取失败")

def getAmazonContent():
    url = "https://www.amazon.cn/dp/B00PF8JZHG/ref=sr_1_2?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E6%80%A6%E7%84%B6%E5%BF%83%E5%8A%A8&qid=1586158702&sr=8-2"
    try:
        kv = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        r = requests.get(url, headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.status_code)
        print(r.encoding)
        print(r.text)
        print(r.request.headers)
    except:
        print("爬取失败")

def searchByBaidu():
    try:
        kv_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                      "Cookie": "BAIDUID=FD2FABA8B6AF1225DDE677B2EDADDB31:FG=1; BIDUPSID=FD2FABA8B6AF1225DDE677B2EDADDB31; PSTM=1566135896; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=7; BDUSS=FRUUtKMGJKQTg1flZ0N21SeEpQdVNZSTRmOG50Zm9EUlhBaH5XcXl3VTBnTEplSVFBQUFBJCQAAAAAAAAAAAEAAABIi10A087AtNPOyKW08~bo0-MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADTzil4084peRD; H_PS_PSSID=1447_31170_21124_31187_30907_31228_30823_31085_31163_31196; sug=3; sugstore=1; ORIGIN=2; bdime=0; COOKIE_SESSION=45_0_3_9_0_1_0_0_3_1_0_0_0_0_0_0_0_0_1586164534%7C9%23240935_15_1586160460%7C5; H_PS_645EC=da31K%2B1mX2i8of1%2FuD4C%2Bn6ZCY9ZqptSbuC6QLhkPcrqoEGJg6XTUDs6ziQ"}
        kv_params = {'wd':'三上悠亚'}
        r = requests.get("http://www.baidu.com/s", headers = kv_headers, params = kv_params)
        r.encoding = "utf-8"
        # print(r.status_code)
        # print(r.request.url)
        # print(r.request.headers)
        print(r.text)
    except:
        print("爬取失败")

def searchBy360():
    try:
        #kv_headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        kv_params = {'q':'Python'}
        r = requests.get("http://www.so.com/s", params = kv_params)
        r.encoding = r.apparent_encoding
        print(r.status_code)
        print(r.request.url)
        #print(r.request.headers)
        print(r.text)
    except:
        print("爬取失败")

def getPicture():
    url  = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
    root = "./pic/"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            print(r.status_code)
            with open(path,'wb') as f:
                f.write(r.content)
            f.close()
            print("文件保存成功")
        else:
            print("文件已经存在")
    except:
        print("爬取失败")

def main():

    #print(getHTMLText("http://www.baidu.com")) #获取baidu html
    getJingdongContent()   #爬取京东
    #getAmazonContent()     #爬取Amazon
    # searchByBaidu()        #用Baidu搜索关键词
    #searchBy360()          # 用360搜索关键词
    #getPicture()            #爬取图片


if __name__ == "__main__":
    main()