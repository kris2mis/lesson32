class Transport:
    def __init__(self, width, length, number):
        self._width = width
        self._length = length
        self._number = number

    @property
    def square(self):
        return self._width + self._length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise Exception()

    @width.deleter
    def width(self):
        del self._width

    @property
    def length (self):
        return self._length

    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length
        else:
            raise Exception()

    @length.deleter
    def width(self):
        del self._length

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number =number

    @number.deleter
    def numberh(self):
        del self._number



    def __srt__(self):
        return f"width = {self._width}," \
               f"lengh = {self._length}," \
               f"number = {self._number}"
