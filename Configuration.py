# Future imports
from __future__ import annotations


class Configuration:
    def __init__(self, *, length: int = 32, quantity: int = 1, no_digits: bool = False, no_hexdigits: bool = False,
                 no_octdigits: bool = False, no_punctuation: bool = False, whitespace: bool = False,
                 no_uppercase: bool = False, no_lowercase: bool = False, exclude_chars: str = '',
                 include_chars: str = '', no_numbering: bool = False, output_file: str = '') -> None:
        self.__length: int = length
        self.__quantity: int = quantity
        self.__no_digits: bool = no_digits
        self.__no_hexdigits: bool = no_hexdigits
        self.__no_octdigits: bool = no_octdigits
        self.__no_punctuation: bool = no_punctuation
        self.__no_uppercase: bool = no_uppercase
        self.__no_lowercase: bool = no_lowercase
        self.__whitespace: bool = whitespace
        self.__no_numbering: bool = no_numbering
        self.__exclude_chars: str = exclude_chars
        self.__include_chars: str = include_chars
        self.__output_file: str = output_file
        return

    @property
    def length(self) -> int:
        """Returns the length attribute"""
        return self.__length

    @length.setter
    def length(self, value: int) -> None:
        """Sets the length to the specified value"""
        value = int(value)
        if value < 1:
            raise ValueError('The length must be greater than 0')

        self.__length = value
        return

    @property
    def quantity(self) -> int:
        """Returns the quantity attribute"""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """Sets the quantity to the specified value"""
        value = int(value)

        if value < 1:
            raise ValueError('The quantity must be greater than 0')

        self.__quantity = value
        return

    @property
    def no_digits(self) -> bool:
        """Returns the no_digits attribute"""
        return self.__no_digits

    @no_digits.setter
    def no_digits(self, value: bool) -> None:
        """Sets the no_digits to the specified value"""
        if type(value) != bool:
            raise TypeError('The specified value must be a boolean')

        self.__no_digits = value
        return

    @property
    def no_hexdigits(self) -> bool:
        """Returns the no_hexdigits attribute"""
        return self.__no_hexdigits

    @no_hexdigits.setter
    def no_hexdigits(self, value: bool) -> None:
        """Sets the no_hexdigits to the specified value"""
        if type(value) != bool:
            raise TypeError('The specified value must be a boolean')

        self.__no_hexdigits = value
        return

    @property
    def no_octdigits(self) -> bool:
        """Returns the no_octdigits attribute"""
        return self.__no_octdigits

    @no_octdigits.setter
    def no_octdigits(self, value: bool) -> None:
        """Sets the no_octdigits to the specified value"""
        if type(value) != bool:
            raise TypeError('The specified value must be a boolean')

        self.__no_octdigits = value
        return

    @property
    def no_punctuation(self) -> bool:
        """Returns the no_punctuation attribute"""
        return self.__no_punctuation

    @no_punctuation.setter
    def no_punctuation(self, value: bool) -> None:
        """Sets the no_punctuation to the specified value"""
        if type(value) != bool:
            raise TypeError('The specified value must be a boolean')

        self.__no_punctuation = value
        return

    @property
    def no_uppercase(self) -> bool:
        """Returns the no_uppercase attribute"""
        return self.__no_uppercase

    @no_uppercase.setter
    def no_uppercase(self, value: bool) -> None:
        """Sets the no_uppercase to the specified value"""
        if type(value) != bool:
            raise TypeError('The specified value must be a boolean')

        self.__no_uppercase = value
        return

    @property
    def no_lowercase(self) -> bool:
        """Returns the no_lowercase attribute"""
        return self.__no_lowercase

    @no_lowercase.setter
    def no_lowercase(self, value: bool) -> None:
        """Sets the no_lowercase to the specified value"""
        if type(value) != bool:
            raise TypeError('The specified value must be a boolean')

        self.__no_lowercase = value
        return

    @property
    def whitespace(self) -> bool:
        """Returns the whitespace attribute"""
        return self.__whitespace

    @whitespace.setter
    def whitespace(self, value: bool) -> None:
        """Sets the whitespace to the specified value"""
        if type(value) != bool:
            raise TypeError('The specified value must be a boolean')

        self.__whitespace = value
        return

    @property
    def exclude_chars(self) -> str:
        """Returns the exclude_chars attribute"""
        return self.__exclude_chars

    @exclude_chars.setter
    def exclude_chars(self, value: str) -> None:
        """Sets the exclude_chars to the specified value"""
        if type(value) != str:
            raise TypeError('The specified value must be a string')

        self.__exclude_chars = value
        return

    @property
    def include_chars(self) -> str:
        """Returns the include_chars attribute"""
        return self.__include_chars

    @include_chars.setter
    def include_chars(self, value: str) -> None:
        """Sets the include_chars to the specified value"""
        if type(value) != str:
            raise TypeError('The specified value must be a string')

        self.__include_chars = value
        return

    @property
    def no_numbering(self) -> bool:
        """Returns the no_numbering attribute"""
        return self.__no_numbering

    @no_numbering.setter
    def no_numbering(self, value: bool) -> None:
        """Sets the no_numbering to the specified value"""
        if type(value) != bool:
            raise TypeError('The specified value must be a boolean')

        self.__no_numbering = value
        return

    @property
    def output_file(self) -> str:
        """Returns the output_file attribute"""
        return self.__output_file

    @output_file.setter
    def output_file(self, value: str) -> None:
        """Sets the output_file to the specified value"""
        if type(value) != str:
            raise TypeError('The specified value must be a string')

        self.__output_file = value
        return


if __name__ == '__main__':
    print('WARNING: Generator.py is a class file and should be imported.')
