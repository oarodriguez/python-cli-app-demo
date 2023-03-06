"""Basic usage of ANSI escape codes."""


def print_with_foreground_color(text: str, color_code: int):
    """Print the given text using basic colors.

    :param text: The text to print.
    :param color_code: The color code.
    """
    print(f"\x1b[{color_code}m", end="")
    print(text, end="")
    print("\x1b[0m")


if __name__ == "__main__":
    for fg_color_code in range(30, 38):
        print_with_foreground_color("Drink Coffee!", color_code=fg_color_code)
