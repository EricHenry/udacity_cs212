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

def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False."""

    # modify the code in this function.

    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    firstletters = set(re.findall('([A-Z]+)', formula))
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    if firstletters:
        tests = ' and '.join(l+'!=0' for l in firstletters)
        body = '%s and (%s)' % (tests, body)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print(f)
    return eval(f), letters

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [str(10**i) + '*' + c
                 for i, c in enumerate(word[::-1])] # str[::-1] reverses a string, saying take the whole string start at the last element
        return '(' + '+'.join(terms) + ')'
    else:
        return word

