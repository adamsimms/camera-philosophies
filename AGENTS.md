# Agent notes

camera-philosophies is a software-defined experimental camera platform for Raspberry Pi. Prefer one milestone (or one issue) per chat when the work is mechanical.

## What this is

Interpretive Camera MVP: documentary capture (`original`), context-shaped second image (`interpretive`), portable shot package. Not Fielding's rover payload. Not Dreamberry's generative window.

Canonical files: [README.md](README.md), `schemas/shot-package.schema.json`, `src/camera_philosophies/`.

## Private material

Private research notes live in the private studio repo (adamsimms/studio, `research/camera-philosophies/`). Nothing from studio comes into this repo unless Adam approves it. Never put a phone number or home address here; a global pre-commit guard blocks them.

## Bibliography / Zotero

Zotero is the source library (public library; no project collection yet, ask Adam). Writing to Zotero is publishing: only approved batches. Do not query `~/Zotero/zotero.sqlite`. Do not invent citations.

## Hard rules

- Do not invent hardware that is not in the README or code.
- Simulated capture stays simulated until a real Pi camera path is wired.
- Public twin is this README until a `docs/` tree exists.
- Secrets only via `.env`; see `.env.example`.

Docs policy and the decisions rule (work decision vs proposal choice vs option): [`.cursor/rules/docs.mdc`](.cursor/rules/docs.mdc). Until a `docs/` tree exists, the README is the brief.

## GitHub

Issues here are about the work. Applications, calls and their deadlines are tracked in the private studio repo, not here. Issue titles have no kind prefix; kind lives on labels.

## Project media

Photos, test captures, renders and video never stay in this repo's ignored folders: they are not backed up. They go to the project's media folder, `$MEDIA_DIR` (`30 STUDIO/32 PROJECTS/CAMERA-PHILOSOPHIES/`), a local outbox that a daily job copies to off-site storage and clears 14 days after the copies are verified. Older media is fetched from that storage, not read back from `$MEDIA_DIR`. Stages: `01-REFERENCES`, `02-STUDIES`, `03-TESTS`, `04-ARTWORK`, `05-DOCUMENTATION`. Inside 02 and 03, one dated folder per piece of work: `<YYYY-MM>-<NAME>`. `examples/output/` is a local cache of simulated runs.

## Support

No funder support to acknowledge yet. When an award lands, add the funder and its acknowledgement wording here and in the README.
