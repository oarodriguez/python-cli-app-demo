"""Demonstrate how to use the click library to make a CLI."""
from typing import Optional

from click import Group, argument, option
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .banner import Banner

# Initialize the object that enables the CLI.
app = Group()

# Rich console object. We use it to enrich the terminal output.
console = Console()


@app.command()
@argument("headline", type=str)
@option("--font", type=str, help="Suggest a font for the banner text.")
@option(
    "--headline-style",
    type=str,
    help="Suggest a style to apply to the banner headline.",
    default=None,
)
@option(
    "--with-panel",
    is_flag=True,
    default=False,
    help="Add a panel around the headline.",
)
def show_banner(
    headline: str,
    font: Optional[str] = None,
    headline_style: Optional[str] = None,
    with_panel: bool = True,
):
    """Show a fancy banner with a HEADLINE using ASCII art."""
    banner = Banner(headline=headline, font_name=font)
    banner_content = Text(banner.text)
    banner_content.stylize(style=headline_style)
    if with_panel:
        banner_content = Panel(banner_content)
    console.print(banner_content)


if __name__ == "__main__":
    show_banner()
