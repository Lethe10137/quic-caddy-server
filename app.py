from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_file():
    if 'uploadfile' not in request.files:
        return {"error": "No file uploaded"}, 401

    file = request.files['uploadfile']
    file_length = len(file.read())  # 读取文件内容，计算大小

    return {"file_size": file_length}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

