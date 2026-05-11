import json

from skilltest.datamodels import StationMeasurement, WeatherStations
from skilltest.database import create_tables, insert_weather_stations, insert_station_measurements
from skilltest.data_analysis import (get_north_sea_station,
                                     get_weather_station_with_highest_temp,
                                     get_average_temperature,
                                     get_biggest_feel_temp_diff)


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

# I chose to do the analysis with SQL functions.
# Pandas would also work fine, but if the dataset increases, working memory may become a limiting factor.

# Q5, weather station info and temperature. #TODO extend solution that returns all max stations that have the max temp.
# now only one is returned
weather_station, temp = get_weather_station_with_highest_temp()  # 'Meetstation Horst', 10.0 degrees celsius

# Q6 average temperature
avg_temp = get_average_temperature()  # 9.76 degrees celsius

# Q7
measurement, station = get_biggest_feel_temp_diff()  # 'Meetstation Zeeplatform F-3'
if isinstance(measurement.temperature, float) and isinstance(measurement.feeltemperature, float): # typecheck
    temp_diff = measurement.temperature - measurement.feeltemperature
    print(temp_diff)

# Q8
station = get_north_sea_station()  # 'Meetstation Zeeplatform F-3'

# Q9A: Automation
# deploy an application that is triggered every 10 minutes. (e.g. cronjob on a linux server)
# send the API call every 10 minutes to ensure that the data is retrieved (if the data is updated minutes later it is
# still retrieved)
# on data retrieval, load the data
# check if the data is new data.
    # if old: stop the process. the data should be present in the next run.
# if the data is new, load it into the database
# after loading the data, a different process can be started to apply analysis and update data elsewhere.
