def words_length_dict(text):
    result = {}
    
    words = text.split()
    
    for word in words:
        result[word] = len(word)
    
    return result