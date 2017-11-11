import requests
from lxml import etree
def login(zjh,mm,v_yzm,cookie):
    Url= "http://jw.bhu.edu.cn/loginAction.do"
    d={
        "zjh1":"",
        "tips":"",
        "lx":"",
        "evalue":"",
        "eflag":"",
        "fs":"",
        "dzslh":"",
        "zjh":zjh,
        "mm":mm,
        "v_yzm":v_yzm
    }
    html=requests.post(Url,data=d,cookies=cookie)
    text = html.text
    return text

def search(zxxnxq,zxXaq,zxJxl,zxZc,zxJc,zxxq,cookie):
    url="http://jw.bhu.edu.cn/xszxcxAction.do?oper=xszxcx_lb"
    requests.get(url,cookies=cookie)
    ds={
        "zxxnxq": zxxnxq,    #学期  学年 春2-1 秋1-1
        "zxXaq": zxXaq,                  #滨海2 松山1
        "zxJxl": zxJxl,                #滨海{201 - 205}单选 203工科楼 204文科楼 松山{1 - 24}
        "zxZc": zxZc,                   #第几周{1 - 24} 英文逗号连接
        "zxJc": zxJc,                 #节次{1 - 13} 英文逗号连接
        "zxxq": zxxq,                   #星期{1 - 7} 英文逗号连接
        "pageSize": "300",            #页面大小 上限 300
        "page": "1",
        "currentPage": "1",
        "pageNo": "1"
    }
    dataUrl="http://jw.bhu.edu.cn/xszxcxAction.do?oper=tjcx"
    html=requests.post(dataUrl,data=ds,cookies=cookie)
    text=html.text
    page = etree.HTML(text)
    table = page.xpath('//tbody/tr/td')
    class_id=[]
    text=[]
    for td in table:
        class_id.append(td.text)
    for i in range(len(class_id)):
        if i%7==3:
            text.append(class_id[i].strip())
    return text
