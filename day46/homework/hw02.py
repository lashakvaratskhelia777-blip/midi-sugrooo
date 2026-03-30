def bigger_than_neighbors(numbers):
    result = []
    
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            result.append(numbers[i])
    
    return result