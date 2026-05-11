from sqlmodel import Session, select, col

from skilltest.database import engine
from skilltest.datamodels import StationMeasurement, WeatherStations


def get_weather_station_with_highest_temp():
    with Session(engine) as session:
        station_measurements = session.exec(
            select(StationMeasurement)
            .where(col(StationMeasurement.temperature).isnot(None))
            .order_by(col(StationMeasurement.temperature).desc())
            .limit(1)
        ).one()

    with Session(engine) as session:
        weather_station = session.get(WeatherStations, station_measurements.stationid)

    return (weather_station, station_measurements.temperature)
