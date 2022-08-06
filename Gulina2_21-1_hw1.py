class Cow:
    def __init__(self, name):
        self.name = name
        

    def voice(self):
        print(f'{self.name}:Muu')


class Dog:
    def __init__(self, name):
        self.name = name


    def voice(self):
        print(f'{self.name}:Gaf Gaf')


class Bear:
    def __init__(self, name):
        self.name = name
    def voice(self):
        print(f'{self.name}:Arrrr')

class Cat:
    def __init__(self, name):
        self.name = name
    def voice(self):
        print(f'{self.name}:Meouw')


cow = Cow('Cow')
cow.voice()

dog = Dog('Dog')
dog.voice()

bear =Bear('Bear')
bear.voice()

cat = Cat('Cat')
cat.voice()
