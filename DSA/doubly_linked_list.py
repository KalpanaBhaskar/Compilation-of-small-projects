class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail =None

    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            cur = self.head
            res =[]
            while cur.next:
                res.append(cur.value)
                cur = cur.next
            res.append(cur.value)
            return str(res)


    # O(n) - search
    def __contains__(self, item):
        cur = self.head
        while cur is not None:
            if cur.value == item:
                return True
            cur = cur.next
        return False
    
    # O(n) or could make it O(1) by adding size variable to node and +1/-1 in append/delete - lenjust returns the size variable
    def __len__(self):
        cur = self.head
        counter =0
        while cur is not None:
            counter +=1
            cur = cur.next
        return counter
    
        #O(n) runtime
    def append(self,value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:     
           new_node = Node(value)                 
           self.tail.next = new_node
           new_node.prev = self.tail
           
    # O(1)
    def prepend(self,value):
        cur = Node(value)       
        cur.next = self.head
        self.head = cur 
    
    #o(n)        
    def insert(self,value,index):
        if index ==0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                cur = self.head
                for i in range (index -1):
                    if cur.next is None:
                        raise ValueError("Index out of bounds")
                    cur= cur.next
                if cur is None:
                    raise ValueError("Index out of bounds")
                new_node = Node(value)
                new_node.next = cur.next
                cur.next= new_node    

    def delete(self,value):
        cur = self.head 
        if cur is not None:
            if cur.value == value:
                self.head=cur.next
                return
            while cur.next:
                if cur.next.value == value:
                    cur.next = cur.next.next
                    return                    
                cur = cur.next
    #O(n) worst case run time, n - len of linked list
    def pop(self,index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        for i in range(index - 1):
            if cur.next is None:
                raise ValueError("Index out of bounds")
            cur = cur.next
        if cur.next is None:
            raise ValueError("Index out of bounds")
        cur.next = cur.next.next
            

    def get(self,index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            cur = self.head
            for i in range(index):
                if cur.next is None:
                    raise ValueError("Index out of bounds")
                cur = cur.next
            return cur.value

if __name__ == "__main__":
    l1 = LinkedList()

    print("Initial List:")
    print(l1)
    print("Length:", len(l1))
    print()

    # append
    l1.append(10)
    print("After append(10):")
    print(l1)
    print("Length:", len(l1))
    print()

    l1.append(5)
    print("After append(5):")
    print(l1)
    print("Length:", len(l1))
    print()

    l1.append(18)
    print("After append(18):")
    print(l1)
    print("Length:", len(l1))
    print()

    l1.append(22)
    print("After append(22):")
    print(l1)
    print("Length:", len(l1))
    print()

    l1.append(29)
    print("After append(29):")
    print(l1)
    print("Length:", len(l1))
    print()

    # prepend
    l1.prepend(100)
    print("After prepend(100):")
    print(l1)
    print("Length:", len(l1))
    print()

    # insert
    l1.insert(200, 1)
    print("After insert(200, 1):")
    print(l1)
    print("Length:", len(l1))
    print()

    # contains
    print("18 in list?", 18 in l1)
    print("50 in list?", 50 in l1)
    print()

    # get
    print("Element at index 0:", l1.get(0))
    print("Element at index 3:", l1.get(3))
    print()

    # delete
    l1.delete(10)
    print("After delete(10):")
    print(l1)
    print("Length:", len(l1))
    print()

    # pop
    l1.pop(1)
    print("After pop(1):")
    print(l1)
    print("Length:", len(l1))
    print()

    # delete head
    l1.delete(100)
    print("After delete(100):")
    print(l1)
    print("Length:", len(l1))
    print()

    # prepend again
    l1.prepend(999)
    print("After prepend(999):")
    print(l1)
    print("Length:", len(l1))
    print()

    # pop head
    l1.pop(0)
    print("After pop(0):")
    print(l1)
    print("Length:", len(l1))
    print()

    # final list
    print("Final List:")
    print(l1)
    print("Final Length:", len(l1))