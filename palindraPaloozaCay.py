class Node:
    def __init__(self, data):
        # Constructor for Node class
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # Constructor for Stack class
        self.top = None

    def push(self, data):
        # Push operation: insert a new node at the top of the stack
        new_node = Node(data)
        if self.top is None:
            # If the stack is empty, set the new node as the top
            self.top = new_node
            self.top.next = None
        else:
            # If the stack is not empty, adjust pointers to insert at the beginning
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        # Pop operation: remove the node from the top of the stack
        if self.top is None:
            # If the stack is empty, print a message
            print("Stack is empty")
        elif self.top.next is None:
            # If the stack has only one element, set the top to None
            self.top = None
        else:
            # If the stack has more than one element, adjust pointers to remove from the beginning
            temp = self.top
            self.top = temp.next
            temp = None

    def display(self):
        # Display the elements of the stack
        if self.top is None:
            print("Empty Stack")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

def is_palindrome(sentence):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalnum())

    # Check if the cleaned sentence is a palindrome
    return cleaned_sentence == cleaned_sentence[::-1]

def main():
    user_input = input("Enter a sentence: ")

    if is_palindrome(user_input):
        print(f"\n'{user_input}' is a palindrome sentence.")

        cleaned_sentence = ''.join(char.lower() for char in user_input if char.isalnum())
        print(f"Cleaned sentence: '{cleaned_sentence}'")
    else:
        print(f"\n'{user_input}' is not a palindrome sentence.")

if __name__ == "__main__":
    main()
