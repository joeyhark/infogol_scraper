import re


def bet_outcome(home, away, bet, result):
    GHome = int(result[0])
    GAway = int(result[4])
    if bet == 'Both Teams To Score':
        if GHome and GAway:
            return True
        else:
            return False
    if bet == 'Both Teams To Score - No':
        if not GHome or not GAway:
            return True
        else:
            return False
    if 'Over' in bet:
        over = float(re.findall(r'\d\.?\d?', bet)[0])
        if (GHome + GAway) > over:
            return True
        elif (GHome + GAway) == over:
            return 'Push'
        else:
            return False
    if 'Under' in bet:
        under = float(re.findall(r'\d\.?\d?', bet)[0])
        if (GHome + GAway) < under:
            return True
        elif (GHome + GAway) == under:
            return 'Push'
        else:
            return False
    if 'or Draw' in bet:
        if home in bet:
            if GHome >= GAway:
                return True
            else:
                return False
        if away in bet:
            if GAway >= GHome:
                return True
            else:
                return False
    if 'To Win' in bet:
        if home in bet:
            if GHome > GAway:
                return True
            else:
                return False
        if away in bet:
            if GAway > GHome:
                return True
            else:
                return False
    if bet == 'Draw':
        if GHome == GAway:
            return True
        else:
            return False


def profit(outcome, odds, value):
    decimal = frac_to_dec(odds)
    if outcome == 'Push':
        return 0
    if outcome:
        return round(decimal * value, 2)
    else:
        return -value


def frac_to_dec(frac):
    fraction = re.findall(r'\d+', frac)
    return int(fraction[0]) / int(fraction[1])
