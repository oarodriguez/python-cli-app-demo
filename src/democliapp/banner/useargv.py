"""Demonstrate how to use argument lists to make a CLI."""
import sys

from .banner import Banner

PROGRAM_NAME = f"{__package__}.useargv"

DESCRIPTION_TEXT = """\
  Show a fancy banner with a HEADLINE using ASCII art.

Positional arguments:
  HEADLINE:     The banner headline.
  font-name:    Suggest a font for the banner text.
"""

BAD_USAGE_MESSAGE = f"""\
Incorrect command invocation. Use {PROGRAM_NAME} to see the the
program correct usage."""


def print_usage():
    """Show how to use the program."""
    print(f"Usage: {PROGRAM_NAME} HEADLINE [font-name]")
    print()
    print(DESCRIPTION_TEXT)


def get_cli_arguments():
    """Implement the logic to parse the CLI arguments."""
    # The script name is the first item in the argument list.
    script_name: str
    args: list[str]
    script_name, *args = sys.argv
    args_count = len(args)
    if not args_count:
        print_usage()
        sys.exit(0)
    if args_count > 2:
        print(BAD_USAGE_MESSAGE)
        # Finish the program with an error status code.
        sys.exit(1)
    if args_count == 2:
        headline, font_name = args
    else:
        (headline,) = args
        font_name = None
    return script_name, headline, font_name


if __name__ == "__main__":
    _, headline, font_name = get_cli_arguments()
    banner = Banner(headline=headline, font_name=font_name)
    print(banner.text)
