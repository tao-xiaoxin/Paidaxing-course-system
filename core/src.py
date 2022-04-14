'''
主视图
    学生视图
    老师视图
    管理员视图
'''
from core import admin_view,student_view,teacher_view


lll = '\033[1;31m'
llll = '\033[1;36m'
rr = '\033[0m'

# 学生视图入口
def student():
    print("正在进入学生登入窗口...")
    student_view.stu_run()

# 老师视图入口
def teacher():
    print("正在进入教师登入窗口...")
    teacher_view.tea_run()

# 管理员视图入口
def admin():
    print("正在进入管理员登入接口...")
    admin_view.admin_run()

view_dic = {
    "0": ["退出",student],
    "1": ["学生登入入口", student],
    "2": ["老师登入入口", teacher],
    "3": ["管理员登入入口", admin],
}

photo = f'''{llll}
            ╭╮╭╮ ╭━━╮ ╭━━╮ ╭━━╮ ╭╮╭╮
            ┃┃┃┃ ┃╭╮┃ ┃╭╮┃ ┃╭╮┃ ┃╰╯┃
            ┃╰╯┃ ┃╰╯┃ ┃╰╯┃ ┃╰╯┃ ╰╮╭╯
            ┃╭╮┃ ┃╭╮┃ ┃╭━╯ ┃╭━╯  ┃┃　
            ┃┃┃┃ ┃┃┃┃ ┃┃   ┃┃    ┃┃　
            ╰╯╰╯ ╰╯╰╯ ╰╯   ╰╯    ╰╯
{rr}\n'''


# run
def run():
    print(f"{'':>15}\033[1;30;42m欢迎进入蟹堡王选课系统\033[0m\n{photo}")
    while 1:
        print(f'{llll}★~☆·☆.~★*∴*~★*∴{rr}{lll}蟹堡学院{rr}{llll}*·∴~*★*∴*★~☆·☆.~*∴*~★{rr}')
        for k, v in view_dic.items():
            print(f"{lll}\t\t\t\t✡{k:>3} {v[0]:<7}{rr}")
        print(f'{llll}°．·°∴ ☆．．·°．·°∴ ☆．．·°．·°∴ ☆．．·°．·°∴ ☆．·°{rr}')
        user_inp = input("请输入功能编号>>").strip()
        if user_inp.lower() == "0":
            print("正在退出...")
            break
        if user_inp in view_dic:
            view_dic[user_inp][1]()
        else:
            print("编号不存在")

if __name__ == '__main__':
    run()
