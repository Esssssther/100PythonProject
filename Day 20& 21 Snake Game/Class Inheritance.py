#Inheritance
#class Fish(Animal): the fish class has all method, behaviour from Animal, and fish class can have other method and behaviour that animal don't have
    #def __init__(self):
        #super().__init__() #super refers to super class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")
class Fish(Animal):
    def __init__(self):
        super().__init__()#inherit all animal class
        # the call to super is recommended but not stirctly required

    def breathe(self): #use the same breathe function but want to make it more special for fish
        super().breathe() #fist inherit the animal breathe function
        print("doing this underwater") #then make it more special as you want
    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe() #this method is using the special fish breathe that inheritant the animal one
print(nemo.num_eyes)


#slicing
piano_keys = ["a","b","c","d","e","f","g"]

print(piano_keys[2:5])

#0,1,2,3,4,5,6,7
#print:['c', 'd', 'e']
print(piano_keys[2:5:2])
#['c', 'e']
print(piano_keys[::2])
#['a', 'c', 'e', 'g']
print(piano_keys[::-1])
#['g', 'f', 'e', 'd', 'c', 'b', 'a']
