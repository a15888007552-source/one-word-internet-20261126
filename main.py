"""Write the one-word summary of the internet to /output/entry.txt.

Reads the output directory from MAKEFUN_OUTPUT_DIR when set, else /output.
"""

from pathlib import Path
import os

LINE = "doomscroll"

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
