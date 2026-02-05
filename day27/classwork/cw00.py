def get_count(sentence):
    ხმოვანი  = "aeiou"   
    count = 0          

    for char in sentence:  
        if char in ხმოვანი:  
            count += 1      

    return count