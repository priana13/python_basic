class Herro:

    def __init__(self , inputName , inputHealth, inputPower , inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

herro1 = Herro("Priana" , 100 , 4 , 90)
herro2 = Herro("Herian" , 700 , 50 , 30)

print(herro1.__dict__)
print(herro2.__dict__)
print(herro1.name)