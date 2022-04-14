'''
老师视图
    登入
    查看教授课程
    选择教授课程
    查看课程下的学生
    修改学生成绩
'''
from lib import common
from interface import teacher_api
lll = '\033[1;31m'
llll = '\033[1;36m'
rr = '\033[0m'

# 记录用户登入
login_user = {"name" : None}

# 退出登入
def logout():
    name = common.logout_api(login_user["name"])
    login_user["name"] = name

# 登入
def login():
    print("登入...")
    while 1:
        name = input("请输入用户名(q退出)>>").strip()
        if name.lower() == "q": break
        t_f, msg = common.login_judge("Teacher", name)
        if not t_f:
            print(msg)
        else:
            passwd = input("请输入密码>>").strip()
            t_f2 = common.login_api("Teacher", msg, passwd)
            if t_f2:
                print("登入成功")
                login_user["name"] = name
                break
            else:
                print("密码错误")

# 查看教授课程
@common.login_auth("Teacher")
def check_course():
    print("查看课程")
    t_f, user_course = teacher_api.check_course_api(login_user["name"])
    if t_f:
        for i,v in enumerate(user_course):
            print(f"编号:{i+1}  课程名:{v}")
    else:
        print(user_course)

# 选择教授课程
@common.login_auth("Teacher")
def select_course():
    print("选择课程")
    while 1:
        name = input("请输入课程名字(q退出)>>").strip()
        if name.lower() == "q":break
        t_f,msg = teacher_api.select_course_api(login_user["name"],name)
        if t_f:
            print(msg)
            break
        else:
            print(msg)


# 查看课程下的学生
@common.login_auth("Teacher")
def check_stu():
    print("查看课程下学生")
    while 1:
        name = input("请输入课程名称(q退出)>>").strip()
        if name.lower() == "q":break
        t_f,msg = teacher_api.check_course_stu_api(name)
        if t_f:
            print(msg)
            break
        else:
            print(msg)



# 修改学生成绩
@common.login_auth("Teacher")
def change_grade():
    print("修改成绩")
    while 1 :
        stu_name = input("请输入学生姓名(q退出)>>").strip()
        if stu_name.lower() == "q":break
        course_name = input("请输入学生的学科名>>").strip()
        num = input("请输入修改的分数>>").strip()
        if num.isdigit():
            num = int(num)
            t_f,msg = teacher_api.change_stu_grade_api(login_user["name"],stu_name,course_name,num)
            if t_f:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("分数请输入数字")


tea_view = {
    "0" : ["退出登入",logout],
    "1" : ["登入系统",login],
    "2" : ["查看教授课程",check_course],
    "3" : ["选择教授课程",select_course],
    "4" : ["查看课程下学生",check_stu],
    "5" : ["修改学生成绩",change_grade],
    "6" : ["退出登入并返回主视图",logout]
}

# run
def tea_run():
    print("欢迎进入教师系统")
    while 1:
        print(f'{llll}＊—═—═—═—═—═—═—═—═—═＊{rr}\033[1;32m蟹堡教师{rr}{llll}＊═—═—═—═—═—═—═—═—═—＊{rr}')
        for k,v in tea_view.items():
            print(f"\t\t\t\t ✿  {lll}{k:.4}  {v[0]:<7}{rr}")
        print(f'{llll}━═━═━━═━═━━═━═━═━═━━═━♛━═━━═━═━━═━═━━═━═━━═━═━ {rr}')
        user_inp = input("请输入功能编号>").strip()
        if user_inp == "6":
            logout()
            print("正在返回主视图...");break
        if user_inp in tea_view:
            tea_view[user_inp][1]()
        else:
            print("功能编号不存在")

if __name__ == '__main__':
    tea_run()
