class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.start = None


    def display_list(self):
        if self.start is None:
            print('List is empty')
            return
        else:
            print("list is: ")
            p = self.start
            while p is not None:
                print(p.value,end=" ")
                p = p.next
            print()

    def insert_in_beginning(self,value):
        temp = Node(value)
        temp.next = self.start
        self.start = temp

    def insert_at_end(self,data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
