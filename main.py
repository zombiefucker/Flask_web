#encoding:utf-8

from flask import Flask,url_for,render_template,request,redirect,session
from exts import db
from models import Users,Articles
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)



#db.create_all()

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users.query.filter(Users.username == username,Users.password == password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('Index'))
            #session.permenent
        else:
            return '用户名或者密码错误'

@app.route('/regist',methods=['GET','POST'])
def Regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2 ')

        user = Users.query.filter(Users.username == username).first()
        if user:
            return u'该用户名已经被注册'
        else:
            user = Users(username=username,password=password1)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('Login'))

@app.route('/release',methods=['GET','POST'])
def Release():
    if request.method == 'GET':
        return render_template('Release.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        article = Articles(title=title,content=content)

        user_id = session.get('user_id')
        user = Users.query.filter(Users.id == user_id).first()
        article.author = user

        db.session.add(article)
        db.session.commit()
        return redirect(url_for('Index'))
        pass




if __name__ == '__main__':
    app.run(debug=True)
