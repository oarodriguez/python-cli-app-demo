"""Demonstrate how to use argument lists to make a CLI."""
import sys

PROGRAM_NAME = f"{__package__}.useargv"


def print_usage():
    """Show how to use the program."""
    print(f"Usage: {PROGRAM_NAME} [-h] ARG1 [ARG2 [ARG3]]")
    print()
    print("Command line interface based on argument lists.")
    print()
    print("Positional Arguments")
    print("  ARG1: Required program argument.")
    print()
    print("Optional Arguments")
    print("  ARG2: First optional argument.")
    print("  ARG3: Second optional argument.")
    print()
    print("Options")
    print("  -h, --help: show this help message and exit.")
    # Finish the program with a SUCCESS status code.
    sys.exit(0)


# The script name is the first item in the argument list. However, we do not
# use it.
extra_args: list[str]
_, *extra_args = sys.argv
extra_args_count = len(extra_args)
if not extra_args_count or extra_args_count > 3:
    print(
        f"Incorrect program invocation. Use {PROGRAM_NAME} -h to see the "
        f"the program correct usage."
    )
    # Finish the program with an error status code.
    sys.exit(1)

if extra_args_count == 1:
    first_arg = extra_args[0]
    if first_arg.strip() in ("--help", "-h"):
        print_usage()

if extra_args_count == 3:
    arg_one, arg_two, arg_three = extra_args
    print("We passed 3 arguments to the program")
    print(f"First argument: {arg_one}")
    print(f"Second argument: {arg_two}")
    print(f"Third argument: {arg_three}")
elif extra_args_count == 2:
    arg_one, arg_two = extra_args
    print("We passed 2 arguments to the program")
    print(f"  First argument: {arg_one}")
    print(f"  Second argument: {arg_two}")
else:
    (arg_one,) = extra_args
    print("We passed 1 argument to the program")
    print(f"  First argument: {arg_one}")
