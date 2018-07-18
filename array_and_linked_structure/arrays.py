"""
File: arrays.py

An Array is like a list, but the client can use
only [], len, iter, and str.

To instantiate, use
<variable> = Array(<capacity>, <optional fill value>)

The fill value is None by default
"""


class Array(object):
    """
    Represents an array.
    """

    def __init__(self, capacity, fillValue = None):
        """
        :param capacity: the static size of the array
        :param fillValue: value that is placed at each position
        """
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """

        :return:The capacity of the array.
        """
        return len(self._items)

    def __str__(self):
        """

        :return:The string representation of the array.
        """
        return str(self._items)

    def __iter__(self):
        """

        :return: Supports traversal with a for loop.
        """
        return iter(self._items)
