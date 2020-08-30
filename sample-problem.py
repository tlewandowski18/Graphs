# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
dictionary = {
            "cat": "bob",
            "dog": 23,
            19: 18,
            90: "fish"
            }
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

def find_sum_of_ints(dict):
    #create a variable to hold the sum
    sum = 0
    #loop through the dictionary:
    for value in dict.values():
        #if value is int, increase the sum by that value
        if type(value) is int:
            sum += value
    #return sum
    return sum

print(find_sum_of_ints(dictionary))
