from sqlalchemy import func
from sqlmodel import Session, col, select

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


def get_biggest_feel_temp_diff() -> tuple[StationMeasurement, WeatherStations | None]:
    with Session(engine) as session:
        diff = func.abs(col(StationMeasurement.feeltemperature) - col(StationMeasurement.temperature))
        measurement = session.exec(
            select(StationMeasurement)
            .where(col(StationMeasurement.feeltemperature).isnot(None))
            .where(col(StationMeasurement.temperature).isnot(None))
            .order_by(diff.desc())
            .limit(1)
        ).one()

    with Session(engine) as session:
        station = session.get(WeatherStations, measurement.stationid)

    return measurement, station


def get_north_sea_station() -> WeatherStations | None:
    with Session(engine) as session:
        return session.exec(
            select(WeatherStations)
            .where(WeatherStations.regio == "Noordzee")
        ).first()


def get_average_temperature() -> float | None:
    with Session(engine) as session:
        return session.exec(
            select(func.avg(StationMeasurement.temperature))
            .where(col(StationMeasurement.temperature).isnot(None))
        ).one()
