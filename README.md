# Xorsound Dark

A minimal dark foobar2000 Mobile skin for iPhone. **Version 0.1.0 was installed and visually tested on iPhone 15.** Independent project, not affiliated with foobar2000.

## Design
- Background: `#101114`
- Off-white typography, grey secondary labels and muted blue `#76B2D3` accents
- Large square artwork, transport controls, and seek bar
- Track title fallback: `$if3(%title%,%filename%,Unknown track)`

## Repository layout
- `src/Xorsound-Dark/` – UTF-16 with BOM skin definitions and PNG assets
- `scripts/build.py` – assembles the installable ZIP-based `.fbskin`
- `dist/Xorsound-Dark.fbskin` – tested 0.1.0 release build

## Build
```sh
python3 scripts/build.py
```

## Install
Copy `dist/Xorsound-Dark.fbskin` to iPhone Files; in foobar2000 Mobile, select **Choose Skin → Browse for skin file…**.

## Version 0.2 roadmap
- Fix lossy audio metadata: MP3 currently displays `?-bit`; show bitrate instead
- Consider album and year display
- Reduce vertical spacing while preserving large controls
- Test long filenames, missing tags, landscape and safe areas

**Device compatibility is verified only for the user's iPhone 15 screenshot of v0.1.0.** Other devices/layouts require testing.
