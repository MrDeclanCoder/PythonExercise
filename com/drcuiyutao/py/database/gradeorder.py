# _*_ coding: utf-8 _*_

import sqlite3, os


def insertUser(id, name, score, cursor):
    cursor.execute(r"INSERT INTO user VALUES (?,?,?)", (id, name, score))


def close(cursor, conn):
    cursor.close()
    conn.commit()
    conn.close()


def get_score_in(low, high):
    # 返回指定分数区间的名字, 按分数从低到高排序
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor = cursor.execute('SELECT * FROM user WHERE score >= ? AND score <= ? order by score asc', (low, high))
    print(cursor.fetchall())
    close(cursor, conn)
    pass


db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('CREATE TABLE user(id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), score INT)')
insertUser('A-001', 'Adam', 99, cursor)
insertUser('A-002', 'Bob', 94, cursor)
insertUser('A-003', 'Calm', 100, cursor)
insertUser('A-004', 'Donald', 60, cursor)
close(cursor, conn)

get_score_in(80, 95)
get_score_in(60, 100)
get_score_in(96, 100)
