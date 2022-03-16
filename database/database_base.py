# -*- coding: utf-8 -*-
import sys
from shlex import join

import pymysql
import mysql
import mysql.connector


def open():
    db = pymysql.connect(host="localhost", user="root", password="19991202abc", database="fund_system", charset="utf8")
    return db


def exec(sql, values):
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    try:
        cursor.execute(sql, values)  # 执行增删改的SQL语句
        db.commit()  # 提交数据
        return 1  # 执行成功
    except:
        db.rollback()  # 发生错误时回滚
        return 0  # 执行失败
    finally:
        cursor.close()  # 关闭游标
        db.close()  # 关闭数据库连接


#带参数的精确查询
# def query(sql, *keys):
#     db = open()  # 连接数据库
#     cursor = db.cursor()  # 使用cursor()方法获取操作游标
#     cursor.execute(sql, keys)  # 执行查询SQL语句
#     result = cursor.fetchall()  # 记录查询结果
#     cursor.close()  # 关闭游标
#     db.close()  # 关闭数据库连接
#     return result  # 返回查询结果


# 不带参数的模糊查询
def query(sql):
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    cursor.execute(sql)  # 执行查询SQL语句
    result = cursor.fetchone()  # 记录查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    print(''.join(map(str,result)))
    return ''.join(map(str,result)) # 返回查询结果


def insert(sql):
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    cursor.execute(sql)  # 执行插入SQL语句
    db.commit()
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    print("插入完成")


def is_has(username):
    db = open()
    cursor = db.cursor()
    sql = "SELECT * FROM userinfo WHERE username='%s'" % username
    cursor.execute(sql)  # 执行mysql语句
    db.commit()
    data = cursor.fetchall()  # 获取所有的内容
    cursor.close()
    print(data)
    db.close()
    if data:
        return True
    else:
        return False

def is_has_student(username):
    db = open()
    cursor = db.cursor()
    sql = "SELECT distinct * FROM studentinfo WHERE id='%s'" % username
    cursor.execute(sql)  # 执行mysql语句
    db.commit()
    data = cursor.fetchall()  # 获取所有的内容
    cursor.close()
    print(data)
    print('已调用is_has_student')
    db.close()
    if data:
        return True
    else:
        return False

def is_has_teacher(username):
    db = open()
    cursor = db.cursor()
    sql = "SELECT distinct * FROM teacherinfo WHERE id='%s'" % username
    cursor.execute(sql)  # 执行mysql语句
    db.commit()
    data = cursor.fetchall()  # 获取所有的内容
    cursor.close()
    print(data)
    print('已调用is_has_teacher')
    db.close()
    if data:
        return True
    else:
        return False

