import argparse
from .passgen import Password


def main():
    """Generate password based on command-line arguments."""
    args = parse_cmd_line_arguments()
    password = Password(args.length, args.no_digits, args.no_symbols)
    password.display_password()


def parse_cmd_line_arguments():
    """Set up parser and command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Random password generator'
    )
    parser.add_argument(
        '-l',
        '--length',
        default=8,
        help='the length of the password (defaults to 8)',
        metavar='',
        type=int
    )
    parser.add_argument(
        '--no-digits',
        action='store_true',
        help='generate a password without digits'
    )
    parser.add_argument(
        '--no-symbols',
        action='store_true',
        help='generate a password without symbols'
    )

    return parser.parse_args()
