# My first file tracked by Git
# Author: Pol Armengol

def greet(name):
    """Return a welcome message for the given name."""
    return f"Hello, {name}! Welcome to Git."

def farewell(name):
    """Return a goodbye message for the given name."""
    return f"Goodbye, {name}! See you next commit."

def count_words(text):
    """Count the number of words in the given text."""
    words = text.split()
    return len(words)

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
    print(f"Word count: {count_words('Hello World Welcome to Git')}")