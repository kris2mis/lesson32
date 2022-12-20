from prod.model.entity import *


class Sorter:

    @staticmethod
    def sort(parking):
        if isinstance(parking, Parking):
            for i in range(len(parking) - 1):
                for index in range(len(parking) - 1 - i):
                    if parking[index].number > parking[index + 1].number:
                        temp = parking[index]
                        parking[index] = parking[index + 1]
                        parking[index + 1] = temp


# park = Parking(10)
# park.add(Transport(1, 1, "AAAAAA"))
# park.add(Transport(1, 1, "BBBB"))
# park.add(Transport(1, 1, "EEEEEEE"))
# park.add(Transport(1, 1, "CCC"))
#
# print(park)
