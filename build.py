#!/usr/bin/env python3
"""Re-inline markdown content into note HTML files."""

import json, re, sys
from pathlib import Path

notes_dir = Path(__file__).parent / "notes"

pairs = [
    ("solid-state-theory.md", "solid-state-theory.html"),
]

for md_file, html_file in pairs:
    md_path = notes_dir / md_file
    html_path = notes_dir / html_file

    if not md_path.exists():
        print(f"SKIP {md_file} (not found)")
        continue

    md = md_path.read_text()
    html = html_path.read_text()

    # Replace the inlined markdown string in the JS
    replacement = f'const __md = {json.dumps(md)};'
    new_html = re.sub(
        r'const __md = ".*?";',
        lambda _: replacement,
        html,
        count=1,
        flags=re.DOTALL,
    )

    if new_html == html:
        print(f"WARN {html_file}: pattern not found, nothing changed")
    else:
        html_path.write_text(new_html)
        print(f"OK   {html_file} updated")
