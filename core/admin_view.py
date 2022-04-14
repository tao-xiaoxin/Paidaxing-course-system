'''
管理员视图
    注册
    登入
    创建学校
    创建老师
    创建课程
'''
from lib import common
from interface import admin_api

lll = '\033[1;31m'
llll = '\033[1;36m'
rr = '\033[0m'

# 记录用户登入
login_user = {"name" : None}

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
    common.register_api('Admin')


# 登入
def login():
    print("登入...")
    while 1:
        name = input("请输入用户名(q退出)>>").strip()
        if name.lower() == "q": break
        t_f, msg = common.login_judge("Admin", name)
        if not t_f:
            print(msg)
        else:
            passwd = input("请输入密码>>").strip()
            t_f2 = common.login_api("Admin", msg, passwd)
            if t_f2:
                print("登入成功")
                login_user["name"] = name
                break
            else:
                print("密码错误")

# 创建学校
@common.login_auth("Admin")
def create_school():
    print('创建学校...')
    while 1:
        name = input("请输入学校名(q退出)>>").strip().lower()
        if name.lower() == "q":break
        campus = input("请输入校区>>").strip().lower()
        t_f,msg = admin_api.create_school_api(name,campus)
        if t_f:
            print(msg)
            break
        else:
            print(msg)


# 创建老师
@common.login_auth("Admin")
def create_tea():
    print("创建老师...\n温馨提示: 用户名长度必须大于3,密码必须由数字或字母组成且大于3位")
    common.register_api('Teacher')

# 创建课程
@common.login_auth("Admin")
def create_course():
    print("创建课程...")
    while 1 :
        name = input("请输入课程名字(q退出)>>").strip().lower()
        if name.lower() == "q":break
        price = input("请输入课程费用(元)>>").strip()
        if price.isdigit():
            price = int(price)
            period = input("请输入课程周期(月)>>").strip()
            if period.isdigit():
                period = int(period)
                t_f,msg = admin_api.create_course_api(name,price,period)
                if t_f:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print("请输入数字")
        else:
            print("请输入数字")

admin_view = {
    "0" : ["退出登入",logout],
    "1" : ["注册用户",register],
    "2" : ["登入系统",login],
    "3" : ["创建学校",create_school],
    "4" : ["创建老师",create_tea],
    "5" : ["创建课程",create_course],
    "6" : ["退出登入并返回主视图",login]
}

# admin_run
def admin_run():
    print("欢迎进入管理员系统")
    while 1:
        print(f'{llll}＊—═—═—═—═—═—═—═—═—═＊{rr}\033[1;32m蟹堡管理{rr}{llll}＊═—═—═—═—═—═—═—═—═—＊{rr}')
        for k,v in admin_view.items():
            print(f"\t\t\t\t ✿{lll}{k:>4}  {v[0]:<5}{rr}")
        print(f'{llll}━═━═━━═━═━━═━═━═━═━━═━♛━═━━═━═━━═━═━━═━═━━═━═━ {rr}')
        user_inp = input("请输入功能编号>>").strip()
        if user_inp == "6":
            logout()
            print("正在返回主视图...");break
        if user_inp in admin_view:
            admin_view[user_inp][1]()
        else:
            print("没有该编号功能")

if __name__ == '__main__':
    admin_run()
