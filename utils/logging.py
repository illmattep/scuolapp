import os
import datetime

class Logger:
    def __init__(self, enabled=True):
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.log_file = os.path.join(log_dir, f'{current_time}.log')
        with open(self.log_file, 'w') as file:
            file.write('')

    def logthis(self, message, level=''):
        with open(self.log_file, 'a') as file:
            if level:
                file.write(f'[{level.upper()}] {message}\n')
                print(f'[{level.upper()}] {message}')
            else:
                file.write(f'{message}\n')
                