from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'm297907057@126.com'
    receivers = ['297907057@qq.com']
    message = MIMEText('777777', 'plain', 'utf-8')
    message['From'] = 'm297907057@126.com'
    message['To'] = '297907057@qq.com'
    message['Subject'] = '88'
    smtper = SMTP('smtp.126.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'aiqing123')
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('邮件发送完成!')


if __name__ == '__main__':
    main()