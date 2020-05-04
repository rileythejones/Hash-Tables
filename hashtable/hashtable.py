class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, CAPACITY):
        self.capacity = CAPACITY 
        self.size = 0 
        self.storage = [None] * self.capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.size += 1 
        index = self.hash_index(key)
        node = self.storage[index]
        if node is None:
            self.storage[index] = HashTableEntry(key, value)

        prev = node 
        while node is not None:
            prev = node 
            node = node.next 

            prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        node = self.storage[index]

        prev = None

        while node is not None and node.key != key:
            prev = node 
            node = node.next 

            if node is None:
                return None

            else:
                self.size -= 1
                result = node.value

            if prev == None:
                node = None

            else: 
                prev.next = prev.next.next 

            return result 
                

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        node = self.storage[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None

        else:
            return node.value 



    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # self.capacity = self.capacity * 2 
        # for item in self.storage:

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
