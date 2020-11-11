# You may change this function parameters
def calculateMinimumSession(numOfBankers, numOfParticipants, bankersPreferences, participantsPreferences):
    bankerLengths = [0 for i in range(numOfBankers)]
    participantLengths = [0 for i in range(numOfParticipants)]

    for i in range(numOfBankers):
        bankerLengths[i] += len(bankersPreferences[i])
    for i in range(numOfParticipants):
        for j in range(len(participantsPreferences[i])):
            if(not(i+1 in bankersPreferences[participantsPreferences[i][j] - 1])):
                bankerLengths[participantsPreferences[i][j] - 1] += 1

    for i in range(numOfParticipants):
        participantLengths[i] += len(participantsPreferences[i])

    for i in range(numOfBankers):
        for j in range(len(bankersPreferences[i])):
            if(not(i+1 in participantsPreferences[bankersPreferences[i][j] - 1])):
                participantLengths[bankersPreferences[i][j] - 1] += 1

    maxBanker = max(bankerLengths)
    maxParticipant = max(participantLengths)
    if(maxBanker > maxParticipant):
        return maxBanker
    return maxParticipant


def main():
    # firstLine = input().split(" ")
    # secondLine = input().split(" ")
    firstLine = ['3', '1,1,1']
    secondLine = ['1', '1&2&3']
    # Sample input:
    # 3 1,1,1&2
    # 3 3&2,1,1
    numOfBankers = int(firstLine[0])
    numOfParticipants = int(secondLine[0])
    bankersPreferences = firstLine[1].split(",")
    participantsPreferences = secondLine[1].split(",")

    bankersPreferencesListOfList = parsePreferences(bankersPreferences)
    participantsPreferencesListOfList = parsePreferences(
        participantsPreferences)

    answer = calculateMinimumSession(
        numOfBankers,
        numOfParticipants,
        bankersPreferencesListOfList,
        participantsPreferencesListOfList
    )

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parsePreferences(preferences):
    preferenceListOfList = []
    for index in range(0, len(preferences)):
        preferenceArr = preferences[index].split("&")
        preferenceListOfList.append([int(p) for p in preferenceArr])
    return preferenceListOfList


if __name__ == '__main__':
    main()
