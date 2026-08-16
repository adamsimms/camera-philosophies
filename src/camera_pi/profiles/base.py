from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ShotContext:
    latitude: float
    longitude: float
    place_label: str
    local_hour: int
    weather_condition: str
    temperature_c: float
    humidity_percent: float
    wind_kph: float


@dataclass(frozen=True)
class ProfileResult:
    interpretive_text: str
    note: str


class CameraProfile(Protocol):
    name: str

    def transform(self, original_text: str, context: ShotContext) -> ProfileResult:
        """Return interpretive output and atmosphere note."""
