# You may change this function parameters
def findMaxProfit(numOfPredictedTimes, predictedSharePrices):
    # Participants code will be here
    total = 0
    i, j = 0, 0
    minValue = float('inf')
    while(i < numOfPredictedTimes-1):
        maxValue = float('-inf')
        if(predictedSharePrices[i+1] > predictedSharePrices[i]):
            minValue = predictedSharePrices[i]
            j = i+1
            while(j < numOfPredictedTimes):
                if(maxValue < predictedSharePrices[j]):
                    maxValue = predictedSharePrices[j]
                else:
                    break
                j += 1
                i = j-1
            total += (maxValue - minValue)
        i += 1
    return total

def main():
    line = input().split()
    numOfPredictedTimes = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedTimes, predictedSharePrices)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()