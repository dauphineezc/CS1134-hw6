from DoublyLinkedList import DoublyLinkedList


def copy_linked_list(lnk_lst):
    new_lst = DoublyLinkedList()
    for elem in lnk_lst:
        new_lst.add_last(elem)
    return new_lst


def deep_copy_linked_list(lnk_lst):
    new_lst = DoublyLinkedList()
    for elem in lnk_lst:
        if isinstance(elem, DoublyLinkedList):
            new_elem = deep_copy_linked_list(elem)
        else:
            new_elem = elem
        new_lst.add_last(new_elem)
    return new_lst
