from os import path
from datetime import date, timedelta, datetime
from jinja2 import Environment, FileSystemLoader


env = Environment(
    loader=FileSystemLoader('%s/templates/' % path.dirname(__file__)))

class Validator:

    @staticmethod
    def default(mail, name, title, return_at, date):
        return_at_date = datetime.strptime(return_at, '%Y-%m-%d').date()
        if return_at_date > date and return_at_date - timedelta(days = 7) == date:
            template = env.get_template('Reminder.html')
            output = template.render(title=title, name = name, return_at_date = return_at_date, days = 7)
            return output

        if return_at_date > date and return_at_date- timedelta(days = 3) == date:
            template = env.get_template('Reminder.html')
            output = template.render(title=title, name = name, return_at_date = return_at_date, days = 3)
            return output
        if return_at_date == date :
            template = env.get_template('ReminderToday.html')
            output = template.render(title=title, name = name, return_at_date = return_at_date)
            return output
        if return_at_date < date and (date - return_at_date).days % 3 == 0:
            template = env.get_template('ReminderCharge.html')
            interval = (date - return_at_date)
            charge = interval.days * 0.25
            output = template.render(title=title, name=name, return_at_date=return_at_date, charge=charge)
            return output
        return None