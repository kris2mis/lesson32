# from transport import Transport
from prod.model.entity import *


class Parking:
    DEFAULT_SIZE = 100

    def __init__(self, size=DEFAULT_SIZE):
        self._ls = []
        if size > 0:
            self._size = size
        else:
            self._size = Parking.DEFAULT_SIZE

    @property
    def _size(self):
        return self.size

    def __len__(self):
        return len(self._ls)

    def add(self, transport):
        if isinstance(transport, Transport):
            self._ls.append(transport)

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            return self._ls[index]
        else:
            raise Exception

    def __setitem__(self, index, value):
        if isinstance(index, int) and 0 <= index < len(self):
            self._ls[index] = value
        else:
            raise Exception

    def __delitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            del self._ls[index]
        else:
            raise Exception

    def __str__(self):
        if not self._ls:
            return "Parking is empty/ I is has {self._size} placec"
        else:
            msg = "Parking list ():\n"
            for transport in self._ls:
                msg += str(transport) + "\n"
            msg += "There are {self._size - len(self)} empte places"
            return msg
