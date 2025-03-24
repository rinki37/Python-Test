
########################################################################################
# Lesson 11 : Scope


# name = "Dave" # Global variable
# def greeting(name):
#     print(name)
# greeting("Sarah") # Here, Sarah will be printed as local is given priority

########################################################################################
# Accessing a global variable

# name = "Dave"
# def greeting():
#     color = "Black" # Local variable
#     print(color)
#     print(name)
# greeting() 
#print(color) # Here, we will get color is not defined as we are trying to access it out of its scope


########################################################################################
# Creating a local argument of same name as global

# name = "Dave"

# def another():
#     def greeting(name):
#         color = "Black"
#         print(color)
#         print(name)
#     greeting("John") 
    
# another()
# greeting("Dave") # This will give error as this funtion is not in global scope

########################################################################################
# Creating a local variable of same name as global

# name = "Dave"
# count = 1 

# def another():
#     color = "Black"
#     count = 2 # This will work, as we are creating a new variable named count.
#     print(count) # This will print 2
#     def greeting(name):
#         print(color)
#         print(name)
#     greeting("John") 
    
# another()

########################################################################################
# Trying to reassign value in a global variable

# name = "Dave"
# count = 1 

# def another():
#     color = "Black"
#     #count = 2 # This will work, as we are creating a new variable named count.
#     #count += 1 # This will give error "cannot access local variable 'count' where it is not associated with a value". Because this is looking for a local declaration of count which is not present.
#     print(count) # This will work as currently there is only one count variable (global) so there is no confusion.
#     def greeting(name):
#         print(color)
#         print(name)
#     greeting("John") 
    
# another()


########################################################################################
# Reassigning value in a global variable in a function

# name = "Dave"
# count = 1 

# def another():
#     color = "Black"
#     global count 
#     count += 2 # Now we are reassigning value in a global variable
#     print(count) 
    
# another()


########################################################################################
# Reassigning value in a global variable in a function

# name = "Dave"

# def another():
#     color = "Black"
#     def greeting(name):
#         nonlocal color
#         color = "Red" # Here, we are reassigning value in the local variable of another function inside greeting function, hence, it is a nonlocal to greeting function.
#         print(color)
#         print(name)
#     greeting("John") 
    
# another()

########################################################################################
# Lesson 12 : Closure (Closure is a function having access to the scope of its parent function after the parent function has returned. )

# def parent_function(person):
#     coins = 3
#     print("Hi parent")
#     def play_game():
#        nonlocal coins
#        coins -= 1
#        if(coins > 1):
#            print("\n" + person + " has " + str(coins) + " coins left.")
#        elif coins == 1:
#            print("\n" + person + " has " + str(coins) + " coin left.")
#        else:
#            print("\n" + person +  " is out of coins.")
           
#     return play_game # If we add paranthesis it will call the function, but if we don't add paranthesis it will return the function

# tommy = parent_function("Tommy")
# tommy()
# tommy()
# tommy()
# tommy()

# Here, we have a parent_function and then we have a child function, but we do not have a explicit call to that, instead after the child function there is return statement of parent_function function. 
# Now, When "tommy = parent_function("Tommy")" line is calling parent_function function it prints Hi parent. and after that it returns the entire function named play_game that we have stored in tommy. And in the next line when we call tommy(), it now contains a function and is working as a call to print_game function while preserving the value of coin which was in the parent_function function. Hence, when we call tommy again that preserved value is used and so on.

  
######

# def parent_function(person):
#     coins = 3
#     print("Hi parent" + " from " +person)
#     def play_game():
#        nonlocal coins
#        coins -= 1
#        if(coins > 1):
#            print("\n" + person + " has " + str(coins) + " coins left.")
#        elif coins == 1:
#            print("\n" + person + " has " + str(coins) + " coin left.")
#        else:
#            print("\n" + person +  " is out of coins.")
#     return play_game

# tommy = parent_function("Tommy")
# jenny = parent_function("Jenny")
# tommy()
# tommy()
# jenny()
# jenny()
             
# Here, we have a parent_function and then we have a child function, but we do not have a explicit call to that, instead after the child function there is return statement of parent_function function. 
# Now, When "tommy = parent_function("Tommy")" line is calling parent_function function it prints Hi parent. and after that it returns the entire function named play_game that we have stored in tommy. And in the next line when we call tommy(), it now contains a function and is working as a call to print_game function while preserving the value of coin which was in the parent_function function. Hence, when we call tommy again that preserved value is used and so on. Then the same happens with jenny.


####

# def parent_function(person, coins):
#     print("Hi parent" + " from " +person)
#     def play_game():
#        nonlocal coins
#        coins -= 1
#        if(coins > 1):
#            print("\n" + person + " has " + str(coins) + " coins left.")
#        elif coins == 1:
#            print("\n" + person + " has " + str(coins) + " coin left.")
#        else:
#            print("\n" + person +  " is out of coins.")
#     return play_game

# tommy = parent_function("Tommy", 4)
# jenny = parent_function("Jenny", 5)
# tommy()
# tommy()
# jenny()
# jenny()



