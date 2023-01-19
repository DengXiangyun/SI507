def change(amount, coins):
    ### amount is a non-negative integer indicating the amount of change to be made
    ### coins is a list of coin values
    if amount==0:
        return 0
    elif coins== []:
        return float('inf')
    else:
        It = coins[-1]
        if It > amount:
            return change(amount, coins[:-1])
        else:
            useIt = 1 + change(amount-It, coins)
            loseIt = change(amount, coins[:-1])

            return min(useIt, loseIt)

# print(change(48, [1, 5, 10, 25, 50]))
# print(change(48, [1, 7, 24, 42]))
# print(change(35, [1, 3, 16, 30, 50]))
# print(change(change(6, [4, 5, 9]))

def giveChange(amount, coins):
    if amount==0:
        return [0, []]
    elif coins== []:
        return [float('inf'), []]
    elif coins[-1] > amount:
        return giveChange(amount, coins[:-1])
    else:
        useIt = giveChange(amount - coins[-1], coins)
        useIt = [useIt[0]+1, [coins[-1]]+useIt[1]]

        loseIt = giveChange(amount, coins[:-1])

        if useIt[0] <= loseIt[0]:
            if useIt[0] == float('inf'):
                return [float('inf'), []]
            else:
                return useIt
        else:
            return loseIt



# print(giveChange(48, [1, 5, 10, 25, 50]))
# print(giveChange(48, [1, 7, 24, 42]))
# print(giveChange(35, [1, 3, 16, 30, 50]))
# print(giveChange(6, [4, 5, 9]))


