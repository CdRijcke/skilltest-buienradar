import matplotlib.pyplot as plt
from sqlmodel import Session, col, select

from skilltest.database import engine
from skilltest.datamodels import StationMeasurement, WeatherStations


def plot_temperature_per_station() -> None:
    with Session(engine) as session:
        rows = session.exec(
            select(WeatherStations.stationname, StationMeasurement.temperature)
            .join(StationMeasurement, StationMeasurement.stationid == WeatherStations.stationid)
            .where(col(StationMeasurement.temperature).isnot(None))
            .order_by(col(StationMeasurement.temperature).desc())
        ).all()

    names = [row[0].replace("Meetstation ", "") for row in rows]
    temps: list[float] = [float(row[1]) for row in rows]

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.bar(names, temps, color="steelblue")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Temperature per weather station")
    ax.tick_params(axis="x", rotation=45)
    ax.set_xticklabels(names, ha="right")  # type: ignore[arg-type]
    plt.tight_layout()
    plt.show()
