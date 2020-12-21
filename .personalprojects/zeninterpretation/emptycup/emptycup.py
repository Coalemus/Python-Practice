""" To get something, one must first have an empty bowl """

##TODO: Define a superclass for both BowlObject and WaterObject.
## mandatory, Classes need to be defined more clearly


##TODO: make the classes interact with each other through functions
# TODO:  called by the user.
## I think I utilized the class function definition wrong,
# the classes need to be coded closer to textbook definition.


##TODO: maybe switch method of using iterators since the results
# TODO:  print 1 char each line in the results,
## NEED TO FIND SOLUTION


##TODO: DEFINE A CLASS AND USE IT'S PARAmETERS AS DEFINITION
# TODO:  OF THE RESULTS OF THE INPUT RESULTS FUNCTION.
## mandatory for properly utilizing the defined classes.


##TODO: Utilize function parameter *args.
# TO do with other todos. 


##TODO: Apply Dunder method to the classes.
## Still reading up on it.


##TODO: make a bowl that has a empty and full state.
## Done.


##TODO: make functions that interact with the classes defined above.
# TODO:  make functions that makes the user fill or empty the bowl.
# TODO:  make this list variable be interactable 
# TODO:  and dynamic towards the code. (?)
## Need to read upon how to apply a class method towards a function
# definition.


##TODO: Use string format() method for easier applicaton of concept.
# To choose between file modification.


##TODO: Ponder if using a for loop for appending on a new 'result'
# TODO:  list is better than other methods.
# Still reading up on it.


##TODO: Apply nonlocal modifier.
## Just a reminder, not mandatory.


##TODO: Use Getter and setter property method decorators, also just
# TODO:  property in general for the ClassObjects.
# To do in tandem with other todos.


##TODO: Swap the if statements that are incorrect into while loops.
## Cannot find anymore incorrect statements.


##TODO: make the state of the variables/classes "water" and "bowl"
# TODO:  as str in order for them to be easily iterable.
## Waiting for the global variables to be defined more clearly.
 

##TODO: Use regex for defining the functions of adding or removing
# TODO:  water.
# To be done in with other todos.


##TODO: maybe tinker with the global variables inside of the functions
# TODO:  and set some into a local variable.
## Reminder, not mandatory.


##TODO: USE ASYNC FUNCTIONS!!! maybe if I could figure out how
# TODO:  to continuously run the script after the userinput.
## mandatory, for the water and bowl to maintain its state 
# after userinput is given.


##TODO: Use a text file for The dialogue.
## Reminder, slightly mandatory if the alternative of using async
# functions doesn't work.


##TODO: Contemplate whether to use an empty list as the result and
# TODO:  to modify the functions towards appending what string appears.
# TODO:  And maybe even a text file for dialogue.
## Third alternative method with similarity to the second,
# use the discord bot code for inspiration on manipulating text files.


##TODO: Compress code into shorthand.
# Do this for clean-up/practice when hopefully all of this works.

## Tinker with code occasionally with new knowledge to implement,
#  Don't think that this is a one-time project.


### Variables

water = {"Water is in bowl":"0", # water(0)
            "Water is not in bowl":"1", # water(1)
            "Water cannot be added into the bowl":"2", # water(2)
            "The bowl is already empty":"3"} # water(3)
   

water_level = {"The bowl is full of water":"0", # waterlevel(0)
                "The bowl is empty":"1"} # waterlevel(1)

### Classes

#class BowlObject:
#    def __init__(self, capacity):
#        global water
#        global water_level

#        self.capacity = water_level

    # def __iter__(self):
#        global water
#        global water_level

#        for water in iter(water_level):
#            if water == (1) and water_level == (1):
#                print("full")
#            elif water == (0) and water_level == (0):
#                print("Empty")
#            else:
#                break
    
#bowl_class = BowlObject()


#class WaterObject:
#   def __init__(self, location):
#       global water
#       global water_level

#       self.location = water
        
#    def __iter__(self):
#        global water
#        global water_level

#        for water in water(i):
#            if water == water(1):
#               self.location = "outside the bowl"
#           elif water == water(0) or water == water(2):
#               self.location = "inside the bowl"
    
#    def overflow(self, state):
#        global water
#        global water_level
 
#        self.state = water 
#        if water == water(2):
#            print("The bowl is overflowing with water \n
#                    and cannot contain more water.")

#water_class = WaterObject()

# TODO: make subclass for interaction of the WaterObject and BowlObject.

class Interaction:
    def __init__(self, ):







### Functions

def addwater():
    global water
    global water_level

    
               

def removewater():
    global water
    global water_level

    

def displaywater():
    global water
    global water_level
    
    print(water)


user_data = input('''\"Choose a Command, entering other data unlike the choices provided results in an error.\" \n
 [A] - add water \n
 [B] - remove water \n
 [C] - display list of responses: ''')


def userinput(): # Use while loop and store all choices in a dict maybe?
    

    if user_data == 'A':
     addwater()
    elif user_data == 'B':
     removewater()
    elif user_data == 'C':
     displaywater()
    elif user_data == 'D':
     exit()
    else:
     print("No such command")

while True: # TODO: Finish for persistence.

    userinput()

# end of code.