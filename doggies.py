#Benjamin A. Keller 
#Dogs - OOP Prototype 
#1/6/2023

'''
This is the first part of a program which will be integrated into the project pets, which will feature 
all the dogs, cats, and even the two fish (including the Beta and the "Kitchen Fish", however, the minows
for fishing will not be included as they are bait for game fishing)
'''

class Dog: 

    def __init__(self, name, volume, speed, toy, energy, eat, amount): 
        self.name = name 
        self.volume = volume
        self.speed = speed 
        self.toy = toy
        self.energy = energy
        self.eat = eat
        self.amount = amount

    # action - barking
    def bark(self): 
        if self.volume > 5: 
            print(self.name + " says BARK!")
        else:
            print(self.name + " says bark")

    # action - dog's current activity. 

    def activity(self): 
        if self.speed > 3:
            print(self.name + " is running very fast!")
        elif self.speed > 1 and self.speed <=3: 
            print(self.name + " is running")
        else: 
            print(self.name + " is resting")

    def play(self):
         
        while self.energy > 10: 
            print(self.name + " is playing with " + self.toy)
            self.energy -= 1
        
        if self.energy == 0: 
            print(self.name + " is taking a nap")
    
    # activity - eating
    def is_eating(self): 
        
        if self.eat == "Treat":
            print(self.name + " gets a treat")
        
        elif self.eat == "Breakfast": 
            print(self.name + " is eating breakfast")
            if self.amount < 5: 
                print(self.name + " is not eating much") 
            else: 
                print(self.name + " is eating a lot!!!!")
        
        elif self.eat == "Lunch": 
            print(self.name + " is eating lunch")
            if self.amount < 5: 
                print(self.name + " not much") 
            else: 
                print(self.name + " is eating a lot!!!!")
        
        else: 
            print(self.name + " is eating dinner")
            if self.amount < 5: 
                print(self.name + "is not eating much") 
            else: 
                print(self.name + " is eating a lot!!!!")

#Dixon 

print()
print("\t\tDixon Says Hi!!!!\n")
Dixon = Dog("Dixon", 8, 8, "Ball", 18, "Lunch", 5)
Dixon.bark()
Dixon.activity()
Dixon.play()
Dixon.is_eating()

#Candy

print() 
print("\t\tSay hi to princess Candy!!! \n")
Candy = Dog("Candy", 2, 0, "Blanket", 0, "Treat", 7)
Candy.bark()
Candy.activity()
Candy.play()
Candy.is_eating()
print()

