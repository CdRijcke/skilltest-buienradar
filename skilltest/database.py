from sqlmodel import SQLModel, Session, create_engine

from skilltest.datamodels import StationMeasurement, WeatherStations

_DB_PATH = "db/weather_data.db"
engine = create_engine(f"sqlite:///{_DB_PATH}")


def create_tables() -> None:
    SQLModel.metadata.create_all(engine)


def insert_weather_stations(stations: list[WeatherStations]) -> None:
    with Session(engine) as session:
        for station in stations:
            session.merge(station)
        session.commit()


def insert_station_measurements(measurements: list[StationMeasurement]) -> None:
    with Session(engine) as session:
        for measurement in measurements:
            session.merge(measurement)
        session.commit()
