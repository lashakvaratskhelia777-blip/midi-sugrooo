user_input = input("შეიყვანე რიცხვები გამოყოფილი space-ით: ")

numbers = user_input.split()

try:
    int_numbers = []
    
    for n in numbers:
        int_numbers.append(int(n))
    
    print("ყველა რიცხვი სწორია:", int_numbers)

except:
    print("სიაში არასწორი მონაცემია")