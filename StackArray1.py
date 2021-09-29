class StackEmptyError(Exception):
    pass

class StackFullError(Exception):
    pass

class Stack:

    def __init__(self,max_size=10):
        self.items = [None] * max_size
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0
    
    def is_full (self):
        return self.count == len (self.items)

    def push(self,x):
        if self.is_full():
            raise StackFullError("Stack is full, cant push")
        self.items[self.count] = x
        self.count += 1

    def pop(self):
        
        if self.is_empty():
            raise StackEmptyError("Stack is empty, cant pop")

        x = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count -= 1
        return x
        
    def peek(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty, cant peek")
        

        return self.items[self.count-1]
    
                          

    def display(self):
                          
        print(self.items)

##############################################################

if __name__ == "__main__":

    st = Stack(8)

    while True:
        print("1.Push")
        print("2.Pop")
        print("3.peek")
        print("4.Size")
        print("5.Display")
        print("6.Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            x = int(input("Enter the element to be pushed: "))
            st.push(x)

        elif choice == 2:
            x = st.pop()
            print("Popped element is : ", x)
        elif choice == 3:
            print("Elemnet at top is : ", st.peek())
        elif choice == 4:
            print("size of stack ", st.size())
        elif choice == 5:
            st.display()
        elif choice == 6:
            break
        else:
            print("Wrong Choice")
        print()
                          
                          
                          

    
                          
                          
                          
                          
        
    