########################################################################################

# f String - Different ways to format strings.

# Way 1
# person = "Dave"
# coins = 3
# print("\n" + person + " has " + str(coins) + " coins left.")

# Way 2
# message = "\n%s has %s coins left." % (person, coins) # This can get complicated with more values
# print(message)

# Way 3
# Format method approach
# message = "\n{} has {} coins left.".format(person, coins)  
# print(message)

# Way 4
# message = "\n{0} has {1} coins left.".format(person, coins) 
# print(message)

# Way 5
# message = "\n{1} has {0} coins left.".format(person, coins)  # 3 has Dave coins left. 
# print(message)

# Way 6
# message = "\n{person} has {coins} coins left.".format(person = person, coins = coins)  # This can get complicated with more values
# print(message)


# Way 7 - using dictionary
# player = {'person': 'Dave', 'coins' : 3}
# message = "\n{person} has {coins} coins left.".format(**player)  
# print(message)


# Way 8 - using dictionary
# player = {'person': 'Dave', 'coins' : 3}
# message = "\n{person} has {coins} coins left.".format(**player)  
# print(message)

##
# Way 9 - f-strings - A way more concise method.
# person = "Dave"
# coins = 3
# message = f"\n{person} has {coins} coins left."
# print(message)


# message = f"\n{person} has {2 * 5} coins left." # This works too.
# print(message)

# message = f"\n{person.lower()} has {2 * 5} coins left." # This works too.
# print(message)


# player = {'person': 'Dave', 'coins' : 3}
# message = f"\n{player['person']} has {player['coins']} coins left." 
# print(message)

#############
# You can pass the formatting options


# num = 10
# print(f"\n2.25 times {num} is {2.25 * num:.2f}") # Here, num:.2f in this we are specifying that we only want 2 decimal values and f denotes fixed place. So, we are formatting the output.

# for num in range(1,11): # Will run for 1 to 10
#     print(f"2.25 times {num} is {2.25 * num:.2f}")
    
# for num in range(1,11): 
#     print(f"{num} divided by 2.25 is {num / 4.52:.2%}")


########################################################################################

# Modules - A file containing a set of functions you want to include in your application.

# import math
# print(math.pi) # accessing pi from math module

# import random
# random.choice() # accessing choice function from random module. 

#from enum import Enum # importing enum from the Enum module. 

# from math import pi # Here, we are only importing pi from the math module. 
# print(pi)

# Createing an alias of module
# import random as rdm
# rdm.choice() # Now we are accessing using the alias. 

#######

# See what is in the module
# import random as rdm
# for item in dir(rdm): # This is will get everything present in the module
#     print(item) 

#######

# Here, i imported my own module named mymodule and accessed its functions and variables. 
# import mymodule
# #print(mymodule.language)
# #mymodule.randomfunfact()
# print(__name__) # This gives the name of the module we are running. 

# print(mymodule.__name__) # Gets the name of mymodule. 



# from rps_with_module import rock_paper_scissors
# rock_paper_scissors()



########################################################################################

# Command Line Arguments

# import argparse # Command line option and argument parsing library. 
# parser = argparse.ArgumentParser(description="Provides a personal greeting.")
# parser.add_argument(
#     "-n", "--name", metavar="name", 
#     required=True, help="The name of the person to greet."
# )
# args = parser.parse_args()

# message = f"Hello {args.name}!"
# print(message)

# To run the above code, run using this command - py test.py -n "Rinki"

#################
# def hello(name, lang):
#     greetings = {
#         "English" : "Hello",
#         "Spanish" : "Hola",
#         "German" : "Hallo",
#     }
#     msg = f"{greetings[lang]} {name}!"
#     print(msg)

# if __name__ == "__main__":
#     import argparse 
#     parser = argparse.ArgumentParser(description="Provides a personal greeting.")
#     parser.add_argument(
#         "-n", "--name", metavar="name", 
#         required=True, help="The name of the person to greet."
#     )
    
#     parser.add_argument(
#         "-l", "--lang", metavar="language", 
#         required=True, choices=["English", "Spanish", "German"],
#         help="The language of the greeting."
#     )
#     args = parser.parse_args()

#     hello(args.name, args.lang) # Run this using  - py test.py -n "Rinki" -l "English"



########################################################################################

# Lesson 17 - Lambda Function (A single expression that return a value.)

# squared = lambda num : num * num # here num is our parameter like we pass to a function. 
# print(squared(2))


#######
# addTwo = lambda num : num +2
# print(addTwo(12))

# sumTotal = lambda a,b: a + b # Traditional way to write the same  - def sum(a,b): return a + b 
# print(sumTotal(2,2))


#################
# Where to use lambda - when we want to build  a function. 

# def funcBuilder(x): 
#     return lambda num : num + x

# addTen = funcBuilder(10) # Here, we are passing the value of x. 
# addTwenty = funcBuilder(20)

# print(addTen(7)) # Here, we are passing the value of num for the lambda. 
# print(addTwenty(7))


########################################################################################

