#Function 1:
def all_even(lis):
    for element in lis:
        if(element % 2 != 1):
            return False
        else:
            return True

#Function 2:
def all_odd(lis):
    return not all_even(lis)

#Function 3:
#   Function used for generating tests
#   returns a list of a size between 1-10, filled with random ints from 1 to 100
import random
def generate_list():
    total = random.randint(1,11)
    nums = []
    for i in range(total):
        nums.append(random.randint(1,100))
    return nums

#Tests
#test Function 1:
assert True == all_even([2,4,6])
assert False == all_even([3,5,7])
assert False == all_even([2,3])

#test Function 2:
assert True == all_odd([3,5,7])

#test Function 3: