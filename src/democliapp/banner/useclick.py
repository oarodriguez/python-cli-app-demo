"""Demonstrate how to use the click library to make a CLI."""
from typing import Optional

from click import Group, argument, option

from democliapp.banner.banner import Banner

app = Group()


@app.command()
@argument("headline", type=str)
@option("--font", type=str, help="Suggest a font for the banner text.")
def show_banner(headline: str, font: Optional[str] = None):
    """Show a fancy banner with a HEADLINE using ASCII art."""
    banner = Banner(headline=headline, font_name=font)
    print(banner.text)


if __name__ == "__main__":
    show_banner()