# Higher order function - a function that takes one or functions as arguments or a function that returns functions as its result. 


# numbers = [3, 7, 12, 23]
# squared_nums = map(lambda num : num * num, numbers) # Here, map() is a predefined function, in map() we are passing a lambda and a data collection. 
# print(list(squared_nums)) # This will give a new list having the squares of the numbers that we provided in a list. 
# Op -[9, 49, 144, 529]  


#######
# Checking odd - lambda num : num % 2 != 0 

# Here, we are checking which numbers from numbers list are odd and then filtering(using the predefiend function) and getting only odd ones in a list. We can do the same using loop but this way can give us concise code. 
# numbers = [3, 7, 12, 23]
# odd_nums = filter(lambda num : num % 2 != 0, numbers)
# print(list(odd_nums)) # Op -[3, 7, 23]


#######
# This is basically curr takes a number from the list, and initially in acc it's 0, so it will add the acc and curr, then the result will be in acc, and then that acc will be added to curra nd so on... 

# numbers = [1,2,3,4,5,1]
# from functools import reduce

# total = reduce(lambda acc, curr: acc + curr, numbers)
# print(total)

# OR ##############
# The above can be achieved using the below too. 

# numbers = [1,2,3,4,5,1]
# print(sum(numbers))


############
# Getting the character count using reduce. 
# from functools import reduce
# names = ["Dave", "Sara", "John Jacob Jingleheimerschmidt"]
# char_count = reduce(lambda acc, curr: acc + len(curr), names, 0) # 0 is starting value
# print(char_count)



########################################################################################

# OOPS in Python

########################################################################################

# Classes in Python - Blueprint of objects. 
# class Vehicle: # Class name will be in capital. 
#     def moves(self): # referring to itself
#         print("Moves along...")
    
# my_car = Vehicle() # Here, my_car is the object of Vehicle class. 
# my_car.moves()

########################################################################################
# Initializer function

# class Vehicle: 
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
        
#     def moves(self):
#         print("Moves along...")
    
# my_car = Vehicle("Tesla", "Model 3") # Here, we are passing  value to be assigned to the property. 
# print(my_car.make) # Accessing property of class. 
# print(my_car.model)
# my_car.moves() # Accesssing method of the class. 

########################################################################################

# Creating differnt object and accessing properties and method using them. 

# class Vehicle: 
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
        
#     def moves(self):
#         print("Moves along...")
    
#     def get_make_model(self):
#         print(f"I'm a {self.make} {self.model}.")
    
# my_car = Vehicle("Tesla", "Model 3") 
# my_car.get_make_model()
# my_car.moves()

# your_car = Vehicle("Tata", "Nano") 
# your_car.get_make_model() 
# your_car.moves()


########################################################################################

# Inheritence ()
# # A class cannot be empty. 

# class Vehicle: 
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
        
#     def moves(self):
#         print("Moves along...")
    
#     def get_make_model(self):
#         print(f"I'm a {self.make} {self.model}.")
    
# my_car = Vehicle("Tesla", "Model 3") 
# my_car.get_make_model()
# my_car.moves()

# your_car = Vehicle("Tata", "Nano") 
# your_car.get_make_model() 
# your_car.moves()


# class Airplane(Vehicle): # Inheriting Vehicle class in Airplane class
#     def moves(self):
#         print("Flies along")
        
# class Truck(Vehicle): # Inheriting Vehicle class in Truck class
#     def moves(self):
#         print("Rumbles along")

# class GolfCart(Vehicle): # Inheriting Vehicle class in GolfCart class
#     pass # It denotes we are not overridding anything here so it will inherit everything from the parent class.  

# cesssna = Airplane("Cessna", "Skyhawk")
# mack = Truck("Mack", "Pinnacle")
# golfwagon = GolfCart("Yamaha", "GC100")
# cesssna.get_make_model()
# cesssna.moves()
# mack.get_make_model()
# mack.moves()
# golfwagon.get_make_model()
# golfwagon.moves()



###############################################################################
### -
# class Vehicle: 
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
        
#     def moves(self):
#         print("Moves along...")
    
#     def get_make_model(self):
#         print(f"I'm a {self.make} {self.model}.")

# class Airplane(Vehicle):
#     def __init__(self, make, model, faa_id):
#         super().__init__(make, model) # Inherting make and moddel properties from super class i.e. parent class. 
#         self.faa_id = faa_id
        
#     def get_make_model(self):
#         print(f"I'm a {self.make} {self.model} with identification number {self.faa_id}.")
               
#     def moves(self):
#         print("Flies along...")
        
# class Truck(Vehicle): 
#     def moves(self):
#         print("Rumbles along...")

# class GolfCart(Vehicle): 
#     pass 

# cesssna = Airplane("Cessna", "Skyhawk", "12-ADDA1")
# mack = Truck("Mack", "Pinnacle")
# golfwagon = GolfCart("Yamaha", "GC100")
# cesssna.get_make_model()
# cesssna.moves()
# mack.get_make_model()
# mack.moves()
# golfwagon.get_make_model()
# golfwagon.moves()


