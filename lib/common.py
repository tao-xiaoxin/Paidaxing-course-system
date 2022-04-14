'''
公共功能
'''
import os
import hashlib
from conf import setting
from db import db_handle,class_media


# 登入装饰器
def login_auth(class_name):
    from core import student_view,teacher_view,admin_view
    def outter(func):
        def wrapper(*args,**kwargs):

            if  class_name == "Student":
                if not student_view.login_user["name"]:
                    print("请學生登入后在使用该功能")
                    student_view.login()
                else:
                    res = func(*args,**kwargs)
                    return res

            elif  class_name == "Teacher":
                if not teacher_view.login_user["name"]:
                    print("请教师登入后在使用该功能")
                    teacher_view.login()
                else:
                    res = func(*args,**kwargs)
                    return res

            elif  class_name == "Admin":
                if not admin_view.login_user["name"]:
                    print("请管理员登入后在使用该功能")
                    admin_view.login()
                else:
                    res = func(*args,**kwargs)
                    return res

        return wrapper
    return outter


# 登入输入用户名判断用户是否存在
def login_judge(classname,name):
    if not os.path.isfile(os.path.join(setting.DB_PATH, classname, f"{name}.pik")):
        if classname == "Student":
            return False, "该学生不存在"
        elif classname == "Teacher":
            return False, "该教师不存在"
        elif classname == "Admin":
            return False, "该管理员不存在"
    else:
        return True, name

# 公共登入接口
def login_api(class_name,name,passwd):
    obj = db_handle.check_obj(class_name,name)
    pass
    if encrypt(passwd) == obj.passwd:  # 对密码进行加密后对比
        return True
    else:
        return False


# 公共注册
def register_api(classname):
    while 1:
        name = input("请输入注册(q退出)>>").strip()
        if name.lower() == "q":break
        if len(name) <= 3:
            print("用户名长度必须大于3")
            continue
        if os.path.isfile(os.path.join(setting.DB_PATH,classname,f"{name}.pik")):
            if classname == "Student":
                print("该学生已存在");continue
            elif classname == "Teacher":
                print("该教师已存在");continue
            elif classname == "Admin":
                print("该管理员已存在");continue
        else:
            passwd = input("请输入密码>>").strip()
            if len(passwd) <= 3 or not passwd.encode("utf-8").isalnum():
                print("密码必须由数字或字母组成且大于3位")
                continue
            passwd2 = input("请确认密码>>").strip()
            if passwd == passwd2:
                if classname == "Admin":
                    class_media.Admin(name,encrypt(passwd))  # 对传入的密码加密
                elif classname == "Student":
                    class_media.Student(name,encrypt(passwd))
                elif classname == "Teacher":
                    class_media.Teacher(name,encrypt(passwd))
                print("注册成功")
                break
            else:
                print("两次密码不一致,请重新输入")



# 密码加密
def encrypt(passwd):
    mm = hashlib.md5(passwd.encode("utf-8"))
    mm.update("派大星".encode("utf-8"))
    return mm.hexdigest()


# 退出登入
def logout_api(name):
    if not name:
        print("当前未登入状态")
    else:
        print("账号退出成功")
        return