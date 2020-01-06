class Parent:

    def last_name(self):
        print('Anavatti')

class Child(Parent):
    def first_name(self):
        print("Vishwas")

a=Child()
a.first_name()
a.last_name()