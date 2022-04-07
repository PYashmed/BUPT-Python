import random

print(dir(random))

# * randint : return a random int
# ^ random.randint(a,b) from a to b include b
print(random.randint(1, 100))

# * random : return a random float
# ^ random.random() no parameter func,ans between 0 and 1
print(random.random())
# ^ get a random float between 100 and 120
print(100+random.random()*20)
