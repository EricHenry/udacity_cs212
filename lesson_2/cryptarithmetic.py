# -------------
#
# solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#

import re, itertools

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f

def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

def valid(f):
    "Formula f id valid if it has no numbers with leadin zeros and evals true."
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if not word.isalpha() or not word.isupper():
        return word

    rev_word = word[::-1]
    translate = [str(10**idx) + '*' + c for idx, c in enumerate(rev_word)]
    compiled = '(' + '+'.join(translate) + ')'

    return compiled