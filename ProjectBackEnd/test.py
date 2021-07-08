# -Write a Python function to multiply all the numbers in a list.

def numberlist(**args):
    numbers=[8, 2, 3, -1, 7]
    cem=1
    for i in args:
        cem*=args
        print(cem)
    return cem

numberlist(8, 2, 3, -1, 7)