'''
学生视图
    注册
    登入
    选择校区
    选择课程
    查看成绩
'''
from interface import student_api
from lib import common
lll = '\033[1;31m'
llll = '\033[1;36m'
rr = '\033[0m'

# 记录用户登入
login_user = {"name":None}

# 退出登入
def logout():
    name = common.logout_api(login_user["name"])
    login_user["name"] = name

# 注册
def register():
    if login_user["name"]:
        print("请退出登入状态在进行注册")
        return
    print("注册\n温馨提示: 用户名长度必须大于3,密码必须由数字或字母组成且大于3位")
    common.register_api('Student')

# 登入
def login():
    print("登入...")
    while 1:
        name = input("请输入用户名(q退出)>>").strip()
        if name.lower() == "q":break
        t_f,msg = common.login_judge("Student",name)
        if not t_f:
            print(msg)
        else:
            passwd = input("请输入密码>>").strip()
            t_f2 = common.login_api("Student",msg,passwd)
            if t_f2:
                print("登入成功")
                login_user["name"] = name
                break
            else:
                print("密码错误")

# 选择校区
@common.login_auth("Student")
def select_campus():
    print("选择校区")
    while 1 :
        name = input("请输入学校名(q退出)>>").strip()
        if name.lower() == "q":break
        campus = input("请输入校区>>").strip()
        t_f,msg = student_api.selece_school_campus_api(login_user["name"],name,campus)
        if t_f:
            print(msg)
            break
        else:
            print(msg)


# 选择课程
@common.login_auth("Student")
def select_course():
    print("选择课程")
    while 1 :
        name = input("请输入课程名称(q退出)>>").strip()
        if name.lower() == "q":break
        t_f,msg = student_api.select_course_api(login_user["name"],name)
        if t_f:
            print(msg)
            break
        else:
            print(msg)

# 查看成绩
@common.login_auth("Student")
def check_grade():
    print("查看成绩")
    t_f,user_grade = student_api.check_grade_api(login_user["name"])
    if t_f:
        for k,v in user_grade.items():
            print(f"学科:{k} 分数:{v}")
    else:
        print(user_grade)


stu_view = {
    "0" : ["退出登入",logout],
    "1" : ["注册用户",register],
    "2" : ["登入系统",login],
    "3" : ["选择校区",select_campus],
    "4" : ["选择课程",select_course],
    "5" : ["查看成绩",check_grade],
    "6" : ["退出登入并返回主视图",logout]
}

def stu_run():
    print("欢迎进入学生登入系统")
    while 1:
        print(f'{llll}＊—═—═—═—═—═—═—═—═—═＊{rr}\033[1;32m蟹堡学员{rr}{llll}＊═—═—═—═—═—═—═—═—═—＊{rr}')
        for k,v in stu_view.items():
            print(f"\t\t\t\t ✿{lll}{k:>4}  {v[0]:<6}{rr}")
        print(f'{llll}━═━═━━═━═━━═━═━═━═━━═━♛━═━━═━═━━═━═━━═━═━━═━═━ {rr}')
        user_inp = input("请选择功能编号>>").strip()
        if user_inp == "6":
            logout()
            print("正在返回主视图...");break
        if user_inp in stu_view:
            stu_view[user_inp][1]()
        else:
            print("功能编号不存在")

if __name__ == '__main__':
    stu_run()