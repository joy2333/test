# 导包
import pymysql
from common.project_path import conf_path
from common.read_config import ReadConfig


# 创建工具类
class DBUtil:
    # 初始化
    __conn = None
    __cursor = None

    # 创建连接
    @classmethod
    def __get_conn(cls, host, port, user, password, database):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host=host,
                                         port=port,
                                         user=user,
                                         password=password,
                                         database=database)
        return cls.__conn

    # 获取游标
    @classmethod
    def __get_cursor(cls, host, port, user, password, database):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn(host, port, user, password, database).cursor()
        return cls.__cursor

    # 执行sql
    @classmethod
    def exe_sql(cls, sql, host, port, user, password, database):
        try:
            # 获取游标对象
            cursor = cls.__get_cursor(host, port, user, password, database)
            # 调用游标对象的execute方法，执行sql
            cursor.execute(sql)
            #  如果是查询
            if sql.split()[0].lower() == "select":
                # 返回所有数据
                return cursor.fetchall()
            #  否则：
            else:
                # 提交事务
                cls.__conn.commit()
                # 返回受影响的行数
                return cursor.rowcount
        except Exception as e:
            # 事务回滚
            cls.__conn.rollback()
            # 打印异常信息
            print(e)
        finally:
            # 关闭游标
            cls.__close_cursor()
            # 关闭连接
            cls.__close_conn()

    # 关闭游标
    @classmethod
    def __close_cursor(cls):
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None

    # 关闭连接
    @classmethod
    def __close_conn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None


# 入参：sql语句，库名
def implement_sql(sql, database, environment="uat"):
    """
    sql:sql语句
    database:数据库名称
    environment:环境
    """
    if environment == "uat":
        host, port, username, password = ReadConfig(conf_path).get_data('mysql_uat', 'db_config')
    else:
        host, port, username, password = ReadConfig(conf_path).get_data('mysql_stg', 'db_config')
    result = DBUtil.exe_sql(sql, host, port, username, password, database)
    return result


if __name__ == '__main__':
    query_sql = "SELECT * FROM student"
    res = implement_sql(query_sql, "test")
    print(res)
