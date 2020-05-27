#дополненная реализация класса Time (из 3 лекции этого года)
#надеюсь я правильно понял прицнип работы этих ошибок
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

    def __validate(self):
        if self.hours > 24:
            raise ValueError("Похоже вы из другой галактики, либо просто плохо учились в школе(садике), кароче нармально чясы введи и заработаю")
        elif self.minutes > 60:
            raise ValueError("скопируй данную ссылочку , может поможет https://ru.wikipedia.org/wiki/Единицы_измерения_времени#Сутки,_час,_минута_и_секунда")
        elif self.seconds > 60:
            raise ValueError("Опа ошибочка")
        else:
            return True

class TimeStamp(Time):
#я же правильно понял что теперь он именно хранит текущее время , а выводим мы его на строке 41 ?
     def time_now(self):
        now = datetime.today()
        return f'{now.hour}:{now.minute}:{now.second}'

time = Time(23 , 42 , 70)
#time.time_input()
print(time.__str__())
print(time._Time__validate())

ts = TimeStamp(1,2,3)
print(ts.time_now())
