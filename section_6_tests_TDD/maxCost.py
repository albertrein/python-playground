def maxCost(cost, labels, dailyCount):
    max_cost = 0
    custo = 0
    contador_dias = dailyCount
    for i in range(1, cost.__len__()-1):
        if contador_dias > 0:
            custo += cost[i]
            if labels[i-1] == 'legal':
                contador_dias -= 1
        if contador_dias == 0:
            if custo > max_cost:
                max_cost = custo
            custo = 0
            contador_dias = dailyCount
    return max_cost

#maxCost([5,2,5,3,11,1,5], ['legal','ilegal','legal','ilegal','legal'],2)
print(maxCost([5, 0, 3, 2, 3, 4, 5], ['legal','legal','illegal','legal','legal'],1))
