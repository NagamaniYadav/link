from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def register():
    return render_template('login.html')

@app.route('/welcom', methods=['post'])
def welcom():
    login=request.form
    p=login['pwd']
    cp=login['cpwd']
    if(p==cp):
        name=login['uname']
        return render_template('welcome.html',uname=name,email=login['email'],Password=login['pwd'])
    else:
        return "Error "


if __name__ == "__main__":
    app.run()

