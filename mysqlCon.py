import pymysql

def db_connect():
    # 打开数据库连接
    db = pymysql.connect(host='localhost', user='root', passwd="", db='district_pinyin')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    return (db, cursor)


def init_provinces():
    db = db_connect()[0]
    cursor = db_connect()[1]
    # 使用 execute()  方法执行 SQL 查询
    province_sql = "SELECT id, shortname, pinyin FROM district_pinyin.china_district_pinyin where level=1; "
    try:
        # 执行SQL语句
        cursor.execute(province_sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        return results
    except:
        print("Error: unable to fetch data")
    finally:
        db.close()


def init_cities():
    db = db_connect()[0]
    cursor = db_connect()[1]
    # 使用 execute()  方法执行 SQL 查询
    city_sql = "SELECT pid, shortname, pinyin FROM district_pinyin.china_district_pinyin where level=2; "
    try:
        # 执行SQL语句
        cursor.execute(city_sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        return results
    except:
        print("Error: unable to fetch data")
    finally:
        db.close()




