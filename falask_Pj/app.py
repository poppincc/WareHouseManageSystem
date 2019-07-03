from datetime import timedelta
from flask import Flask, url_for, render_template, request, redirect, session
from model import User
from db import *
import config
import os

from templates.form import MyForm

app = Flask(__name__)

# 静态文件缓存时间设置
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.config.from_object(config)
app.config['SECRET_KEY'] = os.urandom(24)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。


# app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7) #设置session的保存时间。

# 首页 根据passwd里面的Authority展示对应的主页
# 1-管理员
# 2-老师
# 3-财务人员
# 4-学生
# @app.route('/')
# def index():
#     return render_template('index.html')



# bill学生主页
@app.route('/stu_index')
def index_stu():
    return render_template('stu_index.html')

# bill教师主页
@app.route('/teacher_index')
def index_teacher():
    return render_template('teacher_index.html')

# Bill 老师添加课程信息
@app.route('/add_class', methods=['GET', 'POST'])
def add_class():
    print("添加课程界面", session['username'])
    if request.method == "POST":
        user = User()
        user.name = session['username']
        course_id = request.form["course_id"]
        course_name = request.form["course_name"]
        teacher_name = request.form["teacher_name"]
        print("执行添加收支的课程是", course_name)
        print("教师名称", teacher_name)
        if add_course(course_id, course_name, teacher_name):
            print("课程增加成功")
            message = "课程增加成功"
            return render_template('teacher_addclass.html', message=message)
        else:
            message = "课程增加失败,请重新填写"
            print("课程增加失败,请重新填写")
            return render_template('teacher_addclass.html', message=message)
            #   session.pop(user.name)
    else:
        return render_template('teacher_addclass.html')

# lh 老师 查看班级信息
@app.route('/show_class', methods=['GET', 'POST'])
def show_class():
    # print("课程查询界面", session['username'])
    allclass = show_allclass()
    print(allclass)
    return render_template('teacher_showclass.html', allclass=allclass)

# lh 老师 查看选课信息
@app.route('/show_csselect', methods=['GET', 'POST'])
def show_allcourseofselect():
    # print("课程查询界面", session['username'])
    allselected = show_allcourseselected()
    print(allselected)
    return render_template('teacher_showcsselected.html', allselected=allselected)

# lh 老师 查看选课信息
@app.route('/show_register', methods=['GET', 'POST'])
def show_register():
    # print("课程查询界面", session['username'])
    allregister = show_allregister()
    print(allregister)
    return render_template('teacher_showregister.html', allregister=allregister)


# bill财务人员主页
@app.route('/account_index')
def index_account():
    return render_template('account_index.html')


# bill管理员
@app.route('/admin')
def index_adm():
    return render_template('adm_index.html')


# bill登陆
@app.route('/login/', methods=['GET', 'POST'])
def user_login():
    print(session)
    if session:
        username = session['username']
        # session.pop('username')
        print('session 不为空 ', username)
        print("开始调用函数获取用户类型")
        Authority = login_Authority(username)
        print("Authority", Authority)
        if Authority == '111111':
            print("admin login!")
            return redirect(url_for('index_adm'))
            # return redirect(url_for('user_login'))
        elif Authority == 2:
            return redirect(url_for('index_teacher'))
        elif Authority == 3:
            return redirect(url_for('index_account'))
        else:
            return redirect(url_for('index_stu'))

    # print(session[0])
    if request.method == "POST":
        print(request.form)
        user = User()
        stu_id = user.id = request.form["user_id"]
        user.pwd = request.form["user_pwd"]
        Authority = login_Authority(user.id)
        print("测试Authorith 输出数字", Authority)
        print("admin login", Authority)
        # print(type(Authority))
        if loginCheck(user.id, user.pwd):
            session['username'] = user.id
            if Authority == 111111:
                print("admin login!")
                return redirect(url_for('index_adm'))
            elif Authority == 2:
                return redirect(url_for('index_teacher'))
            elif Authority == 3:
                return redirect(url_for('index_account'))
            else:
                return redirect(url_for('index_stu'))
        else:
            message = "用户名或者密码错误"
            return render_template('user_login.html', message=message)
        print("name:  pwd:", user.name, user.pwd)
        return redirect(url_for("user_login"))  # 跳到主页
    return render_template('user_login.html')


# bill退出系统
@app.route('/out', methods=['GET', 'POST'])
def out():
    session.pop('username')
    return redirect(url_for('user_login'))


# bill修改密码
@app.route('/changepassword', methods=['GET', 'POST'])
def changepassword():
    print("修改界面", session['username'])
    # sql 修改数据库中的密码
    # fun_changepassword(user)
    if request.method == "POST":
        user = User()
        user.name = session['username']
        print("需要修改的用户是", user.name)
        user.pwd = select_pwd(user.name)
        print("数据库查询到的密码是：", user.pwd)
        oldpassword = request.form["oldpassword"]
        print("需要修改的用户是", oldpassword)
        newpassword = request.form["newpassword"]
        renewpassword = request.form["renewpassword"]
        if newpassword == renewpassword:
            print("两次输入密码一致")
            print("----------------------------------------------")
        else:
            message = "两次密码不一致，请重新输入"
            print("两次密码不一致，请重新输入")
            return render_template('changepassword.html', message=message)
        # print("新密码： 旧密码：", oldpassword, user.pwd[0])
        if str(oldpassword) == str(user.pwd[0]):
            print("新旧密码一致")
            user.pwd = newpassword
            update_pwd(user.name, user.pwd)
            print("密码修改成功")
            print("密码修改成功，请推出当前界面重新登陆")
            # return 'ok'
            message = "密码修改成功，请重新登陆"
            # session.pop(user.name)
            return redirect(url_for("user_login"))  # 跳到主页
            # return render_template('user_login.html', message=message)
        else:
            message = "旧密码有误，请重新输入"
            print("旧密码有误，请重新输入")
            return render_template('changepassword.html', message=message)
            #   session.pop(user.name)
    else:
        return render_template('changepassword.html')

