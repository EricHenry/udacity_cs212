# Return the best hand: poker([hand, ...]) => hand
def poker(hands):
    return max(hands, key=hand_rank)

# Return a value indicating the rank of a hand
def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)

# Return a list of the ranks, sorted with higher first
def card_ranks(cards):
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return ranks

# Return True if the ordered ranks form a 5-card straight.
def straight(ranks):
    # true if the difference between the highest and lowest card is 4
    # and if we have 5 unique ranks
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

# Return True if all the cards have the same suit.
def flush(hand):
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

# Return the first rank that this hand has exactly n of.
# Return None if there is no n-of-a-kind in the hand.
def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

# If there are two pair, return the two ranks as a
# tuple: (highest, lowest); otherwise return None
def two_pair(ranks):
    # if there is a pair it will get the first pair, and since it is ordered that pair will be the highest pair
    pair = kind(2, ranks)
    # if there is another piar get the lowest of the pair
    lowpair = kind(2, list(reversed(ranks)))

    # make sure we have a pair and the lowpair does not equal the highpair
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None


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

    # card_ranks assertions
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    #straight assertions
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    #flush assertions
    assert flush(sf) == True
    assert flush(fk) == False
    
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    opranks = card_ranks(op)

    #kind assertions
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    #two-pair
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (11, 2)
    assert two_pair(opranks) == None

    return "tests pass"

print(test())
    
