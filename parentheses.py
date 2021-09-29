from StackArray import Stack

def is_valid(expr):
    st = Stack()

    for ch in expr:
        if ch in '({[':
            st.push(ch)
        if ch in ')}]':
            if st.is_empty():
                print("Right parentheses are more than left parentheses")
                return False
            else:
                char = st.pop()
                if not match_parentheses(char,ch):
                    print("Mismathched parentheses are ", char, " and ", ch)
                    return False

    if st.is_empty():
        print("Balanced Parentheses")
        return True
    else:
        print("Left parentheses are more than right parenthesis")
        return False

def match_parentheses(leftPar, rightPar):
    if leftPar == '[' and rightPar == ']':
        return True
    if leftPar == '{' and rightPar == '}':
        return True
    if leftPar == '(' and rightPar == ')':
        return True
    return False

##########################################################

while True:
    print("Enter an expression with parentheses (q or quit): ", end = ' ')
    expression = input()
    
    if expression == "q":
        break
    if is_valid(expression):
        print("Valid expression")
    else:
        print("Invalid expression")
        
