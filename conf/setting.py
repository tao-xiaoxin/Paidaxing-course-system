'''
配置
'''
import os

PATH = os.path.abspath(os.path.join(__file__,"..",".."))  # E:\选课系统
DB_PATH = os.path.join(PATH,"db")  # E:\选课系统\db


if  not os.path.isdir(DB_PATH):
    os.mkdir(DB_PATH)
