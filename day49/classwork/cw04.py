def food_ranking(category="food", *args):
    counter = 1
    for item in args:
        print(f"{category}: {counter} {item}")
        counter += 1


food_ranking("food", "khinkali", "khachapuri", "lobio")
