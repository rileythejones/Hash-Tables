class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key 
        self.value = value
        self.prev = prev
        self.next = next
        
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, key, value):
        new_node = ListNode(key, value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        key, value = self.head.key, self.head.value
        self.delete(self.head)
        return key, value

    def add_to_tail(self, key, value):
        new_node = ListNode(key, value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        key, value = self.tail.key, self.tail.value
        self.delete(self.tail)
        return key, value

    def move_to_front(self, node):
        if node is self.head:
            return
        self.add_to_head(node.key, node.value)
        self.delete(node)

    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.key, node.value)
        self.delete(node)

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        current = self.head
        max = self.head.value

        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        return max

class HashTable:
    def __init__(self, CAPACITY):
        self.capacity = CAPACITY 
        self.size = 0 
        self.storage = []
        self.load_factor = self.size/self.capacity
        
        for x in range(0, self.capacity):
            DLL = DoublyLinkedList()
            self.storage.append(DLL)
        
    def djb2(self, key):
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        if self.load_factor > 0.7:
            self.resize()
            
        self.size += 1 
        index = self.hash_index(key)
        DLL = self.storage[index]
        DLL.add_to_head(key, value)

    def delete(self, key):
        index = self.hash_index(key)
        node = self.storage[index].head
        DLL = self.storage[index]
        while node:
            if node.key == key:
                DLL.delete(node)
                self.size -= 1
            node = node.next
            
        if (self.load_factor < 0.2) & (self.size > 128):
            self.resize(0.5)
                
    def get(self, key):
        index = self.hash_index(key)
        node = self.storage[index].head
        if node == None:
            return None
        while node.key != key:
            node = node.next 
        return node.value     
           
    def resize(self, size=2):
        old_storage = self.storage
        self.storage = []
        self.capacity = int(self.capacity*size)
        
        for x in range(self.capacity):
            DLL = DoublyLinkedList()
            self.storage.append(DLL)
            
        for DLL in old_storage:
            node = DLL.head
            while node:
                key = node.key
                value = node.value
                node = node.next
                self.put(key, value)

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
