from threading import Thread
from time import sleep


class Knight(Thread):
    knights = 0

    def __init__(self, name, power, enemies=100):
        super().__init__()
        self._name = name
        self.power = power
        self._enemies = enemies
        Knight.knights += 1

    def run(self):
        count_days = 0
        print(f'{self._name}, на нас напали!')
        while self._enemies > 0:
            self._enemies -= self.power
            sleep(1)
            count_days += 1
            print(f'{self._name} сражается {count_days} дней(дня), осталось {self._enemies} воинов.')
        else:
            print(f'{self._name} одержал победу спустя {count_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы завершены!')
