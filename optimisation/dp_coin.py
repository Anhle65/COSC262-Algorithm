import re

from sympy import rem


def coins_reqd(value, coinage):
    """Minimum number of coins to represent value.
       Assumes there is a 1-unit coin."""
    num_coins = [0] * (value + 1)
    tracking_coin = [0] * (value + 1)
    result = []
    for amt in range(1, value + 1):
        minimum = None
        for c in coinage:
            if c <= amt:
                coin_count = num_coins[amt - c]  # Num coins required to solve for amt - c
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
                    tracking_coin[amt] = c
        num_coins[amt] = 1 + minimum
    dict_coin = {}
    
    remain = len(tracking_coin) - 1
    while remain > 0:
        if tracking_coin[remain] not in dict_coin.keys():
            dict_coin[tracking_coin[remain]] = 1
        else:
            dict_coin[tracking_coin[remain]] += 1
        remain -= tracking_coin[remain]
    for coin in dict_coin.keys():
        result.append((coin, dict_coin[coin]))

    return sorted(result, key= lambda x:x[0], reverse=True)
print(coins_reqd(32, [1, 10, 25]))