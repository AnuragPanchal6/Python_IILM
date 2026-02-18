class solution :
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       cr = 0 
       h = T = none
       while l1 or l2 or cr :
           temp =  l1.val if l1  