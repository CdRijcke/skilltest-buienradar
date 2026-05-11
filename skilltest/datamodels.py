from datetime import datetime
from uuid import UUID, uuid4

from typing import Optional

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class WeatherStations(SQLModel, table=True):
    stationid: int = Field(primary_key=True)
    stationname: str
    lat: float
    lon: float
    regio: str

    measurements: list["StationMeasurement"] = Relationship(back_populates="station")


class StationMeasurement(SQLModel, table=True):
    def __init__(self, **data: object) -> None:
        # datetimes were read but internally represented as a string, not a datetime object. This is quite a crude fix
        # to resolve the issue, but not time for intensive debugging
        if isinstance(data.get("timestamp"), str):
            data["timestamp"] = datetime.fromisoformat(str(data["timestamp"]))
        super().__init__(**data)

    measurementid: UUID = Field(default_factory=uuid4, primary_key=True)
    # also a good option for measurementid would be a combination of a timestamp and stationid.
    # but no time to verify the uniqueness
    timestamp: datetime
    temperature: float | None = None
    groundtemperature: float | None = None
    feeltemperature: float | None = None
    windgusts: float | None = None
    windspeedBft: float | None = None
    humidity: float | None = None
    precipitation: float | None = None
    sunpower: float | None = None
    stationid: int = Field(foreign_key="weatherstations.stationid")

    station: Optional[WeatherStations] = Relationship(back_populates="measurements")

    @field_validator("temperature",
                     "groundtemperature",
                     "feeltemperature",
                     "windgusts",
                     "windspeedBft",
                     "humidity",
                     "precipitation",
                     "sunpower", mode="before")
    @classmethod
    def coerce_to_float(cls, v: int | float) -> float:
        return float(v)
