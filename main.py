
from os import getenv,path
from datetime import date, timedelta, datetime
from dotenv import load_dotenv
from MailSender import MailSender
from DBconnector import Connector
from Reminder import Reminder
from Validators import Validator

load_dotenv()
BASE_DIR = path.dirname(path.abspath(__file__))
db_path = path.join(BASE_DIR, "baza.db")



if __name__ == '__main__':
    conn = Connector(db_path, 'SELECT * FROM books')
    mail = MailSender('smtp.poczta.onet.pl', getenv('MAIL_ADDRESS'), getenv('MAIL_PASSWORD'))
    reminder = Reminder(conn.query_result, mail, Validator.default, datetime.strptime('2022-09-17', '%Y-%m-%d').date())
    reminder.check_date()
