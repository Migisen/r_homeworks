from station import TrainStation
from train import Train

station_names = range(7)
station_types = [150, 150, 150, 50, 150, 50, 50, 150]

stations = [TrainStation(station_code=code, station_type=station_type) for code, station_type in
            zip(station_names, station_types)]

trains = []

for minute in range(1, 540):
    if minute % 5 == 0:
        trains.append(Train(departure_time=minute))
        for station in stations:
            for train in trains:
                if train.current_station == station.station_code and train.available is True:
                    people = train.load_people(station.people_amount)
                    station.people_amount -= people

    for train in trains:
        if train.available:
            train.update_station()

    for station in stations:
        station.update_time()

print('Done!')
