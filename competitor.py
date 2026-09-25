A: list[int] = [None] * 10**6 # we default setup a fixed list
cnt: int = 0 # size of array
i_max = -1 # index of largest element

def push(key : int):
    # use current cnt as index and insert value

    # if i_max is -1 or the new value is greater than current max
    # update i_max as the new index

    # now add one more to cnt
    pass # remove this line when coding. this is to stop the code from failing

def pop() -> int | None:
    # if i_max is -1 return None

    # set key_max to the current max (ie value at index i_max)
    # swap max value item with last item
    # reduce total count by 1

    # if total count is 0 set i_max to -1

    # linear search from left to right to find the max
    
    # return the max key
    return 


def getTop(s) -> int | None:
    # if i_max is -1 return None
    
    # return the key at i_max
    return 


    
"""
If you're up for it (it's not difficult), you could use classes
in this case we could create a class called Compatitor, 
The usage is very similar but it's a lot cleaner, as a class nicely encapsulate it's own data. 
There's other benefits but it's not relevent right now
to change the above there's one thing to note. each function needs to pass in a `self` as the first parameter
You don't have to worry about how to pass it in, it's automatic and refers to the current instance you're working with

this self MUST be used before it's internal parameters for it to work.

Example:

1. setup a class
class Competitor:
    A: list[int] = [None] * 10**6 # we default setup a fixed list

    def push(self, key : int): # notice the self here
        # any variables defined here do not need to use self
        local_var = key
    
        self.list.push(local_var) # self points to the properties (ie variables) for this instance.

        ...

2. Using it from an experiment file
from competitor import Competitor

3. add a single line before using your competitor to create an instance:
   competitor = Competitor() 

4. use as you do without class

"""