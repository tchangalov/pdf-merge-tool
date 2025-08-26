import argparse
import re
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
import sys

def parse_page_range(range_str, total_pages):
    """Parse page ranges like 1-3,5 into zero-based page indices."""
    pages = set()
    for part in range_str.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            pages.update(range(start - 1, end))
        else:
            pages.add(int(part) - 1)
    return [p for p in sorted(pages) if 0 <= p < total_pages]

def merge_pdfs(inputs, output):
    writer = PdfWriter()

    for entry in inputs:
        if ':' in entry:
            path_str, range_str = entry.split(':', 1)
        else:
            path_str, range_str = entry, None

        path = Path(path_str)
        if not path.exists():
            print(f"Error: File not found: {path}")
            sys.exit(1)
        print(f"Reading {path}")
        reader = PdfReader(str(path))
        total_pages = len(reader.pages)

        if range_str:
            try:
                pages = parse_page_range(range_str, total_pages)
            except Exception as e:
                print(f"Error parsing range '{range_str}' in file '{path}': {e}")
                sys.exit(1)
        else:
            pages = range(total_pages)

        for p in pages:
            writer.add_page(reader.pages[p])

    with open(output, "wb") as out_f:
        writer.write(out_f)

    print(f"✅ Merged PDF saved to: {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Merge PDFs with optional page ranges. "
                    "Format: input1.pdf[:1-3,5] input2.pdf[:2-4] ..."
    )
    parser.add_argument("inputs", nargs="+", help="Input PDF files, optionally with page ranges")
    parser.add_argument("-o", "--output", required=True, help="Output PDF file path")

    args = parser.parse_args()
    merge_pdfs(args.inputs, args.output)
