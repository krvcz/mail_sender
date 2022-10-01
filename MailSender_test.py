from unittest.mock import patch
from MailSender import MailSender

@patch('smtplib.SMTP_SSL')
def test_send_mail(mock):
    mailsender = MailSender('server', 'mail', 'password')
    mailsender.send_mail('receiver_mail', 'message')
    mock.assert_called()
    context = mock.return_value.__enter__.return_value
    context.login.assert_called_with('mail', 'password')
    context.sendmail.assert_called_with('mail', 'receiver_mail', 'message')
