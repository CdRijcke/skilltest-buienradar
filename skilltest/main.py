import json

from skilltest.datamodels import StationMeasurement

with open("data/data_buienradar.json") as f:
    data = json.load(f)

# load data into datamodel
stations_measurements = [
    StationMeasurement(**station) for station in data["actual"]["stationmeasurements"]
]
