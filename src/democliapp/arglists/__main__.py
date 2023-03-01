"""Demonstrate how to use argument lists to make a CLI."""
import sys


def print_usage():
    """Show how to use the program."""
    print(f"Usage: {__package__} [-h] ARG1 [ARG2 [ARG3]]")
    print()
    print("Command line interface based on argument lists.")
    print()
    print("Options")
    print("  -h, --help: show this help message and exit.")
    # Finish the program with a SUCCESS status code.
    sys.exit(0)


# The script name is the first item in the argument list.
script_name: str
extra_args: list[str]
script_name, *extra_args = sys.argv
extra_args_count = len(extra_args)
if not extra_args_count or extra_args_count > 3:
    print(
        f"Incorrect program invocation. Use {__package__} -h to see the "
        f"the program correct usage."
    )
    # Finish the program with an error status code.
    sys.exit(1)

if extra_args_count == 1:
    first_arg = extra_args[0]
    if first_arg.strip() in ("--help", "-h"):
        print_usage()

print("Program invocation parameters")
print()
print("Script name")
print(f"  {script_name}")

print("Additional arguments")
print(f"  {extra_args}")

if extra_args_count == 3:
    arg_one, arg_two, arg_three = extra_args
    print("We passed three arguments to the program")
    print(f"First argument: {arg_one}")
    print(f"Second argument: {arg_two}")
    print(f"Third argument: {arg_three}")
elif extra_args_count == 2:
    arg_one, arg_two = extra_args
    print("We passed two arguments to the program")
    print(f"  First argument: {arg_one}")
    print(f"  Second argument: {arg_two}")
else:
    (arg_one,) = extra_args
    print("We passed one argument to the program")
    print(f"  First argument: {arg_one}")
