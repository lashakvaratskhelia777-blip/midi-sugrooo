#შექმენით ლისთი, თქვენი დავალებაა რომ ყოველ იტერაციაზე თითოეულ ელემენტის პირველი ასო გაადიდოთ და შეინახო ახალ ლისთში list comprehension გამოყენებით
words = ["python", "java", "javascript", "html", "css"]

capitalized_words = [word.capitalize() for word in words]

print(capitalized_words)