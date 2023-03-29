import random

# your code here

def generate_random ():
    r = random.randint(0, 9)
    return r

print(generate_random())

print("Random number between 0 and 9 is % s" % generate_random())