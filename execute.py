import smtplib, ssl
from email.mime.text import MIMEText

#write your email
sender = 'lilikheirandish@gmail.com'
receivers = ['lilikheirandish@gmail.com']
body = 'hello! my name is Leila'


msg = MIMEText(body, 'html') 
msg['Subject'] = 'python email'
msg['From'] = sender
msg['To'] = ','.join(receivers)



Send_Email = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
Send_Email.login(user = sender, password = '******')
Send_Email.sendmail(sender, receivers, msg.as_string())
Send_Email.quit()

