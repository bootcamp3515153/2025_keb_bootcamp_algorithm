class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.data = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next: #if next node exist
            current = current.next
        current.next = Node(data)

if __name__ == "__main__":
    l = LinkedList()
    l.append(7)
    l.append(-11)