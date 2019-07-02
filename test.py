from flask import Flask,request,url_for,render_template,redirect
from models import User

app = Flask(__name__)
USERS = {
    1:{'name':'bob','age':28,'text':'aaaaaaaaaaa'},
    2:{'name':'john','age':18,'text':'bbbbbbbbbbb'},
    3:{'name':'car','age':23,'text':'cccccccccccc'}
}

@app.route('/detail/<int:uid>',methods=['GET','POST'])
def detail(uid):
    info = USERS.get(uid) # 等同于info = USERS[uid]
    return render_template('detail.html',info=info)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # request.query_string
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            return redirect('http://www.luffycity.com')
        else:
            return render_template('login.html',error='auth fail:user or password fault')

@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html',user_dict=USERS)



'''
@app.route('/')
def hello_world():
    content = 'fucking hello world'
    return render_template('index.html',content=content)

@app.route('/users')
def user_index():
    user = User(1,'wucaitian')
    return render_template('user_index.html',user=user)

@app.route('/users/<username>',methods=['GET','POST'])
def hello_users(username): 
    return 'hello user:'+username

@app.route('/user_id')
def user_id():
    id = request.args.get('id')
    user = None
    if int(id) == 1:
        user = User(1,'wucaitian')
    
    return render_template('user_id.html',user=user)

@app.route('/base1')
def base1():
    return render_template('1.html')

@app.route('/base2')
def base2():
    return render_template('2.html')


#反向路由，路由构造
@app.route('/urlfor_userid')
def urlforuserid():
    URLFOR = url_for('userid')
    print(URLFOR)
    return 'url is :'+URLFOR

'''

if __name__ == "__main__":
    app.run()