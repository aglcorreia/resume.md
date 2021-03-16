from typing import List

import markdown
import argparse

def title(mdlines: List[str]) -> str:
    """
    Return the contents of the first markdown heading in mdlines, which we
    assume to be the title of the document.
    """
    for line in mdlines:
        if line[0] == "#":
            return line.strip("#").strip()
    raise ValueError("Cannot find any lines that look like markdown headings")


def make_html(mdlines: List[str], styles: str) -> str:
    """
    Compile mdlines to HTML and prepend/append preamble/postamble.
    """
    preamble = """
	<html lang="en">
	<head>
	<meta charset="UTF-8">
	<title>{title}</title>
	<link rel="stylesheet" type="text/css" href="{css_styles}">
	</head>
	<body>
	<div id="resume">
	"""

    postamble = """
	</div>
	</body>
	</html>
	"""
	
    return "".join(
        (
            preamble.format(title=mdlines[0], css_styles=styles),
            markdown.markdown("".join(mdlines), extensions=["extra"]),
            postamble,
        )
    )

def main():
    parser = argparse.ArgumentParser(description='Make an HTML resume from a markdown file.')
    parser.add_argument('input', type=str, help='The resume markdown file path.')
    parser.add_argument('output', type=str, help='The resume HTML output file path.')
    parser.add_argument('styles', type=str, help='The style sheet.')
    
    args = parser.parse_args()
    
    with open(args.input) as mdfp:
        mdlines = mdfp.readlines()
    with open(args.output, "w") as htmlfp:
        htmlfp.write(make_html(mdlines, args.styles))
    
if __name__ == "__main__":
    main()

