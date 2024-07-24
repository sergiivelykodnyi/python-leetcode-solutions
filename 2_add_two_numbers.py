import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_linked_list(arr):
    """ Convert an array to linked list """
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head


def linked_list_to_array(head):
    """ Convert a linked list to array """
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    dummy = ListNode(0)
    current = dummy

    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next

    return dummy.next


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        l1 = array_to_linked_list([2, 4, 3])
        l2 = array_to_linked_list([5, 6, 4])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_array(result), [7, 0, 8])

        l1 = array_to_linked_list([0])
        l2 = array_to_linked_list([0])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_array(result), [0])

        l1 = array_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = array_to_linked_list([9, 9, 9, 9])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_array(
            result), [8, 9, 9, 9, 0, 0, 0, 1])

        l1 = array_to_linked_list([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        l2 = array_to_linked_list([5, 6, 4])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_array(result), [
                         6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
