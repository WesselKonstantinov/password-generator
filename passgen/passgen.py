import secrets
import string


LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL_CHARS = string.punctuation


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

    def __init__(self, length):
        """
        Parameters
        ----------
        length : int
            The length of the password
        """

        self._generator = _PasswordGenerator(length)

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
        print(f'Generated the following password: {password}')


class _PasswordGenerator:
    """
    A class used to represent a PasswordGenerator

    ...

    Attributes
    ----------
    _length : int
        the length of the password to generate
    _password : str
        the password to be created

    Methods
    -------
    create_password()
        Creates and returns a new password
    """

    def __init__(self, length):
        """
        Parameters
        ----------
        length : int
            The length of the password
        """

        self._length = length
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

        all_chars = f'{LETTERS}{DIGITS}{SPECIAL_CHARS}'
        self._password = ''.join(secrets.choice(all_chars)
                                 for i in range(self._length))
        return self._password
