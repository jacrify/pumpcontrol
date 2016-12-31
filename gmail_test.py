import smtplib


gmail_user="john.cranney@gmail.com"
gmail_password="rpiyazdznoezdvry"
to="john.cranney@gmail.com"
subject="test"
body=""


email_text = """  
To: %s  
Subject: %s

%s
""" % (to, subject, body)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user, to, email_text)
server.close()
