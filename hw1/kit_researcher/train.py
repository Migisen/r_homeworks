import numpy as np


class Train:

    def __init__(self, departure_time):
        self.departure_time = departure_time
        self.people_amount = 0
        self.full = 0  # Вместимость поезда
        self.current_station = 0  # 0 - жулебино
        self.available = True
        self.next_station = 0

    def load_people(self, people_count):
        people_taken = 0
        for person in range(people_count):
            k = round(0.2 + self.current_station * 0.6, 1)
            prob = 1 - self.full ** k
            if np.random.choice([False, True], 1, p=[1 - prob, prob]):
                people_taken += 1
                self.full = (self.people_amount + people_taken) / 500
                if self.full == 1:
                    self.available = False
                    break

        self.people_amount += people_taken
        self.next_station = self.current_station + 1
        return people_taken

    def update_station(self):
        self.current_station = self.next_station
