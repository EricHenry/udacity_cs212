# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1

"Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
def all_ints():
    i = 0
    while True:
        yield i
        if i > 0:
            i = i * -1
        else:
            i = i * -1 + 1
