from datetime import date, timedelta, datetime
from Validators import  Validator, env

def test_default():
    data = [(1, '123@gmail.com', 'Sebastian', 'Bitwa Warszawska', '2022-09-24', env.get_template('Reminder.html').render(title='Bitwa Warszawska', name='Sebastian', return_at_date='2022-09-24', days=7)),
            (2, '124@gmail.com', 'Bartosz', 'Pan Koziołek', '2022-09-14', env.get_template('ReminderCharge.html').render(title='Pan Koziołek', name='Bartosz', return_at_date='2022-09-14', charge=0.75)),
            (3, '125@gmail.com', 'Sebastian', '1920', '2022-09-20', env.get_template('Reminder.html').render(title='1920', name='Sebastian', return_at_date='2022-09-20', days=3)),
            (4, '126@gmail.com', 'Kacper', 'W pustyni i w puszczy', '2022-09-17', env.get_template('ReminderToday.html').render(title='W pustyni i w puszczy', name='Kacper', return_at_date='2022-09-17', days=3)),
            (5, '127@gmail.com', 'Jędrzej', 'On', '2022-09-30', None),
            (6, '127@gmail.com', 'Jędrzej', 'Diuna', '2022-09-11', env.get_template('ReminderCharge.html').render(title='Diuna', name='Jędrzej', return_at_date='2022-09-11', charge=6*0.25))]

    for row in data:
        assert Validator.default(row[1], row[2], row[3], row[4], datetime.strptime('2022-09-17', '%Y-%m-%d').date()) == row[5]
