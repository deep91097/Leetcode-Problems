class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        cur_pointer = self.set[key % len(self.set)]
        while cur_pointer.next:
            if cur_pointer.next.key == key:
                return

            cur_pointer = cur_pointer.next

        cur_pointer.next = ListNode(key)    

        

    def remove(self, key: int) -> None:
        cur_pointer = self.set[key % len(self.set)]
        while cur_pointer.next:
            if cur_pointer.next.key == key:
                cur_pointer.next = cur_pointer.next.next 
                return

            cur_pointer = cur_pointer.next

    def contains(self, key: int) -> bool:
        cur_pointer = self.set[key % len(self.set)]
        while cur_pointer.next:
            if cur_pointer.next.key == key:
                return True

            cur_pointer = cur_pointer.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)