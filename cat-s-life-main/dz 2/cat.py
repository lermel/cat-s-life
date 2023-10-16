class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class CatBreed(Cat):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


my_cat = CatBreed("Tosya", 4, "Siamese")

print(f"{my_cat.name} is {my_cat.age} years old and she has {my_cat.breed} breed.")