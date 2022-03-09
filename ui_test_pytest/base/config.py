import logging.handlers
from base.project_path import log_path


# 日志基础配置方法
def basic_log_config():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # 1.创建处理器
    # 1.1 输出到控制台
    ls = logging.StreamHandler()

    # 1.2 每日生成一个日志文件
    # lht = logging.handlers.TimedRotatingFileHandler("test_result/log/test.log",
    #                                                 when="midnight", interval=1, backupCount=2, encoding="utf-8")
    # 1.2 限制日志文件的大小为5M，备份数为4
    lht = logging.handlers.RotatingFileHandler(log_path + '/test.log', maxBytes=5 * 1024 * 1024,
                                               backupCount=5, encoding="utf-8")
    # 2.创建格式化器
    formatter = logging.Formatter(fmt="[%(asctime)s]-[%(levelname)s]-[%(name)s]-"
                                      "[%(filename)s(%(funcName)s:%(lineno)d)]:%(message)s")
    # 3.给处理器设置格式化器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 4.给日志器添加处理器
    logger.addHandler(ls)
    logger.addHandler(lht)


if __name__ == '__main__':
    basic_log_config()
    for i in range(40000):
        logging.info("软件测试")
