from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали!')
        flow = 100
        days = 0
        while flow > 0:
            sleep(1)
            days += 1
            flow -= self.power
            if flow < 0:
                flow = 0
            print(f'{self.name} сражается {days} суток, осталось {flow} воинов врага.')
        print(f'{self.name} одержал победу спустя {days} дней(я)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')