from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    result_list = DoublyLinkedList()
    node1 = srt_lnk_lst1.header.next
    node2 = srt_lnk_lst2.header.next

    def merge_sublists(node1, node2):
        if node1 is srt_lnk_lst1.trailer:
            while node2 is not srt_lnk_lst2.trailer:
                result_list.add_last(node2.data)
                node2 = node2.next
        elif node2 is srt_lnk_lst2.trailer:
            while node1 is not srt_lnk_lst1.trailer:
                result_list.add_last(node1.data)
                node1 = node1.next
        elif node1.data <= node2.data:
            result_list.add_last(node1.data)
            merge_sublists(node1.next, node2)
        else:
            result_list.add_last(node2.data)
            merge_sublists(node1, node2.next)

    merge_sublists(node1, node2)
    return result_list
