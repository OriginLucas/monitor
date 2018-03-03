#!/usr/bin/python
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class Mail():
    def __init__(self):
        self.rank={
            1:'normail',
            2:'warning',
            3:'high',
            4:'serious',
        }
    def rank(self,count):
        if count>=5 and count<10:
            self.mail_msg(2)
        elif count>=10 and count<15:
            self.mail_msg(3)
        elif count>=15:
            self.mail_msg(4)
        elif count<5:
            self.mail_msg(1)

    def mail_msg(self,level):
        '''还需要具体项目名'''

        mail=self.rank[level]
        self.sendmail(mail)


    def sendmail(self,mail):
        msg = MIMEText(mail,'plain', 'utf-8')
        msg_root = MIMEMultipart('related')

        f = '18235105708@163.com'
        t = 'zgw747897@gmail.com'
        p = 'wy7478'
        msg_root.attach(msg)
        msg_root['From'] = f
        msg_root['To'] = t
        msg_root['Subject'] = 'wrsndm'
        server = SMTP('smtp.163.com', 25)
        # server.set_debuglevel(1)   #显示发送过程
        server.login(f, p)
        server.sendmail(f, [t], msg_root.as_string())
        server.quit()

