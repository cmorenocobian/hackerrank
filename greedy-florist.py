def getMinimumCost(k, c):
    
    cost = 0
    count = 0
    c.sort(reverse = True)
    for i in c:
        price = count // k + 1       
        cost += i * price
        count += 1
    
    return cost
