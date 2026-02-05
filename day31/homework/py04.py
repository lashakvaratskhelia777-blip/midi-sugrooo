#შექმენით ფუნქცია სახელად manual_min რომელსაც გადაეცემა რიცხვების სია და უნდა დააბრუნოს ამ სიიდან ყველაზე პატარა
def manual_min(numbers):
    smallest = numbers[0]
    
    for num in numbers:
        if num < smallest:
            smallest = num
    
    return smallest
print(manual_min)