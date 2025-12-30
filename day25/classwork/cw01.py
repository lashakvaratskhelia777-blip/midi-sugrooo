#შექმენით ფუნქცია, რომელსაც გადაეცემა 2 რიცხვი, პირველ რიცხვს ჰქონდეს default value 3, ხოლო მეორეს 5. ფუნქციამ უნდა გამოიტანოს ამ ორი რიცხვიდან უდიდესი რიცხვი
def max_number(a=3, b=5):
    return max(a, b)

print(max_number())        
print(max_number(10))      
print(max_number(2, 8))