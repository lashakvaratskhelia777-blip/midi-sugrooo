def manual_find(lst, element):
    for index in range(len(lst)):
        if lst[index] == element:
            return index
    return -1
