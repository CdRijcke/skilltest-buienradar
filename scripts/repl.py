import json

from skilltest.datamodels import StationMeasurement

with open("data/data_buienradar.json") as f:
    data = json.load(f)

# load data into datamodel
stations_measurements = [
    StationMeasurement(**station) for station in data["actual"]["stationmeasurements"]
]






### scripting
stations_measurements = data["actual"]["stationmeasurements"]


for index, station in enumerate(stations_measurements):
    try:
        StationMeasurement(**station)
    except:
        print(index)
        print(station)
        break


station["temperature"]
StationMeasurement(**station)

stations_measurements[0]
