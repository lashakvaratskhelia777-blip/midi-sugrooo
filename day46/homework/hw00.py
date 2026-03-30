def change_string(text):
    result = ""
    
    for i in range(len(text)):
        if i % 2 == 1:
            result += text[i].upper()
        else:
            result += text[i]
    
    return result