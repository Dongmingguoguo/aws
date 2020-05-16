from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, redirect
from Myflask.strUtil import Pic_str
from Myflask.dbconnection import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Myflask.postdbconnection import User2
from Myflask.dbComment import Comment
import datetime
import os as os
import json
from datetime import datetime


app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])
engine = create_engine('mysql+pymysql://root:994410@localhost:3306/books')
Session = sessionmaker(bind=engine)
session = Session()
loadsource_userinfo = session.query(User.id, User.username, User.password).all()
loadsource = session.query(User2.title, User2.name, User2.depart, User2.time).all()
load_len = len(loadsource)


def acquire_name(data):
    title = data
    return title



@app.route('/homepage')
def beigin():

    return render_template('prac/Bootstrap.html')

@app.route('/nihao')
def nihaos(data):
    return render_template(data);


@app.route('/asddas')
def temp_prod():
    str = "hello"
    li = [1, 2, 3, 4]
    return render_template('prac/justry.html', str=str, li=li[1], haha=li[2])


@app.route('/ad')
def upload_test():
    return render_template('prac/prac2.html')


@app.route('/loadpr')
def load_data():
    return jsonify(result=loadsource[0][1])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/debug_tmplate')
def debug_template():
    return render_template('prac/template4each.html')


@app.route('/post', methods=['GET', 'POST'])
def post():
    t_db = datetime.now()
    t_db2 = str(t_db)
    t_db2 = t_db.strftime("%Y-%m-%d %H:%M:%S")
    usertitle = request.form.get('title')
    userdepart = request.form.get('depart')
    username = request.form.get('name')
    content = request.form.get('pcontent')
    filename = '/Users/dongmintian994410/PycharmProjects/FinalProject/Myflask/static/prod/'+t_db2+".html"
    filename2 = str(filename)
    print(filename2)
    q = render_template('prac/template4each.html', title=usertitle, content=content)
    ff = open(filename, 'w')
    ff.write(q)
    ff.close
    urladd = '/static/prod/'+t_db2+'.html'
    ed_title = User2(title=usertitle, name=username, depart=userdepart, ctent=content, time=t_db2, url=urladd)
    session.add(ed_title)
    session.commit()
    session.flush()
    return redirect('homepage')

@app.route('/')
def login2():
    return render_template('/login.html')


@app.route('/logout')
def logout():
    return render_template('/login.html')


@app.route('/logindas', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'login' in request.form and 'password' in request.form:
        username = request.form.get('login')
        password = request.form.get('password')
        if session.query(User).filter(User.username == username).all() and session.query(User).filter(User.password == password).all():
            return render_template('prac/Bootstrap.html', userID=username)
        else:
            return redirect('/')


@app.route('/register_db', methods=['GET', 'POST'])
def register2():
    if request.method == 'POST' and 'user-name' in request.form and 'password' in request.form:
        username = request.form.get('user-name')
        password = request.form.get('password')
        repss = request.form.get('repeat-password')
        email = request.form.get('email')
        q = session.query(User).filter(User.username == username).all()
        print(len(q))
        print(password)
        print(repss)

        if password == repss and len(q) == 0:
            new_usr = User(username=username, password=password, email=email)
            session.add(new_usr)
            session.commit()
            session.flush()
            print('I am here')
            return redirect('/')
        else:
            return render_template('register.html', status='Repeat password')



@app.route('/find')
def find_page():
    return render_template('find.html')


@app.route('/template4each')
def template4each():
    return render_template('prac/template4each.html')


# 上传文件
@app.route('/postprac', methods=['GET', 'POST'])
def test():
    clicked = None
    if request.method == "POST":
        clicked = request.json['data']
        return render_template('loadprac.html')


@app.route('/postpage')
def postpage():
    return render_template('prac/prac2.html')


@app.route('/up_photo', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        print
        fname
        ext = fname.rsplit('.', 1)[1]
        new_filename = Pic_str().create_uuid() + '.' + ext
        f.save(os.path.join(file_dir, new_filename))

        return jsonify({"success": 0, "msg": "上传成功"})
        return jsonify({"error": 1001, "msg": "上传失败"})


@app.route('/data_deliver', methods=['POST', 'GET'])
def data_deliver():
    resource = session.query(User2.title, User2.name, User2.depart, User2.time, User2.url).all()
    return json.dumps(resource)



@app.route('/bootstrap')
def bootstrap():
    return render_template('prac/Bootstrap.html')

@app.route('/boot2')
def bootstrap2():
    return render_template('prod/nihao.html')


@app.route('/prod_temp')
def prod_temp(data):
    rec_data = data
    return rec_data

@app.route('/admin')
def admin():

    return render_template('admin.html')



@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/add')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=loadsource[0][1])


@app.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('upload', filename)):
            return send_from_directory('upload', filename, as_attachment=True)
        pass


# show photo·
@app.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)
