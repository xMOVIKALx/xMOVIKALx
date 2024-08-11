# This is a simple-function-wrapper for prints
# You can use it just for print-in functions
# like :
# ------
# decorator = Wrapper()
#
# @decorator.custom_symbol('+', max_digits=10)
# def p():
#   print("Hello world!")
# -----------------------------------------------
# output :
# ++++++++++
# Hello world!
# ++++++++++

class Wrapper:

    def custom_symbol(self, symbol, max_digits=100):
        def wrapper(func):
            print(f'{symbol}' * max_digits)
            func()
            print(f'{symbol}' * max_digits)

        return wrapper

    def line(self, max_digits=100):
        def wrapper(func):
            print('-' * max_digits)
            func()
            print('-' * max_digits)

        return wrapper

    def star(self, max_digits=100):
        def wrapper(func):
            print('*' * max_digits)
            func()
            print('*' * max_digits)

        return wrapper

    def arrow(self, max_digits=100):
        def wrapper(func):
            print('^' * max_digits)
            func()
            print('^' * max_digits)

        return wrapper

    def square(self, max_digits=100):
        def wrapper(func):
            print('#' * max_digits)
            func()
            print('#' * max_digits)

        return wrapper

    def tilde(self, max_digits=100):
        def wrapper(func):
            print('~' * max_digits)
            func()
            print('~' * max_digits)

        return wrapper

    def dot(self, max_digits=100):
        def wrapper(func):
            print('.' * max_digits)
            func()
            print('.' * max_digits)

        return wrapper
