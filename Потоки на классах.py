import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
        self.enemies = 100

    def run(self):
        for i in range(1, 11):
            print(f"{self.name}, на нас напали!")
            print(f"{self.name}, сражается {i} день(дня)..., осталось {self.enemies} воинов.")
            self.enemies -= self.skill
            time.sleep(1)
            if self.enemies <= 0:
                print(f"{self.name} одержал победу спустя {i} дней!")
                break

knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()