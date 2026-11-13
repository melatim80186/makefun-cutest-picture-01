"""cutest-picture-01 entry (Python 3.13, standard library only).

Copies the picture held in entry.png beside this file to /output/entry.png,
byte for byte. The picture is a baby red panda cub hugging a giant daisy:
soft round shapes, big bright eyes, a head tilt and tiny paws wrapped around
the flower stem -- made to be cute at one glance and to read clearly even
small. The program does no network access and no computation that could vary
between runs, so two runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path  # standard library only; nothing is installed before the run


def main() -> int:
    here = Path(__file__).resolve().parent
    picture = (here / "entry.png").read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(picture)
    # Fail loudly rather than silently shipping a partial copy: the judge
    # sees exactly these bytes, so the written file must match the source.
    if target.read_bytes() != picture:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
