"""Command line application definition."""
from argparse import ArgumentParser

USAGE_HELP_TEXT = "An educational, Pythonic Command Line Application."
main_parser = ArgumentParser(prog=__package__, description=USAGE_HELP_TEXT)


def execute():
    """Command line app main entry point."""
    # The main parser has not associated action. So, show the help message.
    main_parser.print_help()
