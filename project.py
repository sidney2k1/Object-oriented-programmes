class dog:
    animal="dog"
    def __init__(self,breed,color):
        self.breed=breed
        self.color=color
Rodger=dog("Pug","black")
Buzo=dog("Labrador","brown")
print("Rodger is a {}".format(Rodger.animal))
print("Buzo is a {}".format(Buzo.animal))
print("{} is {} in color".format(Rodger.breed,Rodger.color))
print("{} is {} in color".format(Buzo.breed,Buzo.color))
print("Accessing class variable using class name:")
print(dog.animal)