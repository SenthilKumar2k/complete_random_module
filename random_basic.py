import random

print(random.random())        # print random num 0 to 1 in the form of float
print(random.uniform(1,10))   # print random num 1 to 10 in the form of float
print(random.randint(111111,999999))  # print random number inthe form of int
lit=[1,5,9,7,3]
print(random.choice(lit))     # print random number from the list
print(random.sample(lit, 2))  # print 2 random num from the lit in form of list
print(random.sample(lit, 3))  # print 3 random num from the lit in form of list
random.shuffle(lit)           # helps to suffle the list 
print(lit) 