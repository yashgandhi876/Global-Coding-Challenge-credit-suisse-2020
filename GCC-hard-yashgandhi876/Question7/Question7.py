import collections
# Participants may update the following function parameters


def findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList):
    # Participants code will be here
    maxnumber = max(max(questionAndAnswerListOfList))
    arr = [[] for _ in range(maxnumber)]
    sus = []

    for i in range(0, numOfQuestions):
        string = []
        for j in range(1, len(questionAndAnswerListOfList[i])):
            if(arr[questionAndAnswerListOfList[i][0]-1] != 0):
                string = arr[questionAndAnswerListOfList[i][0]-1]
            if(questionAndAnswerListOfList[i][j] != questionAndAnswerListOfList[i][0]):
                string.append(questionAndAnswerListOfList[i][j])
            arr[questionAndAnswerListOfList[i][0]-1] = string

    for i in range(maxnumber):
        for j in range(len(arr[i])):
            temp = arr[i][j]
            if(not(temp in sus)):
                for l in range(numOfQuestions):
                    if(questionAndAnswerListOfList[l][0] == temp):
                        if(i+1 in arr[temp-1]):
                            sus.append(i+1)
                            sus.append(questionAndAnswerListOfList[l][0])
                            break

    for e in range(numOfQuestions):
        for i in range(numOfQuestions):
            count = 0
            if(i+1 not in sus and len(questionAndAnswerListOfList[i]) > 2):
                for j in range(1, len(questionAndAnswerListOfList[i])):
                    if(questionAndAnswerListOfList[i][j] in sus):
                        count += 1
                    if(count >= 2):
                        sus.append(questionAndAnswerListOfList[i][0])
                        break

    strings = ''
    sus = sorted(list(set(sus)))
    for i in range(len(sus)):
        strings += str(sus[i]) + ','
    return strings[:-1]


def main():
    # firstLine = input().split("")
    # secondLine = input()
    firstLine = ['5']
    secondLine = '1 2 4,2 3 5,3 5 6,4 5 2,5 6,6 5'

    numOfQuestions = int(firstLine[0])
    questionAndAnswers = secondLine.split(",")
    questionAndAnswerListOfList = parseQuestionAndAnswer(questionAndAnswers)

    # Participants may update the following function parameters
    answer = findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parseQuestionAndAnswer(questionAndAnswers):
    questionAndAnswerListOfList = []
    for index in range(0, len(questionAndAnswers)):
        questionAndAnswerList = questionAndAnswers[index].split(" ")
        questionAndAnswerListOfList.append(
            [int(x) for x in questionAndAnswerList])
    return questionAndAnswerListOfList


if __name__ == '__main__':
    main()
