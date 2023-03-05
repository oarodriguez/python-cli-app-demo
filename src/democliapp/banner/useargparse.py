"""Demonstrate how to use the argparse module to make a CLI."""
from argparse import ArgumentParser, Namespace

from .banner import Banner

APP_DESCRIPTION_TEXT = "Show a fancy banner using ASCII art."
FONT_OPT_HELP_TEXT = "Suggest a font for the banner text."

parser = ArgumentParser(
    description=APP_DESCRIPTION_TEXT, prog=f"{__package__}.useargparse"
)
parser.add_argument("headline", metavar="HEADLINE", type=str)
parser.add_argument(
    "--font",
    type=str,
    help=FONT_OPT_HELP_TEXT,
)

if __name__ == "__main__":
    args: Namespace = parser.parse_args()
    headline = getattr(args, "headline")
    font_name = getattr(args, "font", None)
    banner = Banner(headline=headline, font_name=font_name)
    print(banner.text)
