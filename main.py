# Future imports
from __future__ import annotations

# Standard library imports
from argparse import ArgumentParser
from typing import cast
from typing import TYPE_CHECKING

# Local imports
from Configuration import Configuration
from Generator import Generator

# Type checking
if TYPE_CHECKING:
    from typing import TextIO


def get_default_args() -> ArgumentParser:
    """Returns default ArgumentParser instance"""
    parser: ArgumentParser = ArgumentParser(prog='RandString')

    # Add arguments to parser
    parser.add_argument('--length', '-l',
                        nargs='?',
                        default=32,
                        help='how long to make the generated string.')
    parser.add_argument('--quantity', '-q',
                        nargs='?',
                        default=1,
                        help='how many strings to generate.')
    parser.add_argument('--no-digits', '-d',
                        action='store_true',
                        default=False,
                        help='disables the use of digits.')
    parser.add_argument('--no-hexdigits', '-f',
                        action='store_true',
                        default=False,
                        help='disables the use of hexdigits.')
    parser.add_argument('--no-octdigits', '-o',
                        action='store_true',
                        default=False,
                        help='disables the use of octdigits.')
    parser.add_argument('--no-punctuation', '-p',
                        action='store_true',
                        default=False,
                        help='disables the use of punctuation.')
    parser.add_argument('--whitespace', '-w',
                        action='store_true',
                        default=False,
                        help='enables the use of whitespace.')
    parser.add_argument('--exclude-chars', '-e',
                        default='',
                        help='excludes the specified characters. (Does not support whitespace characters)')
    parser.add_argument('--include-chars', '-i',
                        default='',
                        help='includes the specified characters. '
                             '(This will re-add the characters after all other checks)')
    parser.add_argument('--no-numbering', '-n',
                        action='store_true',
                        default=False,
                        help='disables numbering of the output')
    parser.add_argument('--output-file', '-F',
                        nargs='?',
                        const='./generated_strings.txt',
                        default='',
                        help='sets the output file')
    return parser


def main() -> None:
    """Main function"""
    # TODO: Implement the ability to copy to clipboard from command line tool (secretly).
    #   Add multiprocessing for anything over 1000 generated strings
    #   Add CSV output support (custom delimiter)
    #   Ensure included characters and excluded chars are ascii/UTF-8
    configuration: Configuration = Configuration()

    parser: ArgumentParser = get_default_args()
    config: Configuration = cast(Configuration, parser.parse_args(namespace=configuration))

    generator = Generator(config=config)

    strings: tuple[str, ...] = generator.generate_strings()

    k: int
    string: str
    output: str
    if not config.no_numbering and not config.output_file:
        output = '\n'.join(f'{k:{len(str(config.quantity))}}: {string}' for k, string in enumerate(strings, start=1))
    else:
        output = '\n'.join(strings)

    f: TextIO
    if config.output_file:
        with open(config.output_file, 'w') as f:
            f.write(output)
            f.close()
    else:
        print(output)
    return


if __name__ == '__main__':
    main()
