def replace_threes(n):
    result = []
    
    for i in range(1, n+1):
        if i % 3 == 0:
            result.append("Three")
        else:
            result.append(i)
    
    return result