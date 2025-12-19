 #შექმენით ფუნქცია სახელად difference, რომელსაც გადაეცემა სამი რიცხვი, შემდეგ გამოიტანეთ ამ სამი რიცხვიდან ყველაზე დიდი და ყველაზე პატარა რიცხვი


def difference(a, b, c):
    largest = max(a, b, c)
    smallest = min(a, b, c)
    return largest, smallest
print(difference(5,2,9))

numbers = difference(5, 2, 9)