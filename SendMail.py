import smtplib, ssl
from email.mime.text import MIMEText
sender = 'youremail0@gmail.com'
receivers = ['youremail@icloud.com']
body_of_email = 'hello this is test!'

msg = MIMEText('body_of_email', 'html') 
msg['Subject'] = 'Subject line goes here'
msg['From'] = sender
msg['To'] = ','.join(receivers)
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'Lili Kheirandish', password = '******')
s.sendmail(sender, receivers, msg.as_string())
s.quit()
"""
import subprocess
process = subprocess.Popen(['echo', 'More output'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
stdout, stderr
"""  




