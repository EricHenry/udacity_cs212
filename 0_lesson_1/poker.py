import random
import itertools

allranks = '23456789TJQKA'
redcards = [r+s for r in allranks for s in 'DH']
blackcards = [r+s for r in allranks for s in 'CS']

# Return the best hand: poker([hand, ...]) => hand
def poker(hands):
    return max(hands, key=hand_rank)

# From a 7-card hand, return the best 5 card hand.
def best_hand(hand):
    return max(itertools.combinations(hand, 5), key=hand_rank)

# Try all values for jokers in all 5-card selections.
def best_wild_hand(hand):
    hands = set(best_hand(h) for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)

# Return a list of possible replacements for a card.
# There will be more than 1 only for wild cards
def replacements(card):
    if card == '?B': return blackcards
    elif card == '?R': return redcards
    else: return [card]

# Return a list of all items equal to the max of the iterable
def allmax(iterable, key=None):
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

# Shuffle the deck and deal out numhands n-card hands
def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deal[n*i:n*(i+1)] for i in range(numhands)]

# Return a list of [(count, x)...], highest count first, then highest x
def group(items):
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)

def unzip(pairs): return zip(*pairs)

# Return a value indicating the rank of a hand
def hand_rank(hand):
    # counts is the count of each rank; ranks lists corresponding ranks
    # e.g "7 T 7 9 7" => counts = (3, 1, 1); ranks(7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r,s in cards])
    counts, ranks = unzip(groups)
    if (ranks == [14, 5, 4, 3, 2]):
        ranks = [5, 4, 3, 2, 1]
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return max(count_rankings[counts], 4*straight + 5*flush), ranks

count_rankings = {(5,): 10, (4, 1): 7, (3, 2): 6, (3, 1, 1): 3, (2, 2, 1): 2, (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}

# Test cases for the functions in poker program
def test():
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    fl = "3H TH JH QH 5H".split()
    st = "8H 9C TS JH QD".split()
    tk = "KS KH KD 4C 9D".split()
    tp = "2D 2H JS JC 6C".split()
    op = "TD TS 3D 7C 2H".split()
    hc = "QD TS 3D 7C 2H".split()
    ls = "AC 3S 4H 2H 5C".split()

    #poker assertions
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + [fh] * 99) == sf

    # hand_rank assertions
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert hand_rank(fl) == (5, [12, 11, 10, 5, 3])
    assert hand_rank(st) == (4, 12)
    assert hand_rank(tk) == (3, 13, [13, 13, 13, 9, 4])
    assert hand_rank(tp) == (2, (11, 2), [11, 11, 6, 2, 2])
    assert hand_rank(op) == (1, 10, [10, 10, 7, 3, 2])
    assert hand_rank(hc) == (0, [12, 10, 7, 3, 2])

    # test_best_wild_hand
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())) 
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])

    return "tests pass"

print(test())
    
