def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)