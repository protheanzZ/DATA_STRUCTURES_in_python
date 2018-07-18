class Node(object):
    """
    Represents a singly linked node.
    """

    def __init__(self, data, next=None):
        """
        Instantiates a Node with a default next of None.
        :param data:
        :param next:
        """
        self.data = data
        self.next = next
