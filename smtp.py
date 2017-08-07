import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'fireburnbird@163.com'
receivers = ['529077434@qq.com']

mail_host="smtp.163.com"
mail_user="fireburnbird@163.com"
mail_pass="xxxxxxx"

message = MIMEText('Python mail sending test...','plain','utf-8')
message['From'] = 'fireburnbird@163.com'
message['To'] = '529077434@qq.com'

subject = 'Python SMTP mail test'
message['Subject'] = Header(subject,'utf-8')
try:
       
       smtpObj = smtplib.SMTP()
       smtpObj.connect(mail_host,25)
       smtpObj.login(mail_user,mail_pass)
       smtpObj.sendmail(sender,receivers,message.as_string())
       print "successful sending"
except:
       print "fail to send!"


