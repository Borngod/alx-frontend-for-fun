#!/usr/bin/env python3
"""
markdown2html.py

Converts a Markdown file to HTML with support for Headings.

Usage:
    ./markdown2html.py <markdown_file> <output_file>

Requirements:
- PEP 8 style (version 1.7.*)
- All files must be executable
- All modules should be documented: python3 -c 'print(__import__("markdown2html").__doc__)'
- Code should not be executed when imported (by using if __name__ == "__main__":)
"""

import sys
import os
import markdown2

def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML.

    :param markdown_file: The input Markdown file.
    :param output_file: The output HTML file.
    """
    try:
        with open(markdown_file, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()
            html_content = markdown2.markdown(markdown_content)
            with open(output_file, 'w', encoding='utf-8') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)
