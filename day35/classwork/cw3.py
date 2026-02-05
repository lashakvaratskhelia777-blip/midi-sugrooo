#შექმენით ერთი ინტეჯერების list სადაც გექნებათ მოცემული რიცხვები 1 დან 20 მდე, თქვენი დავალებაა რომ გაფილტროთ კენტი რიცხვები list comprehension გამოყენებით
numbers = [i for i in range(1, 21)]

odd_numbers = [n for n in numbers if n % 2 != 0]

print(odd_numbers)