#!/usr/bin/env python3
"""Build foobar2000 Mobile .fbskin from UTF-16 source and PNG assets."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
source = root / "src" / "Xorsound-Dark"
output = root / "dist" / "Xorsound-Dark.fbskin"
for layout in source.glob("*.txt"):
    if not layout.read_bytes().startswith((b"\xff\xfe", b"\xfe\xff")):
        raise SystemExit(f"Expected UTF-16 BOM: {layout}")
output.parent.mkdir(exist_ok=True)
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    for path in sorted(source.rglob("*")):
        if path.is_file():
            archive.write(path, path.relative_to(source.parent))
with ZipFile(output) as archive:
    assert archive.testzip() is None
print(output)
