from __future__ import annotations

import json
import uuid
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from src.camera_pi.profiles.base import ShotContext
from src.camera_pi.profiles.interpretive import InterpretiveProfile


def _simulated_capture() -> str:
    # Placeholder for Raspberry Pi sensor capture output path/content.
    return "Original capture: pedestrian crossing under cloudy afternoon light."


def _simulated_context() -> ShotContext:
    # Placeholder for live providers (GPS, weather, sensors, wearables).
    return ShotContext(
        latitude=45.5019,
        longitude=-73.5674,
        place_label="Montreal, QC",
        local_hour=16,
        weather_condition="cloudy",
        temperature_c=23.0,
        humidity_percent=68.0,
        wind_kph=18.0,
    )


def run() -> Path:
    shot_id = str(uuid.uuid4())
    captured_at = datetime.now(timezone.utc).isoformat()

    original_text = _simulated_capture()
    context = _simulated_context()
    profile = InterpretiveProfile()
    result = profile.transform(original_text=original_text, context=context)

    out_dir = Path("examples/output") / shot_id
    out_dir.mkdir(parents=True, exist_ok=True)

    original_path = out_dir / "original.txt"
    interpretive_path = out_dir / "interpretive.txt"
    note_path = out_dir / "note.txt"
    metadata_path = out_dir / "metadata.json"

    original_path.write_text(original_text + "\n", encoding="utf-8")
    interpretive_path.write_text(result.interpretive_text + "\n", encoding="utf-8")
    note_path.write_text(result.note + "\n", encoding="utf-8")

    metadata = {
        "id": shot_id,
        "captured_at": captured_at,
        "profile": profile.name,
        "files": {
            "original": str(original_path.name),
            "interpretive": str(interpretive_path.name),
        },
        "context": {
            "location": {
                "latitude": context.latitude,
                "longitude": context.longitude,
                "place_label": context.place_label,
            },
            "weather": {
                "condition": context.weather_condition,
                "temperature_c": context.temperature_c,
                "humidity_percent": context.humidity_percent,
                "wind_kph": context.wind_kph,
            },
            "time": {
                "local_hour": context.local_hour,
                "is_blue_hour": context.local_hour in {6, 20},
            },
            "raw_context": asdict(context),
        },
        "note": result.note,
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    return out_dir


if __name__ == "__main__":
    out = run()
    print(f"Wrote demo shot package to {out}")
