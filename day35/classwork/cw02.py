#შექმენით ერთი ლისთი ხილზე, და გაფილტრეთ იმ ხილის სახელები რომლებიც არ იწყება "A" ზე
fruits = ["Apple", "Banana", "Avocado", "Orange"]

result = [f for f in fruits if f[0] != "A"]

print(result)