# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        self.last_node = None
        
        return self.traverse_recur(head)
        
    def traverse_recur(self, node):
        if node == None:
            return self.last_node
        else:
            new_node = ListNode(node.val)
            new_node.next = self.last_node
            self.last_node = new_node
            return self.traverse_recur(node.next)
            
