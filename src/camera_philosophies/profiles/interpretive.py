from __future__ import annotations

from dataclasses import dataclass

from .base import ProfileResult, ShotContext


@dataclass(frozen=True)
class InterpretiveProfile:
    name: str = "interpretive-v1"

    def transform(self, original_text: str, context: ShotContext) -> ProfileResult:
        mood = self._derive_mood(context)
        rhythm = self._derive_rhythm(context)
        palette = self._derive_palette(context)

        interpretive_text = (
            f"{original_text}\n"
            f"Interpretive overlay: mood={mood}; rhythm={rhythm}; palette={palette}; "
            f"context=({context.place_label}, {context.weather_condition}, {context.local_hour}:00)."
        )
        note = (
            f"{context.place_label} felt {mood} at {context.local_hour}:00, "
            f"with {context.weather_condition} air and a {rhythm} pace."
        )
        return ProfileResult(interpretive_text=interpretive_text, note=note)

    def _derive_mood(self, context: ShotContext) -> str:
        if context.weather_condition.lower() in {"rain", "storm"}:
            return "reflective"
        if context.local_hour < 7 or context.local_hour > 20:
            return "hushed"
        if context.temperature_c > 28:
            return "electric"
        return "open"

    def _derive_rhythm(self, context: ShotContext) -> str:
        if context.wind_kph > 25:
            return "restless"
        if context.humidity_percent > 75:
            return "heavy"
        return "steady"

    def _derive_palette(self, context: ShotContext) -> str:
        if context.weather_condition.lower() == "clear":
            return "warm highlights"
        if context.weather_condition.lower() in {"cloudy", "overcast"}:
            return "muted silver"
        return "split-tone dusk"
