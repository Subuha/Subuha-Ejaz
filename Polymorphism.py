
# Online Python - IDE, Editor, Compiler, Interpreter

class Animal():
    def sound(self):
        return "some sound"
class Dog(Animal):
    def sound (self):
        return "Bark"
class Cat(Animal):
    def sound (self):
        return "Meow"

def make_sound(animal):
    print(animal.sound()) 

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
