# Future imports
from __future__ import annotations

# Standard library imports
from secrets import choice as secrets_choice
from typing import TYPE_CHECKING

from string import digits as string_digits
from string import hexdigits as string_hexdigits
from string import ascii_lowercase as string_lowercase
from string import octdigits as string_octdigits
from string import punctuation as string_punctuation
from string import ascii_uppercase as string_uppercase
from string import whitespace as string_whitespace
from string import printable as string_printable

# 3rd party imports

# Type checking
if TYPE_CHECKING:
    from typing import Optional

    from Configuration import Configuration


class Generator:
    def __init__(self, *, config: Optional[Configuration] = None, chars: Optional[str] = None,
                 length: Optional[int] = None, quantity: Optional[int] = None) -> None:
        self.__character_set: str
        self.__config: Configuration

        if config is not None and chars is not None:
            raise AttributeError('You cannot specify both a config and chars parameter.')
        elif config is not None:
            self.__config = config
            self.__character_set = self.generate_character_set()
        elif chars is not None:
            self.__config = None
            self.__character_set = chars
        else:
            raise AttributeError('You must specify at least one of config or chars.')

        self.__length: int = length
        self.__quantity: int = quantity
        return

    @property
    def character_set(self) -> str:
        """Returns character set"""
        return self.__character_set

    def generate_character_set(self) -> str:
        """Generates character set for generator"""
        # Starting character set from string
        characters: str = string_printable

        # Check if whitespace characters are not allowed
        if not self.__config.whitespace:
            for itr in string_whitespace:
                characters = characters.replace(itr, '')
        # Check if lowercase characters are not allowed
        if self.__config.no_lowercase:
            for itr in string_lowercase:
                characters = characters.replace(itr, '')
        # Check if uppercase characters are not allowed
        if self.__config.no_uppercase:
            for itr in string_uppercase:
                characters = characters.replace(itr, '')
        # Check if punctuation characters are not allowed
        if self.__config.no_punctuation:
            for itr in string_punctuation:
                characters = characters.replace(itr, '')

        # Check if hex-digit characters are not allowed
        if self.__config.no_hexdigits:
            for itr in string_hexdigits:
                characters = characters.replace(itr, '')
        # Check if digit characters are not allowed
        elif self.__config.no_digits:
            for itr in string_digits:
                characters = characters.replace(itr, '')
        # Check if oct-digit characters are not allowed
        elif self.__config.no_octdigits:
            for itr in string_octdigits:
                characters = characters.replace(itr, '')

        # Exclude any characters explicitly excluded
        for itr in self.__config.exclude_chars:
            characters = characters.replace(itr, '')

        # Include any characters explicitly included
        characters += self.__config.include_chars

        # Ensure that there are no duplicates
        base_set: str = ''.join(dict.fromkeys(characters))
        return base_set

    def generate_strings(self) -> tuple[str, ...]:
        """Generates the desired number of strings"""
        if self.__config:
            quantity = self.__config.quantity
            length = self.__config.length
        else:
            quantity = self.__quantity
            length = self.__length

        strings: list[str] = []
        for k in range(quantity):
            strings.append(''.join(secrets_choice(self.__character_set) for _ in range(length)))
        return tuple(strings)


if __name__ == '__main__':
    print('WARNING: Generator.py is a class file and should be imported.')
