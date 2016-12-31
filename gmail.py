import smtplib


def send_mail(subject,body,config):
	gmail_user=config['gmailid']
	gmail_password=config['gmailpw']
	to=config['gmailid']


	email_text = """\
To: %s 
Subject: %s

%s
""" % (to, subject,body)

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_password)
	server.sendmail(gmail_user, to, email_text)
	server.close()
