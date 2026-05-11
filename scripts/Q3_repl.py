import json

from skilltest.datamodels import StationMeasurement, WeatherStations
from skilltest.database import create_tables, insert_weather_stations, insert_station_measurements

with open("data/data_buienradar.json") as f:
    data = json.load(f)

stations_measurements = [
    StationMeasurement(**station) for station in data["actual"]["stationmeasurements"]
]

weather_stations = [
    WeatherStations(**station) for station in data["actual"]["stationmeasurements"]
]

create_tables()
insert_weather_stations(weather_stations)
insert_station_measurements(stations_measurements)
