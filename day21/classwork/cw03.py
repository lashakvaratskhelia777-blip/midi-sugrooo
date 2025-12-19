#მომხმარებელს შემოატანინეთ თავისი სახელი, მეგობარი1ის სახელი და მეგობარი2ის სახელი,
#თ(ისე როგორც წინა საკლასოში), შემდეგ ეს გასწორებული სახელები ჩაამატეთ სიაში, საბოლოოდ კი შექმენით ახალი დასორტირებული სია და დაპრინტეთ

user = input("შეიყვანეთ თქვენი სახელი: ")
friend1 = input("შეიყვანეთ მეგობარი 1-ის სახელი: ")
friend2 = input("შეიყვანეთ მეგობარი 2-ის სახელი: ")

user = user.capitalize()
friend1 = friend1.capitalize()
friend2 = friend2.capitalize()



names = [user, friend1, friend2]

sorted_names = sorted(names)


print(names)
print(sorted_names)
