def organizingContainers(container):
    # Participants code will be here
    listt = [0 for _ in range(len(container))]
    ls = 0
    rs = 0
    for i in range(len(container)):
        for j in range(len(container[i])):
            if(i != j):
                if(container[i][j] != 0):
                    container[i][i] += container[i][j]
                    container[i][j] = 0
                    listt[i] = container[i][i]
    if(sorted(listt, reverse=True) == listt):
        return "Possible"
    return "Impossible"


if __name__ == "__main__":
    q = int(input().strip())
    answer = ""
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
            container_t = [int(container_temp)
                           for container_temp in input().strip().split(' ')]
            container.append(container_t)
        result = organizingContainers(container)
        if(answer == ""):
            answer = str(result)
        else:
            answer = answer + "," + str(result)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line
