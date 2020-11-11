def find_min_days(prices, profit):
    # Participants code will be here
    ptl = len(profit)
    psl = len(prices)
    buyDay = -1
    sellDay = -1
    stri = ""
    for i in range(ptl):
        setflag = False
        for j in range(psl):
            for k in range(j+1, psl):
                if((prices[k] - prices[j]) == profit[i]):
                    if(buyDay != -1):
                        if(sellDay >= k):
                            sellDay = k
                            buyDay = j
                    else:
                        buyDay = j
                        sellDay = k
                    setflag = True
        if(buyDay == -1 and sellDay == -1):
                stri += "-1"
        else:
            if(setflag):
                stri += f'{buyDay+1} {sellDay+1}'
            else:
                stri += "-1"
        if(i != ptl-1):
            stri += ","
    if(stri == "-1,"):
        return stri[:-1]
    return stri.strip()

n, d = map(int, input().split())
prices = list(map(int, input().split()))
profit = list()
for i in range(d):
    profit.append(int(input().strip()))
answer = find_min_days(prices,profit)
# Do not remove below line
print(answer)
# Do not print anything after this line