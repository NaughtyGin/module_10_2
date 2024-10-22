from threading import Thread
from time import sleep


class Knight(Thread):
    knights = []

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, power, enemies=100):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies
        Knight.knights.append(self)

    def run(self):
        count_days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.enemies -= self.power
            sleep(1)
            count_days += 1
            if self.enemies <= 0:
                print(f'{self.name} сражается {count_days} дней(дня), уже не осталось воинов.')
            else:
                print(f'{self.name} сражается {count_days} дней(дня), осталось {self.enemies} воинов.')
        else:
            print(f'{self.name} одержал победу спустя {count_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
third_knight = Knight('Илья Муромец', 30)
threads = []
for obj in Knight.knights:
    obj.start()
    threads.append(obj)
for thread in threads:
    thread.join()
print('Все битвы завершены!')
