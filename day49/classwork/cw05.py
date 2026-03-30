def car_builder(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

car_builder(brand="Toyota", model="Corolla", year=2021, color="Red")
# trim აკეთებს მოდელის დამატებას, მაგალითად: trim="LE"