from flask import Flask, render_template, redirect, request, url_for
from toptrack import *

app = Flask(__name__)
 
@app.route('/', methods=['POST','GET'])
def main2():
    if request.method == 'POST':
        return redirect(url_for('test'))
    return render_template('home.html')
 
@app.route('/test', methods=['POST','GET'])
def test():
    return render_template('test_test.html',toptrack_results = toptrack_results)
 
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
