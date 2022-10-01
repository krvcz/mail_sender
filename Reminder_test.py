from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from DBconnector import Connector
from Reminder import Reminder
from MailSender import MailSender
from Validators import Validator
from unittest.mock import patch

@patch('Validators.Validator.default', return_value = 'template.html' )
@patch('MailSender.MailSender.send_mail')
def test_check_date(valid_mock, mail_mock):
    data = [(1, '123@gmail.com', 'Sebastian', 'Bitwa Warszawska', '2022-09-24'), (2, '124@gmail.com', 'Bartosz', 'Pan Koziołek', '2022-09-16'),
            (3, '125@gmail.com', 'Sebastian', '1920', '2022-09-20'), (4, '126@gmail.com', 'Kacper', 'W pustyni i w puszczy', '2022-09-17'),
            (5, '127@gmail.com', 'Jędrzej', 'On', '2022-09-30')]
    mailsender = MailSender('server', 'mail', 'password')
    reminder = Reminder(data, mailsender, Validator.default, '2022-09-17')
    reminder.check_date()
    valid_mock.assert_called()
    mail_mock.assert_called()