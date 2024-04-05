# 1 Functional Prompt
# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
#


class functional_prompt:

  def __init__(self, array):
    self.array = array


array = [
    4,
    51,
    46,
    78,
    115,
]


def orginization(array):
  return sorted(array)


print(orginization(array))

# def functional_prompt(array):
#     return sorted(array)

# print(functional_prompt(array))

data = [15, 50, 45, 90, 2, 3, 84, 15]


def clean(data):
  return sorted(data)


print(clean(data))

# Once a functional solution to this problem has been implemented, answer the following questions.
# How does this solution ensure data immutability?
# Is this solution a pure function? Why or why not?
# Is this solution a higher order function? Why or why not?
# Would it have been easier to solve this problem using a different programming style?
# Why in particular is functional programming a helpful paradigm when solving this problem?

#The data is safe from change by using specific names of refernce of names however if someone were to put in a string the list, it would break.
#The solution is pure as it process a desired outcome by formatting and array of numbers into a ascending order.
#It is a fucntion that can take another function by using class and __init__.
#No i think python is easier to understand and its format is cleaner as javascript is a bit messy.
#I think that paradigmm is helpful when solving this problem because of the fact one could put in a function within this function.

#<------------------------------------------------>#
# 2 Object Oriented Prompt
# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.
# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
# Define a repair() method that will update the condition of the podracer to "repaired".
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".


class Podracer:
  def __init__(self,max_speed,condition,price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price


  def repair(self):
    self.condition = "repaired"

class AnakinPod(Podracer):
  def __init__(self, max_speed,condition,price):
    super.__init__(max_speed,condition,price)


    def boost(self):
      self.max_speed *= 2


class SebulbasPod(Podracer):
  def __init__(self, max_speed,condition,price):
    super.__init__(max_speed, condition, price)

    def flame_jet(self,other):
      other.condition = "trashed"



