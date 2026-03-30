def multiply_by_index(numbers):
    result = []
    
    for i in range(len(numbers)):
        result.append(numbers[i] * i)
    
    return result