class Hero:

    def __init__(self,name,health,attactPower,armorNumber):
        self.name = name
        self.health = health
        self.attactPower = attactPower
        self.armorNumber = armorNumber

    def serang(self,lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self , self.attactPower)

    def diserang(self , lawan , attactPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attact_diterima = attactPower_lawan/self.armorNumber

        print('serangan terasa : ' + str(attact_diterima))
        self.health -= attact_diterima

        print('data ' + self.name + ' terisa ' + str(self.health))


sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,20,10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)



