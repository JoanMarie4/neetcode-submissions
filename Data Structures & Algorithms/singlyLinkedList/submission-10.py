class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        node = self.head.next
        i = 0
        while node:
            if i == index:
                return node.val
            i += 1
            node = node.next
        
        return -1
        

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        if not node.next:
            self.tail = node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        node = self.head
        for _ in range(index):
            if node.next != None:
                node = node.next
            else:
                return False

        if node and node.next:
            if node.next == self.tail:
                self.tail = node
            node.next = node.next.next
            return True

        return False
        
        

    def getValues(self) -> List[int]:
        node = self.head.next
        res = []
        while node:
            res.append(node.val)
            node = node.next

        return res
        
