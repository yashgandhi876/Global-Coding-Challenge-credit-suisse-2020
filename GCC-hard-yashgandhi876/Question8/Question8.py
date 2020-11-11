# Participants may update the following function parameters
def countNumberOfWays(numOfUnits, numOfCoinTypes, coins):
    # Participants code will be here
    matrix = []
    for i in range(numOfCoinTypes+1):
        temp = []
        for j in range(numOfUnits+1):
            temp.append(0)
        matrix.append(temp)
    for i in range(numOfCoinTypes+1):
        matrix[i][0] = 1
    for i in range(1, numOfCoinTypes+1):
        for j in range(1, numOfUnits+1):
            if(coins[i-1] <= j):
                matrix[i][j] = matrix[i][j - coins[i-1]] + matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[-1][-1]


def main():
    firstLine = input().split(" ")
    secondLine = input().split(" ")

    numOfUnits = int(firstLine[0])
    numOfCoinTypes = int(firstLine[1])
    coins = list(map(int, secondLine))

    # Participants may update the following function parameters
    answer = countNumberOfWays(numOfUnits, numOfCoinTypes, coins)

    # Please do not remove the below line.
    print("ans: ", answer)
    # Do not print anything after this line


if __name__ == '__main__':
    main()
