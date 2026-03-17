# 39.Reverse a Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    return prev

#40. Detect loop in linkedlist
def hasCycle(head):
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
        if slow == fast:          # They met! A cycle exists
            return True
            
    return False                  # Fast reached the end

#41.find middle node
def middleNode(head):
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # For even lists, slow ends up on the second middle node automatically
    return slow

#42.Merge two sorted linkedlists
def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    # If one list is longer, attach the remainder
    tail.next = list1 if list1 else list2
    
    return dummy.next