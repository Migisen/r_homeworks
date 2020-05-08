import numpy as np


class TrainStation:

    def __init__(self, station_code, station_type):
        self.station_code = station_code  # Кодируем в цифры, 0 - депо etc.
        self.station_type = station_type  # 50 - промышленные, 150 - жилые
        self.people_amount = 0  # Количество людей на платформе станции
        self.time = 1  # Хз, пока, надо ли, но пусть будет
        self.states = np.zeros(541)

    def new_people(self):
        def sigmoid(x):
            return 1 / (1 + np.exp(-0.03 * x))

        def f(x):
            return sigmoid(x) * (1 - sigmoid(x))

        y = self.station_type * f(self.time - (self.station_code + 2) * 30)
        z = np.random.poisson(lam=y)
        self.time += 1
        self.people_amount += z
        self.states[self.time] = self.people_amount

    def update_time(self):
        self.new_people()