# lh 管理员 增加人员
@app.route('/add_account', methods=['GET', 'POST'])
def add_account():
    if request.method == "POST":
        print("增加人员: ")
        user = User()
        user.id = request.form["accountid"]
        user.name = request.form["name"]
        user.pwd = request.form["pwd"]
        user.gender = request.form["gender"]
        user.email = request.form["email"]
        user.tel = request.form["tel"]
        user.introduce = request.form["introduce"]
        user.ruletype = request.form["ruletype"]
        db_add_account(user.id, user.name, user.pwd, user.gender, user.email, user.tel, user.introduce, user.ruletype)
        add_message = "添加成功"
        return render_template('adm_add_account.html',add_message = add_message)
    return render_template('adm_add_account.html')

# lh 管理员 查看人员
@app.route('/show_account')
def show_account():
    # print("查看人员: ")
    # sql 查看人员数据库中的所有人员
    account = show_allacount()
    # print(account)
    return render_template('adm_show_account.html',account =account)

# cc 管理员 人员管理
@app.route('/person_management',methods=['GET', 'POST'])
def person_management():
    return render_template('person_management.html')

# cc 人员管理_查看人员
@app.route('/show_person',methods=['GET', 'POST'])
def show_person():
    person = show_allperson()
    print(person)
    return render_template('person_management_show.html',person =person)

# cc 人员管理_变更人员
@app.route('/add_person',methods=['GET', 'POST'])
def add_person():
    form = MyForm()
    if request.method == "POST":
    #print(form.validate_on_submit())
    #if form.validate_on_submit():
        print(form.data['status'])
        print("增加人员: ")
        user = User()
        user.name = request.form["name"]
        user.materiel = request.form["materiel"]
        user.product = request.form["product"]
        user.purchase = request.form["purchase"]
        power=111111
        cc_add_account(user.name, user.pwd,power)
        add_message = "添加成功"
        return render_template('add_person.html', add_message=add_message)
    return render_template('add_person.html',form=form)

#cc 人员管理_权限管理
@app.route('/show_person',methods=['GET', 'POST'])
def change_person():
    person = show_allperson()
    print(person)
    return render_template('person_management_show.html',person =person)

# Bill  学生签到
@app.route('/stu_register', methods=['GET', 'POST'])
def stu_register():
    print("签到界面", session['username'])
    if request.method == "POST":
        user = User()
        user.name = session['username']
        print("需要签到的用户是", user.name)
        if add_register(user.name):
            print("签到成功")
            message = "签到成功"
            return render_template('stu_register.html', message=message)
        else:
            message = "签到成功,请重新打卡"
            print("签到成功,请重新打卡")
            return render_template('stu_register.html', message=message)
            #   session.pop(user.name)
    else:
        return render_template('stu_register.html')

# lh 学生选课
@app.route('/stu_xuanke', methods=['GET', 'POST'])
def stu_xuanke():
    all_course = show_allcourse()
    stu_id = session['username']
    all_coursesed = show_allcoursesed(stu_id)
    if request.method == "POST":
        print(request.form)
        courseid = request.form["course_id"]
        dbstu_xuanke(courseid,stu_id)
    return render_template('stu_xuanke.html',all_course = all_course,all_coursesed = all_coursesed)

# Bill 财务人员 增加收支记录
@app.route('/accounting_shouzhi', methods=['GET', 'POST'])
def accounting_shouzhi():
    print("添加收支界面", session['username'])
    if request.method == "POST":
        user = User()
        user.name = session['username']
        add_type = request.form["add_type"]
        amount = request.form["add_amount"]
        print("执行添加收支的金额是", amount)
        print("执行添加收支的用户是", user.name)
        if add_shouzhi(user.name, add_type, amount):
            print("收支增加成功")
            message = "收支增加成功"
            return render_template('accounting_shouzhi.html', message=message)
        else:
            message = "收支增加失败,请重新填写"
            print("收支增加失败,请重新填写")
            return render_template('accounting_shouzhi.html', message=message)
            #   session.pop(user.name)
    else:
        return render_template('accounting_shouzhi.html')

# lh 财务 查看报表统计
@app.route('/accounting_baobiao', methods=['GET', 'POST'])
def accounting_baobiao():
    # print("课程查询界面", session['username'])
    baobiao = show_baobiao()
    baobiaoxize = show_baobiaoxize();
    print(baobiaoxize)
    return render_template('accounting_baobiao.html', baobiao=baobiao,baobiaoxize = baobiaoxize)

if __name__ == '__main__':
    app.run(debug=True)