# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp_pointer_l1 = l1
        temp_pointer_l2 = l2

        sum_l = ListNode()
        temp_pointer_sum = sum_l
        temp_pointer_sum.val = 0
        temp_pointer_sum.next = None
        additional_value = 0

        while temp_pointer_l1 != None or temp_pointer_l2 != None:
            if temp_pointer_l1 != None:
                temp_value_l1 = temp_pointer_l1.val
                temp_pointer_l1 = temp_pointer_l1.next
            else:
                temp_value_l1 = 0
            if temp_pointer_l2 != None:
                temp_value_l2 = temp_pointer_l2.val
                temp_pointer_l2 = temp_pointer_l2.next
            else:
                temp_value_l2 = 0

            # print(additional_value)
            sum_l_value = temp_value_l1 + temp_value_l2 + additional_value
            current_value = sum_l_value % 10
            additional_value = sum_l_value // 10

            temp_pointer_sum.val = current_value
            if temp_pointer_l1 == None and temp_pointer_l2 == None:
                if additional_value > 0:
                    temp_pointer_sum.next = ListNode()
                    temp_pointer_sum = temp_pointer_sum.next
                    temp_pointer_sum.val = additional_value
                    temp_pointer_sum.next = None
                else:
                    temp_pointer_sum.next = None
            else:
                temp_pointer_sum.next = ListNode()
                temp_pointer_sum = temp_pointer_sum.next
        
        return sum_l
