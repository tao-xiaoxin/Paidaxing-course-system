'''
教师功能接口
    查看教授课程
    选择教授课程
    查看课程下的学生
    修改学生成绩
'''
import os
from db import class_media
from conf import setting


# 查看教授的课程
def check_course_api(name):
    user_obj = class_media.Teacher.check(name)
    user_course = user_obj.check_course()
    if len(user_course) == 0:
        return False, "还未选择教授的课程"
    else:
        return True, user_course

# 选择教授的课程
def select_course_api(user_name,course_name):
    course_path = os.path.join(setting.DB_PATH, "Course", f"{course_name}.pik")
    if not os.path.isfile(course_path):
        return False, f"'{course_name}'课程不存在"
    else:
        user_obj = class_media.Teacher.check(user_name)
        course_obj = class_media.Course.check(course_name)
        if course_name in check_course_api(user_name):
            return False, f"'{course_name}'课程已存在"
        else:
            user_obj.select_course(course_name)
            return True, f"'{course_name}'课程添加成功"


# 查看看课程下的学生
def check_course_stu_api(course_name):
    course_path = os.path.join(setting.DB_PATH,"Course",f"{course_name}.pik")
    if not os.path.isfile(course_path):
        return False, f"'{course_name}'课程不存在"
    else:
        course_obj = class_media.Course.check(course_name)
        course_stu_list = course_obj.check_stu_list()
        if len(course_stu_list) == 0:
            return True, f"还没有学生选择'{course_name}'课程"
        else:
            return True, f"选择了'{course_name}'课程的学生:{course_stu_list}"




# 修改学生成绩
def change_stu_grade_api(user_name,stu_name,stu_course,num):
        stu_path = os.path.join(setting.DB_PATH,"Student",f"{stu_name}.pik")
        course_path = os.path.join(setting.DB_PATH, "Course", f"{stu_course}.pik")
        if os.path.isfile(stu_path) and os.path.isfile(course_path):
            stu_obj = class_media.Student.check(stu_name)
            course_obj = class_media.Course.check(stu_course)
            if not course_obj.name in stu_obj.check_course():
                return False, f"学生'{stu_name}'未选择'{stu_course}'这门课程"
            else:
                tea_obj = class_media.Teacher.check(user_name)
                tea_obj.change_grade(stu_obj, stu_course, num)
                return True, f"学生'{stu_name}'成绩修改成功"
        else:
            return False, f"学生或者课程不存在"

