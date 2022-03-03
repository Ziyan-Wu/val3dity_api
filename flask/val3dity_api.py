import json
import os
import subprocess
import time
import uuid


from flask import Flask, render_template, redirect
from flask import request
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.env = 'development'
app.debug = True

# @app.route("/", methods=['POST', 'GET'])
# def root():
#     if request.method == 'POST':
#         request_data = request.get_json()
#         # print(request_data)
#         language = request_data['language']
#         print(language)
#         # return "{}".format(language)
#         s = '''
#             <form action="" method="get">
#                 <p><input type="text" placeholder="type username"></p>
#                 <p><input type="text" placeholder="type password"></p>
#                 <p><input type="submit" value="submit"></p>
#             </form>
#             '''
#         # print(s)
#         return s
#         # return language
#     return "<p>Welcome to the val3dity server!</p>"


@app.route('/validate', methods=['POST', 'GET'])
def com():
    if request.method == 'POST':
        os.chdir('../val3dity_exe') # go to path of val3dity.exe

        request_data = request.get_json()
        # path = request_data['path']
        # print(path)
        # save it as a file ----- temporal direct-- request
        cmd = []
        cmd.append("./val3dity.exe")
        # cmd.append('D:/data/cityjson/cube10.json')
        cmd.append(request_data)
        op = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = (op.communicate()[0]).decode('UTF-8')
        return result
    else:
        return 'this is /validate GET method\n'



if __name__ == '__main__':
    app.run()
