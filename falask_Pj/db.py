import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="test", charset="utf8")
cur = conn.cursor()


# 登录
def loginCheck(name, pwd):
    sql = "select * from authority where personName='%s' and password='%s'" % (name, pwd)
    cur.execute(sql)
    result = cur.fetchall()
    if (len(result)) == 0:
        return False
    else:
        return True
    conn.close()


# 登录查询返回用户类型
def login_Authority(id):
    conn.ping(reconnect=True)
    sql = "select authority from  authority where personName='%s'" % (id)
    #sql = "select authority from  authority where personName='"+id+"';"
    cur.execute(sql)
    result = cur.fetchone()
    for record in result:
        return record
    conn.close()


# 登录查询返回用户密码
def select_pwd(name):
    sql = "select password from  passwd where accountingid='%s'" % (name)
    cur.execute(sql)
    result = cur.fetchall()
    for record in result:
        return record
    conn.close()


# 修改用户密码
def update_pwd(name, pwd):
    sql = "update passwd set password= '%s'  where accountingid='%s'" % (pwd, name)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 提交到数据库执行
        conn.commit()
        print("语句已经提交")
    except:
        conn.rollback()

    conn.close()


# lh 管理员 增加用户
def db_add_account(id, name, pwd, gender, email, tel, introduce, ruletype):

    sql_account = "insert into account value ('%s','%s','%s','%s','%s','%s' ) " % (id, name, gender, email,tel,introduce)
    sql_pwd = "insert into passwd value ('%s','%s',%s)" % (id, pwd, ruletype)
    print(sql_account + " " + sql_pwd)
        # 执行SQL语句
    try:
        cur.execute(sql_account)
        cur.execute(sql_pwd)
        # 提交到数据库执行
        conn.commit()
        conn.close()
    except:
        conn.rollback()

# lh 管理员 查看全部人员返回所有结果
def show_allacount():
    sql = "select * from  account "
    cur.execute(sql)
    result = cur.fetchall()
    # for record in result:
    return result
    conn.close()

# cc 管理员_人员管理_查看人员
def show_allperson():
    sql = "select * from  authority "
    #print(sql)
    cur.execute(sql)
    result = cur.fetchall()
    return result
    conn.close()

# Bill学生打卡记录
def add_register(name):
    sql = "insert into register (accountingid,type,time) values(%s,%s,now())" % (name, 1)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 提交到数据库执行
        conn.commit()
        print("语句已经提交")
        return True
        conn.close()
    except:
        conn.rollback()


# Bill 学生查看全部打卡记录返回所有结果
def show_register(name):
    sql = "select * from  register where accountingid='%s'" % (name)
    cur.execute(sql)
    result = cur.fetchall()
    # for record in result:
    return result
    conn.close()

# lh 学生查看全部课程
def show_allcourse():
    sql = "select * from  course "
    cur.execute(sql)
    result = cur.fetchall()
    # for record in result:
    return result
    conn.close()

# lh 学生查看全部已选课程
def show_allcoursesed(id):
    sql = "select course.courseid,course.coursename from courseselected ,course " \
          "where studentid='%s' and courseselected.courseid = course.courseid "  % (id)
    cur.execute(sql)
    result = cur.fetchall()
    # for record in result:
    return result
    conn.close()

# lh 学生选课
def dbstu_xuanke(courseid,stuid):
    print(courseid + " " + stuid)
    sql = "insert into courseselected  value('%s', '%s') " % (courseid,stuid)
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()

# Bill 财务增加收支记录
def add_shouzhi(name,type,amount):
    sql = "insert into finance (accountingid,type,amount,time) values(%s,%s,%s,now())" % (name, type,amount)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 提交到数据库执行
        conn.commit()
        print("语句已经提交")
        return True
        conn.close()
    except:
        conn.rollback()

# lh 财务 查看报表
def show_baobiao():
    sql = "select sum(f2.amount)/2 as shouru,sum(f1.amount)/2 as zhichu, (sum(f2.amount) - sum(f1.amount))/2  as shouzhi  " \
          "from  finance as f1,finance as f2 where f1.type = 1 and f2.type = 0"
    cur.execute(sql)
    result = cur.fetchall()
    # for record in result:
    return result
    conn.close()

# lh 财务 查看报表详细
def show_baobiaoxize():
    sql = "select  (CASE when type='0' then '收入' when type='1' then '支出' END)as type ,f.amount  from  finance f"
    cur.execute(sql)
    result = cur.fetchall()
    # for record in result:
    return result
    conn.close()


# Bill 老师增加课程
def add_course(course_id, course_name, teacher_name):
    sql = "insert into course (courseid,teacherid,coursename) values('%s','%s','%s' )" % (course_id, teacher_name, course_name)
    # print("sql语句: "+sql)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 提交到数据库执行
        conn.commit()
        print("语句已经提交")
        return True
        conn.close()
    except:
        conn.rollback()

# lh 老师 查看课程
def show_allclass():
    sql = "select c.classid,stu.name from  class as c, account as stu where c.studentid = stu.accountingid"
    cur.execute(sql)
    result = cur.fetchall()
    # for record in result:
    return result
    conn.close()

# lh 老师 查看选课情况
def show_allcourseselected():
    sql = "SELECT rs.coursename, t.name, rs.stuname  " \
          "FROM (SELECT c.coursename , stu.name as stuname, c.teacherid FROM course as c, account as stu, " \
          "courseselected as cs   WHERE cs.courseid = c.courseid and cs.studentid = accountingid) as rs, account as t " \
          "where t.accountingid = rs.teacherid "
    cur.execute(sql)
    result = cur.fetchall()
    # for record in result:
    return result
    conn.close()

# lh 老师 查看考勤
def show_allregister():
    sql = "select a.name , r.time " \
          "from  register as r, account as a " \
          " where r.accountingid = a.accountingid"
    cur.execute(sql)
    result = cur.fetchall()
    # for record in result:
    return result
    conn.close()

# xijiawei
# 展示所有成品
def show_allproducts():
    sql = "select productCode,productType from productInfo;"
    cur.execute(sql)
    result=cur.fetchall()
    return result
    conn.close()

# xijiawei
# 插入成品静态表
def insert_into_productInfo(productcode,producttype,client,adminstrationCost,processCost,supplementaryCost,operatingCost,tax,remark):
    sql = "insert into productInfo (productCode,productType,client,adminstrationCost,processCost,supplementaryCost,operatingCost,tax,remark)value('%s','%s','%s','%s','%s','%s','%s','%s','%s');" \
          % (productcode,producttype,client,adminstrationCost,processCost,supplementaryCost,operatingCost,tax,remark)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 提交到数据库执行
        conn.commit()
        print("语句已经提交")
        return True
        conn.close()
    except:
        conn.rollback()

# xijiawei
# 插入成品录入表
def insert_into_productChange(productCode,entryClerk,updateOfContent):
    sql = "insert into productInfo (productCode,entryClerk,updateOfContent)value('%s','%s','%s','%s');" \
          % (productCode,entryClerk,updateOfContent)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 提交到数据库执行
        conn.commit()
        print("语句已经提交")
        return True
        conn.close()
    except:
        conn.rollback()