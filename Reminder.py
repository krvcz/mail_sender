from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Reminder:
    def __init__(self, data, mail_sender, validator, date):
        self.data = data
        self.mail_sender = mail_sender
        self.validator = validator
        self.date = date

    def check_date(self):
        for row in self.data:
            mail, name, title, return_at = row[1:]
            html = self.validator(mail, name, title, return_at, self.date)
            if html is not None:
                to_email = self.mail_sender.sender_mail
                from_email = self.mail_sender.sender_mail
                subject = 'Wypożyczenie książki [PRZYPOMNIENIE!]'
                message = MIMEMultipart()
                message['Subject'] = subject
                message['From'] = from_email
                message['To'] = to_email
                message.attach(MIMEText(html, "html"))
                msgBody = message.as_string()
                self.mail_sender.send_mail(self.mail_sender.sender_mail, msgBody)
