import requests
from flask import *
import method

global cookie
cookie=None
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/code.jpg')
def imagr():
    imageUrl = "http://jw.bhu.edu.cn/validateCodeAction.do?random=0.8694466282020366"
    r=requests.get(imageUrl)
    resp = Response(r, mimetype="image/jpeg")
    global cookie
    cookie=r.cookies
    return resp

@app.route('/login',methods=['GET', 'POST'])
def login():
    global cookie
    if request.method == 'POST' and cookie!=None:
        zjh=request.form.get('zjh','default value')
        mm=request.form.get('mm','default value')
        v_yzm=request.form.get('v_yzm','default value')
        text= method.login(zjh, mm, v_yzm, cookie)
        if "请您重新输入" in text:
            return render_template("login.html",error="您输入的信息有误,请重新输入")
        else:
            return render_template("index.html")

    else:
        return render_template("login.html")

@app.route('/SpryAssets/SpryValidationSelect.js')
def js():
    return send_file("templates/SpryAssets/SpryValidationSelect.js")

@app.route('/SpryAssets/SpryValidationSelect.css')
def css():
    return send_file("templates/SpryAssets/SpryValidationSelect.css")

@app.route('/SpryAssets/SpryValidationTextField.js')
def tjs():
    return send_file("templates/SpryAssets/SpryValidationTextField.js")

@app.route('/SpryAssets/SpryValidationTextField.css')
def tcss():
    return send_file("templates/SpryAssets/SpryValidationTextField.css")

@app.route('/search',methods=['GET', 'POST'])
def search():
    global cookie
    if request.method == 'POST' and cookie!=None:
        #print(cookie.get("JSESSIONID"))
        if cookie.get("JSESSIONID")=="":
             return render_template("login.html")
        zxxnxq=request.form.get('zxxnxq','default value')
        zxXaq=request.form.get('zxXaq','default value')
        zxJxl=request.form.get('zxJxl','default value')
        zxZc=request.form.get('zxZc','default value')
        zxJc=request.form.get('zxJc','default value')
        zxxq=request.form.get('zxxq','default value')
        text= method.search(zxxnxq, zxXaq, zxJxl, zxZc, zxJc, zxxq, cookie)
        if len(text)>0:
            return render_template("result.html",texts=text)
        else:
            return render_template("index.html",notfind="没有查询到结果，请稍后再试")

    else:
        return render_template("login.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=8080)
