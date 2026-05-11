import numpy as np
import matplotlib.pyplot as plt
from sqlmodel import Session, col, select

from skilltest.database import engine
from skilltest.datamodels import StationMeasurement, WeatherStations


def plot_temperature_per_station() -> None:
    with Session(engine) as session:
        rows = session.exec(
            select(WeatherStations.stationname, StationMeasurement.temperature, StationMeasurement.feeltemperature)
            .join(StationMeasurement, StationMeasurement.stationid == WeatherStations.stationid)
            .where(col(StationMeasurement.temperature).isnot(None))
            .where(col(StationMeasurement.feeltemperature).isnot(None))
            .order_by(col(StationMeasurement.temperature).desc())
        ).all()

    names = [row[0].replace("Meetstation ", "") for row in rows]
    temps: list[float] = [float(row[1]) for row in rows]
    # feel_temps: list[float] = [float(row[2]) for row in rows]
    diff_temps: list[float] = [abs(float(row[1] - row[2])) for row in rows]

    avg = sum(temps) / len(temps)

    x = np.arange(len(names))
    width = 0.4
    fig, ax = plt.subplots(figsize=(14, 6))  # type: ignore[arg-type]
    ax.bar(x - width / 2, temps, width, color="steelblue", label="Temperature")  # type: ignore[arg-type]
    ax.bar(x + width / 2, diff_temps, width, color="orange", label="Temp / feel-temp diff")  # type: ignore[arg-type]
    ax.axhline(avg, color="red", linestyle="--", linewidth=1.5, label=f"Average ({avg:.1f} °C)")  # type: ignore[arg-type]
    ax.legend()  # type: ignore[arg-type]
    ax.set_ylabel("Temperature (°C)")  # type: ignore[arg-type]
    ax.set_title("Temperature per weather station (station in the North Sea is highlighted in red)")  # type: ignore[arg-type]
    ax.set_xticks(x)  # type: ignore[arg-type]
    ax.set_xticklabels(names, ha="right", rotation=45)  # type: ignore[arg-type]
    for label in ax.get_xticklabels():  # type: ignore[arg-type]
        if "Zeeplatform F-3" in label.get_text():
            label.set_color("red")
    plt.tight_layout()
    plt.show()  # type: ignore[arg-type]
