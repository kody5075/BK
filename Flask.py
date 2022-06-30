!pip install flask-ngrok
!pip install flask
from flask import Flask, flash, request, redirect, render_template,session
import ipfshttpclient
import os
app = Flask(__name__)

path=""
@app.route('/', methods=['GET', 'POST'])
def Home():
    return "This is Home"


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # 獲取圖片文件
    if request.method == 'POST':
        file = request.files.get('file')

        # 定義一個圖片存放的位置存放在static /img下面
        path = "C:/Users/A0989/OneDrive/桌面/區塊/"

        # 圖片名稱
        global file_name
        file_name = file.filename

        # 圖片path和名稱組成圖片的保存路徑
        file_path = path + file_name

        # 保存圖片
        file.save(file_path)
        return render_template('upload_ok.html')
        #return "上傳成功"
    # 返回圖片地址
    os.chdir("C:/Users/A0989/OneDrive/桌面/區塊/")
    return render_template('upload.html')
@app.route('/ipfs')
def ipfs():
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001') 
    os.chdir("C:/Users/A0989/OneDrive/桌面/區塊/")
    print("file_name:",file_name)
    res = client.add(file_name)
    
    return render_template('test.html',title = res)
    # 請將上面res印出內容中找出的HASH值貼到下一行的cat函數需要的字串中
    #print("IPFS file content=", client.cat('QmcLzL52wdigx4ViFvM1QqD9J4jvErPUnV6BVLWRKRxFJY'))
if __name__ == '__main__':
    app.run()