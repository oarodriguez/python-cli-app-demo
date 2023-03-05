"""Demonstrate how to use the argparse module to make a CLI."""
import sys
from argparse import ArgumentParser, Namespace

APP_DESCRIPTION_TEXT = (
    "Command line interface built using the argparse module."
)

parser = ArgumentParser(
    description=APP_DESCRIPTION_TEXT, prog=f"{__package__}.useargparse"
)
parser.add_argument(
    "arg1", metavar="ARG1", type=str, help="Required program argument."
)
parser.add_argument(
    "--arg2", metavar="ARG2", type=str, help="First optional argument"
)
parser.add_argument(
    "--arg3", metavar="ARG3", type=str, help="Second optional argument."
)

if __name__ == "__main__":
    script_name = sys.argv[0]
    args: Namespace = parser.parse_args()
    arg_one = getattr(args, "arg1")
    arg_two = getattr(args, "arg2", None)
    arg_three = getattr(args, "arg3", None)
    num_args = sum(
        [
            int(arg_value is not None)
            for arg_value in (arg_one, arg_two, arg_three)
        ]
    )
    print(f"We passed {num_args} arguments to the program")
    print(f"  First argument: {arg_one}")
    if arg_two is not None:
        print(f"  Second argument: {arg_two}")
    if arg_three is not None:
        print(f"  Third argument: {arg_three}")
