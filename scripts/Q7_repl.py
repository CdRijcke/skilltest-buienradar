from skilltest.data_analysis import get_biggest_feel_temp_diff


measurement, station = get_biggest_feel_temp_diff()
print(measurement)
print(station)

if isinstance(measurement.temperature, float) and isinstance(measurement.feeltemperature, float):
    temp_diff = measurement.temperature - measurement.feeltemperature
    print(temp_diff)
