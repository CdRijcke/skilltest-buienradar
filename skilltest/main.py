import json

from skilltest.datamodels import StationMeasurement, WeatherStations
from skilltest.database import create_tables, insert_weather_stations, insert_station_measurements
from skilltest.data_analysis import get_weather_station_with_highest_temp


with open("data/data_buienradar.json") as f:
    data = json.load(f)


# Q1
stations_measurements = [
    StationMeasurement(**station) for station in data["actual"]["stationmeasurements"]
]


# Q2
weather_stations = [
    WeatherStations(**station) for station in data["actual"]["stationmeasurements"]
]


# Q3
create_tables()
insert_weather_stations(weather_stations)
insert_station_measurements(stations_measurements)


# Q5, weather station info and temperature. #TODO extend solution that returns all max stations that have the max temp.
# now only one is returned
weather_station, temp = get_weather_station_with_highest_temp()
