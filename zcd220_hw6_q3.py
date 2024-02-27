from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.linked_list = DoublyLinkedList()
        if len(orig_str) > 0:
            prev_char = orig_str[0]
            count = 1
            for char in orig_str[1:]:
                if char == prev_char:
                    count += 1
                else:
                    self.linked_list.add_last((prev_char, count))
                    prev_char = char
                    count = 1
            self.linked_list.add_last((prev_char, count))

    def __add__(self, other):
        result = CompactString("")
        for elem in self.linked_list:
            result.linked_list.add_last(elem)
        for elem in other.linked_list:
            result.linked_list.add_last(elem)
        return result

    def __lt__(self, other):
        return str(self) < str(other)

    def __le__(self, other):
        return str(self) < str(other) or str(self) == str(other)

    def __gt__(self, other):
        return str(self) > str(other)

    def __ge__(self, other):
        return str(self) > str(other) or str(self) == str(other)

    def __repr__(self):
        current_node = self.linked_list.header.next
        result = ""
        while current_node != self.linked_list.trailer:
            key, value = current_node.data
            result += key * value
            current_node = current_node.next
        return result
