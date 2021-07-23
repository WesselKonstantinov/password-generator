import secrets
import string
from rich import print as rprint

LETTERS = string.ascii_letters
DIGITS = string.digits
SYMBOLS = string.punctuation


class Password:
    """
    A class used to represent a Password

    ...

    Attributes
    ----------
    _generator : _PasswordGenerator
        the generator that creates the password

    Methods
    -------
    display_password()
        Prints the newly generated password to the terminal
    """

    def __init__(self, length, no_digits=False, no_symbols=False):
        """
        Parameters
        ----------
        length : int
            The length of the password
        no_digits: bool
            Whether the password must contain digits or not
        no_symbols: bool
            Whether the password must contain symbols or not
        """

        self._generator = _PasswordGenerator(length, no_digits, no_symbols)

    def display_password(self):
        """Prints the newly generated password to the terminal.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        password = self._generator.create_password()
        rprint(f'Generated password: [bold yellow]{password}[/bold yellow]')


class _PasswordGenerator:
    """
    A class used to represent a PasswordGenerator

    ...

    Attributes
    ----------
    _length : int
        the length of the password to generate
    _no_digits: bool
        whether the password must contain digits or not
    _no_symbols: bool
        whether the password must contain symbols or not
    _password : str
        the password to be created

    Methods
    -------
    create_password()
        Creates and returns a new password
    """

    def __init__(self, length, no_digits=False, no_symbols=False):
        """
        Parameters
        ----------
        length : int
            The length of the password
        no_digits: bool
            Whether the password must contain digits or not
        no_symbols: bool
            Whether the password must contain symbols or not
        """

        self._length = length
        self._no_digits = no_digits
        self._no_symbols = no_symbols
        self._password = ''

    def create_password(self):
        """Creates and returns a new password.

        Parameters
        ----------
        None

        Returns
        -------
        self._password : str
            The newly generated password
        """

        all_chars = LETTERS
        if not self._no_digits:
            all_chars += DIGITS
        if not self._no_symbols:
            all_chars += SYMBOLS

        self._password = ''.join(secrets.choice(all_chars)
                                 for i in range(self._length))
        return self._password
