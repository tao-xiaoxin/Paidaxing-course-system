''''
文件保存和查看
'''
import os
import pickle
from conf import setting

# 保存各类信息
def save_date(obj):
    # 拼接一个以类名为名的文件夹
    dir_path = os.path.join(setting.DB_PATH,type(obj).__name__)
    # 判断是否存在, 不存在创建一个
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    # 拼接一个文件路径,以对象名字为文件名
    if obj.__class__.__name__ == "School":
        file_path = os.path.join(dir_path, f"{obj.name}_{obj.campus}.pik")
    else:
        file_path = os.path.join(dir_path,f"{obj.name}.pik")
    with open(file_path,"wb")as f:
        pickle.dump(obj,f)
        f.flush()


# 获取对象
def check_obj(class_name,name):
    # 拼接出文件路径
    file_path = os.path.join(setting.DB_PATH,class_name,f"{name}.pik")
    with open(file_path,"rb")as f1:
        obj = pickle.load(f1)
    return obj


