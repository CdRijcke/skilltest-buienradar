from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class StationMeasurement(BaseModel):
    measurementid: UUID = Field(default_factory=uuid4)
    timestamp: datetime
    temperature: float | None = None
    groundtemperature: float | None = None
    feeltemperature: float | None = None
    windgusts: float | None = None
    windspeedBft: float | None = None
    humidity: float | None = None
    precipitation: float | None = None
    sunpower: float | None = None
    stationid: int


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


class WeatherStations(BaseModel):
    stationid: int
    stationname: str
    lat: float
    lon: float
    regio: str
