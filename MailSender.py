import smtplib, ssl



class MailSender:
    def __init__(self, smtp_server, sender_mail, password, context = ssl.create_default_context(), port = 465 ):
        self.smtp_server = smtp_server
        self.sender_mail = sender_mail
        self.password = password
        self.context = context
        self.port = port


    def send_mail(self, receiver_mail, message):
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context = self.context) as connection:
                connection.login(self.sender_mail, self.password)
                connection.sendmail(self.sender_mail, receiver_mail, message)

