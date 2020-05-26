#Реализация класса Time (из 1 лекции этого года) 
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_input(self):
        self.hours = int(input('Hours: '))
        self.minutes = int(input('Minutes: '))
        self.seconds = int(input('Seconds: '))

    def print_time(self):
        print(f'{self.hours}:{self.minutes}:{self.seconds}')
time = Time(1 , 2 , 3)
time.time_input()
time.print_time()