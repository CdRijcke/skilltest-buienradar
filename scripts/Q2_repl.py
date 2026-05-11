import json

from skilltest.datamodels import StationMeasurement, WeatherStations

with open("data/data_buienradar.json") as f:
    data = json.load(f)



data['actual']['stationmeasurements'][0]

# load data into datamodel
stations_measurements = [
    WeatherStations(**station) for station in data["actual"]["stationmeasurements"]
]
