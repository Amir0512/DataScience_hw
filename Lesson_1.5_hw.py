from datetime import datetime


class Logger:

    def __init__(self):
        self.date = datetime.now().date()
        self.file_dir = 'C:/Users/mrzia/PycharmProjects/pythonProject'
        self.text_dir = f'{self.file_dir}/log_{self.date}.txt'
        self.last_event = ''

    @staticmethod
    def date():
        return datetime.today().strftime('%d.%m.%Y')

    def write_log(self, event):
        curr_time = Logger.date()
        if curr_time != self.date:
            self.date = curr_time
            self.text_dir = f'{self.file_dir}/log_{self.date}.txt'
        with open(self.text_dir, 'a+', encoding='UTF-8') as f:
            current_time = datetime.now().strftime('%H:%M:%S')
            current_event = f'[{current_time}] {event}'
            f.write(f'{current_event}\n')
            self.last_event = current_event

    def clear_log(self):
        with open(self.text_dir, 'w', encoding='UTF-8') as f:
            f.write('')

    def get_logs(self):
        with open(self.text_dir, 'r', encoding='UTF-8') as f:
            logs = f.readlines()
        return logs

    def get_last_event(self):
        return self.last_event
