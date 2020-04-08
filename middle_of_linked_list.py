# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.


# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.


# Note:

# The number of nodes in the given list will be between 1 and 100.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def middleNode(head):
    current_node = head
    len_ll = 0

    while current_node:
        current_node = current_node.next
        len_ll += 1

    mid_idx = (len_ll//2) + 1
    mid_node = head

    while mid_idx > 1:
        mid_node = mid_node.next
        mid_idx -= 1

    return mid_node
