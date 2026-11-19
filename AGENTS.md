# Codex guidance – Xorsound Dark

Maintain a real, installable foobar2000 Mobile `.fbskin`, **not** a static design mockup.

- Source of truth is `src/Xorsound-Dark/`. Build artifact contains a top-level `Xorsound-Dark/` directory.
- Preserve UTF-16 LE with BOM for every `.txt` layout and `skindef.txt`; do not silently convert to UTF-8.
- Build with `python3 scripts/build.py`, test ZIP integrity and inspect its internal paths.
- Target iPhone 15 portrait, maintain additional layouts, and do not assert compatibility without actual app testing.
- Palette: `#101114` background; muted blue `#76B2D3`; light primary text and subdued grey.
- Preserve filename fallback and existing folder browsing; skin cannot be assumed to modify the app's browser behavior.
- Known v0.1.0 issue: MP3 may show `?-bit`. Use kbps for lossy codecs where supported.
- Check foobar2000 Mobile skin syntax before introducing new widget types or layout properties.
