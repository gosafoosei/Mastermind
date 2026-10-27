#!/usr/bin/env python3
"""Build the self-contained ZIP distributed by the offline site button."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import os


ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "Mastermind-Simulations-Offline.zip"
TEMP_ARCHIVE = ARCHIVE.with_suffix(ARCHIVE.suffix + ".tmp")
EXCLUDED_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}


def main() -> None:
    try:
        with ZipFile(TEMP_ARCHIVE, "w", compression=ZIP_DEFLATED) as bundle:
            for directory, child_dirs, filenames in os.walk(ROOT):
                child_dirs[:] = sorted(name for name in child_dirs if name not in EXCLUDED_DIRS)
                current = Path(directory)
                for filename in sorted(filenames):
                    path = current / filename
                    if path in {ARCHIVE, TEMP_ARCHIVE} or filename in {"Thumbs.db", ".DS_Store"}:
                        continue
                    bundle.write(path, path.relative_to(ROOT).as_posix())
        os.replace(TEMP_ARCHIVE, ARCHIVE)
    finally:
        TEMP_ARCHIVE.unlink(missing_ok=True)

    print(f"Created {ARCHIVE.name} ({ARCHIVE.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
