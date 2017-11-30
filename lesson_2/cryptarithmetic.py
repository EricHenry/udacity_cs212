# -------------
#
# solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#

import string, re

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    validmappings = [f for f in fill_in(formula) if valid(f)]

    if len(validmappings) == 0:
        return None
    else:
        return validmappings[0]

# assume: def fill_in(formula):
#        "Generate all possible fillings-in of letters in formula with digits."


def valid(f):
    "Formula f id valid if it has no numbers with leadin zeros and evals true."
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False