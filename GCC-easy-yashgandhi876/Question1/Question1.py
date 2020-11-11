import sys
# You may change this function parameters


def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    maxValue = float('-inf')
    minValue = float('inf')
    total = -1
    for i in range(numOfPredictedDay):
        minValue = predictedSharePrices[i]
        for j in range(i+1, numOfPredictedDay):
            if(minValue < predictedSharePrices[j]):
                maxValue = predictedSharePrices[j]
                if((maxValue - minValue) > total):
                    total = maxValue - minValue
    return total


def main():
    line = input().split()
    numOfPredictedDay = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


if __name__ == '__main__':
    main()
