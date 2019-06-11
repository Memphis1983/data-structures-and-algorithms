"""
Python version 3.7.0
2.1 - Remove Dups
Write code to remove duplicates
from an unsorted linked list.
How would you solve this if a temporary
buffer is not allowed?
"""
import unittest
from typing import List


class Node:
    def __init__(self, d: int):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self, initial_value: int = None):
        self.head = None
        if initial_value is not None:
            self.head = Node(initial_value)

    def append_to_tail(self, d: int) -> None:
        if self.head is None:
            self.head = Node(d)
            return
        end = Node(d)
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = end

    def append_to_head(self, d: int) -> None:
        new_head = Node(d)
        new_head.next = self.head
        self.head = new_head

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.head is None:
            return '<empty>'
        ll = []
        n = self.head
        while n.next is not None:
            ll.append('{} -> '.format(n.data))
            n = n.next
        ll.append(str(n.data))
        return ''.join(ll)

    def __eq__(self, other):
        a = self.head
        b = other.head
        while a is not None and b is not None:
            if a.data != b.data:
                return False
            # otherwise, advance both pointers
            a = a.next
            b = b.next
        return a is None and b is None


def build_linked_list(numbers: List[int]) -> LinkedList:
    ll = LinkedList()
    for num in numbers:
        ll.append_to_tail(num)
    return ll


def remove_dups(ll: LinkedList) -> LinkedList:
    """
    remove_dups will remove duplicates from the
    input linked list ll. A temporary buffer
    is used.
    Runtime: O(N)
    Space Complexity: O(N)
    :param ll: a linked list
    :return: a linked list without duplicates
    """
    n = ll.head
    unique_vals = {n.data}  # set literal
    output_ll = LinkedList(n.data)
    while n is not None:
        if n.data not in unique_vals:
            output_ll.append_to_tail(n.data)
        unique_vals.add(n.data)
        n = n.next
    return output_ll


def remove_dups_no_buffer(ll: LinkedList) -> LinkedList:
    """
    remove_dups will remove duplicates from the
    input linked list ll. No temporary buffer
    used.
    Runtime: O(N^2)
    Space Complexity: O(1)
    :param ll: a linked list
    :return: a linked list without duplicates
    """
    n = ll.head
    while n is not None:
        curr_data = n.data
        m = n.next
        prev = n
        # search for duplicates from n + 1 to the
        # end of the linked list
        while m is not None:
            if m.data == curr_data:
                # re-arrange pointers to omit
                # the duplicate
                prev.next = m.next
            else:
                # otherwise, advance m and prev pointers
                prev = m
            m = prev.next
        n = n.next
    return ll


class TestRemoveDups(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            (
                build_linked_list([1, 2, 3, 3, 5]),
                build_linked_list([1, 2, 3, 5])
            ),
            (
                build_linked_list([1, 2, 3, 3]),
                build_linked_list([1, 2, 3])
            ),
            (
                build_linked_list([1, 2, 2]),
                build_linked_list([1, 2])
            ),
            (
                build_linked_list([1]),
                build_linked_list([1])
            ),
            (
                build_linked_list([1, 1]),
                build_linked_list([1])
            ),
            (
                build_linked_list([2, 2, 2, 2, 2, 2]),
                build_linked_list([2])
            ),
            (
                build_linked_list([1, 1, 3, 4, 5, 5, 6, 7]),
                build_linked_list([1, 3, 4, 5, 6, 7])
            ),
            (
                build_linked_list([7, 2, 7, 9, 20, 1, 0, 0, 0, 25]),
                build_linked_list([7, 2, 9, 20, 1, 0, 25])
            ),
            (
                build_linked_list([9, 8, 7, 6, 6, 1, 2, 3, 4, 4]),
                build_linked_list([9, 8, 7, 6, 1, 2, 3, 4])
            ),
            (
                build_linked_list([9, 9, 9, -10, -100, 45, 67, -100, 99]),
                build_linked_list([9, -10, -100, 45, 67, 99])
            )
        ]

    def test_remove_dups(self):
        for ll, expected in self.test_cases:
            self.assertEqual(remove_dups(ll), expected)

    def test_remove_dups_no_buffer(self):
        for ll, expected in self.test_cases:
            self.assertEqual(remove_dups_no_buffer(ll), expected)


if __name__ == '__main__':
    unittest.main()
