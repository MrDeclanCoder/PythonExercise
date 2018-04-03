# 导入sqlite驱动
import sqlite3


def createConn(dbName):
    # 连接到sqlite数据库
    # 数据库文件是test.db
    # 如果文件不存在, 会自动在当前目录创建
    conn = sqlite3.connect(dbName)
    return conn


def createCursor(conn):
    # 创建一个Cursor
    cursor = conn.cursor()
    return cursor


def close(cursor, conn):
    # 关闭cursor
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭connection
    conn.close()


def selectEle(cursor, tableName):
    # 查询
    cursor = cursor.execute('select * from user where id=?', ('1',))
    values = cursor.fetchall()
    print(values)


conn = createConn('test.db')
cursor = createCursor(conn)
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\',\'Micheal\')')
selectEle(cursor, conn)
close(cursor, conn)
