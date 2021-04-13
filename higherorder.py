# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("Hello, professor. I'm JiaYao Teng")
    print(greeting)


greet(shout)
greet(whisper)
