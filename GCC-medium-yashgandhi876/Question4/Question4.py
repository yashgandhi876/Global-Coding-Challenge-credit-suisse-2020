# Participants may update the following function parameters
def maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed, p, x, y):
    profitList = []
    total = 0
    for i in range(noOfTradesAvailable):
        total = (p[i]*x[i]-((1-p[i])*y[i]))
        if(total > 0):
            profitList.append(total)
    profitList = sorted(profitList, reverse=True)
    total = 0
    if(maximumTradesAllowed > len(profitList)):
        for i in range(len(profitList)):
            if(profitList[i] > 0):
                total += profitList[i]
    else:
        for i in range(maximumTradesAllowed):
            total += profitList[i]
    # print(profitList)
    return "{:.2f}".format(total)


def main():
    # This part may require participants to fill in as well.
    # noOfTradesAvailable, maximumTradesAllowed = list(map(int, input().split()))
    # p = list(map(float, input().split()))
    # x = list(map(float, input().split()))
    # y = list(map(float, input().split()))
    noOfTradesAvailable, maximumTradesAllowed = 2, 2
    p = [0.90, 0.50]
    x = [1.00, 0.50]
    y = [100.00, 0.40]

    # Participants may update the following function parameters
    answer = maximumExpectedMoney(
        noOfTradesAvailable, maximumTradesAllowed, p, x, y)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line


if __name__ == '__main__':
    main()
