#дополненная реализация класса Time (из 2 лекции этого года)
from datetime import *
class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_input(self):
        self.hours = int(input('Hours: '))
        self.minutes = int(input('Minutes: '))
        self.seconds = int(input('Seconds: '))

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def validate(self):
        if self.hours > 24:
            return False
        elif self.minutes > 60:
            return False
        elif self.seconds > 60:
            return False
        else:
            return True

    def time_now(self):
        now = datetime.today()
        return f'{now.hour}:{now.minute}:{now.second}'

class TimeStamp(Time):

    def print_time_now(self):
        parent = super()
        return parent.time_now()

time = Time(12 , 30 , 30)
#time.time_input()
print(time.__str__())
print(time.validate())

ts = TimeStamp(1,2,3)
print(ts.print_time_now())