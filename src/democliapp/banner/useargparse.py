"""Demonstrate how to use the argparse module to make a CLI."""
from argparse import ArgumentParser, Namespace

from .banner import Banner

PROGRAM_NAME = f"{__package__}.useargparse"

parser = ArgumentParser(
    description="Show a fancy banner with a HEADLINE using ASCII art.",
    prog=f"{PROGRAM_NAME}",
)
parser.add_argument(
    "headline", metavar="HEADLINE", type=str, help="The banner headline."
)
parser.add_argument(
    "--font",
    type=str,
    help="Suggest a font for the banner text.",
)

if __name__ == "__main__":
    args: Namespace = parser.parse_args()
    banner = Banner(
        headline=getattr(args, "headline"),
        font_name=getattr(args, "font", None),
    )
    print(banner.text)
