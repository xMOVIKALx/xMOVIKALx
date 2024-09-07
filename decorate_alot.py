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
import sys


def red_print(value):
    print(value, file=sys.stderr)


class Wrapper:

    def custom_symbol(self, symbol, max_digits=100, space=False):
        if space == True:
            symbol = f"{symbol} "

        def wrapper(func):
            print(f'{symbol}' * max_digits)
            func()
            print(f'{symbol}' * max_digits)

        return wrapper

    def line(self, max_digits=100, space=False):
        if space == True:
            symbol = f"- "
        else:
            symbol = '-'

        def wrapper(func):
            print(f'{symbol}' * max_digits)
            func()
            print(f'{symbol}' * max_digits)

        return wrapper

    def star(self, max_digits=100, space=False):
        if space == True:
            symbol = f"* "
        else:
            symbol = '*'

        def wrapper(func):
            print(f'{symbol}' * max_digits)
            func()
            print(f'{symbol}' * max_digits)

        return wrapper

    def arrow(self, max_digits=100, space=False):
        if space == True:
            symbol = f"^ "
        else:
            symbol = '^'

        def wrapper(func):
            print(f'{symbol}' * max_digits)
            func()
            print(f'{symbol}' * max_digits)

        return wrapper

    def square(self, max_digits=100, space=False):
        if space == True:
            symbol = f"# "
        else:
            symbol = '#'

        def wrapper(func):
            print(f'{symbol}' * max_digits)
            func()
            print(f'{symbol}' * max_digits)

        return wrapper

    def tilde(self, max_digits=100, space=False):
        if space == True:
            symbol = f"~ "
        else:
            symbol = '~'

        def wrapper(func):
            print(f'{symbol}' * max_digits)
            func()
            print(f'{symbol}' * max_digits)

        return wrapper

    def dot(self, max_digits=100, space=False):
        if space == True:
            symbol = f". "
        else:
            symbol = '.'

        def wrapper(func):
            print(f'{symbol}' * max_digits)
            func()
            print(f'{symbol}' * max_digits)

        return wrapper
