# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next_node = ListNode(0)
        init_node = ListNode(0,next_node)
        prev_node = init_node
        carry_over = 0
        carried = False

        while (l1 or l2):
            l1_add = l1.val if l1!=None else 0
            l2_add = l2.val if l2!=None else 0
            s = l1_add+l2_add + carry_over
            if carry_over==1:
                carry_over = 0
            if s>9:
                s%=10
                carry_over=1
            next_node.val+=s
            next_node.next = ListNode(0)
            prev_node = next_node
            next_node = next_node.next if (l1!=None or l2!=None) and not carried else None
            l1 = l1.next if l1!=None else None
            l2 = l2.next if l2!=None else None
            if l1==None and l2==None and carry_over == 1:
                    next_node.val=1
                    carried = True

        if not carried:
            prev_node.next = None
        return init_node.next
