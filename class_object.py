class Enemy:
    life=3
    def attack(self):
        print("Oops!")
        self.life-=1

    def checkLife(self):
        if self.life<=0:
            print("Dead")
        else:
            print(str(self.life)+" life left")

e1=Enemy()
e2=Enemy()

e1.attack()
#e1.attack()
e1.attack()
e1.checkLife()
e2.checkLife()


class Ene:
    def __init__(self,x):
        self.energy=x

    def get_energy(self):
        print(self.energy)

a=Ene(5)
b=Ene(10)

a.get_energy()
b.get_energy()