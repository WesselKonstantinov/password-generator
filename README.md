# Random password generator
A command-line tool that can be used for creating random passwords.

## Setup
1. `git clone https://github.com/WesselKonstantinov/password-generator && cd password-generator`
2. `pip install -r --user requirements.txt`

## Usage
### Help
Run `python3 password.py -h` or `python3 password.py --help` for an overview of all commands:
```
$ python3 password.py -h
usage: password.py [-h] [-l] [-nd] [-ns] [-c]

Random password generator

optional arguments:
  -h, --help         show this help message and exit
  -l , --length      the length of the password (defaults to 8)
  -nd, --no-digits   generate a password without digits
  -ns, --no-symbols  generate a password without symbols
  -c, --copy         copy the password to the clipboard
```

### Optional arguments
#### -l/--length
If the password length is not specified, the program generates a password that consists of 8 characters:
```
$ python3 password.py
Generated password: qkO!x&h}
```

Otherwise, if the length is specified (e.g. 10), the program will produce a password of 10 characters:
```
$ python3 password.py --length 10
Generated password: p@M/dfgMv}
```

#### -nd/--no-digits
This optional argument can be used to generate a password without digits:
```
$ python3 password.py --length 10 --no-digits
Generated password: MVvYvVnj#C
```

##### -ns/--no-symbols
This optional argument is used to generate a password without special characters:
```
$ python3 password.py --no-symbols
Generated password: FCiHPXyO
```

#### -c/--copy
Finally, it is possible to copy the newly generated to the clipboard using this optional argument:
```
$ python3 password.py --length 12 --copy
Generated password: +F^3;A$UlR}W
Copied the new password to the clipboard.
```