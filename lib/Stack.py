class Stack:
    def __init__(self, elements=None):
        """Initialize a new stack."""
        if elements is None:
            elements = []
        self.elements = elements

    def push(self, element):
        """Add an element to the top of the stack."""
        self.elements.append(element)

    def pop(self):
        """Remove and return the top item from the stack. Raises an exception if the stack is empty."""
        if self.empty():
            raise Exception("Stack is empty")
        return self.elements.pop()

    def size(self):
        """Return the number of items in the stack."""
        return len(self.elements)

    def empty(self):
        """Check if the stack is empty."""
        return len(self.elements) == 0

    def search(self, element):
     try:
        return self.elements.index(element)
     except ValueError:
        return -1

