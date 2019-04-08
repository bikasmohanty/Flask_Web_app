from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def root():
    data= [1,2,3,4]
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(port=5200, debug=True)
