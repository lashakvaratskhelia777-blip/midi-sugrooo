#  შემქენით პროგრამა რომელიც მომხმარებელს შემოატანინებს ორ რიცხვს და ყოფს ერთამენთზე. გამოიყენეთ try / except რომ პროგრამა არ გაჩერდეს თუ მომხმარებელმა შემოიტანა 0

try:
    num1 = float(input("enter your number"))
    num2 = float(input("enter your number"))
    result = num1 / num2
except ZeroDivisionError: 
    print("ნულზე არიყოფა")
except ValueError:
    print("შეიყვანე მხოლოდ რიცხვი")