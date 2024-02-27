from DoublyLinkedList import DoublyLinkedList


class Integer:
    def __init__(self, num_string):
        self.data = DoublyLinkedList()
        for digit in num_string:
            self.data.add_last(int(digit))

    def __repr__(self):
        num_string = ''.join(str(digit) for digit in self.data)
        return num_string.lstrip('0') or '0'

    def __add__(self, other):
        carry = 0
        result = Integer('')

        node1 = self.data.trailer.prev
        node2 = other.data.trailer.prev

        while node1 is not None or node2 is not None or carry > 0:
            val1 = node1.data if node1 is not None and node1.data is not None else 0
            val2 = node2.data if node2 is not None and node2.data is not None else 0

            digit_sum = val1 + val2 + carry
            carry = digit_sum // 10
            digit_sum %= 10
            result.data.add_first(digit_sum)

            node1 = node1.prev if node1 is not None else self.data.delete_node(node1) if node1 is not None else None
            node2 = node2.prev if node2 is not None else other.data.delete_node(node2) if node2 is not None else None

        return result
