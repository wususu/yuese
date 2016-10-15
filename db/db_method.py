import pymysql


def connect(host, user, passwd, db):
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, charset='utf8')
    return conn

def get(conn, sql):
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
        result = cur.fetchmany(100)
        conn.commit()
    finally:
        conn.close()
    return result

if __name__ == '__main__':
    conn = connect('127.0.0.1', 'root', 'root', 'wechat_article')
    sql = "select * from article ORDER BY post_time"
    print(get(conn, sql))