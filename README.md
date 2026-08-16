# camera-philosophies

Software-defined experimental camera platform for Raspberry Pi.

Repo: [adamsimms/camera-philosophies](https://github.com/adamsimms/camera-philosophies)

This repository starts with an MVP called the **Interpretive Camera**:

- capture a documentary image (`original`)
- generate a second context-shaped image (`interpretive`)
- store a portable shot package with metadata and a short note

## MVP Scope

`v0.1` includes:

- shot package schema (`schemas/shot-package.schema.json`)
- profile/plugin interface (`src/camera_philosophies/profiles/base.py`)
- interpretive profile (`src/camera_philosophies/profiles/interpretive.py`)
- local pipeline demo (`src/camera_philosophies/pipeline/run_demo.py`)

## Quick Start

```bash
PYTHONPATH=src python -m camera_philosophies.pipeline.run_demo
```

Then inspect `examples/output/`.

## Next Hardware Step

Replace the simulated capture with Raspberry Pi camera capture and connect real context providers (GPS, weather API, sensor stack, optional wearable input).
