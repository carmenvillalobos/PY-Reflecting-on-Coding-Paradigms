# Section 1: Functional Prompt

def flatten_and_sort(array):
    arr = []
    for element in array:
        for i in element:
            arr.append(i)
    return sorted(arr)

# Reflection Questions

# How does this solution ensure data immutability?
# This solution ensures data immutability because it is only allowing the given elements from the parameter array to be pushed into a new array.

# Is this solution a pure function? Why or why not?
# This solution is a pure function because the output depends on the given input (i.e., the parameter array in this case)

# Is this solution a higher order function? Why or why not?
# This is not a higher ordered functions because it does not accept one or more functions as an argument and doesn't return a function

# Would it have been easier to solve this problem using a different programming style?
# I do not think that there would have been an easier way to solve this problem using a different programming style. It is a simple function answers a simple question.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# Functional programming is a helpful paradigm when solving this problem because we are not able to add or delete any of the elements within the array and the output (return statement purely depends on its input)

# Section 2: Object Oriented Prompt
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def boost(self):
        self.max_speed = self.max_speed * 2

