import argparse
from .passgen import Password


def main():
    args = parse_cmd_line_arguments()
    password = Password(args.length)
    password.display_password()


def parse_cmd_line_arguments():
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

    return parser.parse_args()
