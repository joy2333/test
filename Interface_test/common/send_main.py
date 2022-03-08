import smtplib
import logging
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_sender = '3397188079@qq.com'  # 发件人邮箱账号
my_pass = 'ecejgziuqbxpchgi'  # 发件人邮箱密码


def mail(filename, addressee):
    ret = True
    try:

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("测试报告", 'utf-8')  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = Header("测试报告", 'utf-8')  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        subject = '测试报告'  # 邮件的主题，也可以说是标题
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('测试报告', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test_report.html"'
        message.attach(att1)

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, addressee, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        logging.info("发送邮件时出现异常：{}".format(e))
        ret = False

    if ret:
        logging.info("邮件发送成功")
    else:
        logging.info("邮件发送失败")
    return ret
