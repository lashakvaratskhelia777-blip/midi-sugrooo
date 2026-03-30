my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("შეიყვანე ინდექსი: "))
    my_list.pop(index)
    print("განახლებული სია:", my_list)

except:
    print("ინდექსი არ არსებობს")