import random

# Returns a random floating-point number in the range [0.0, 1.0).
# where 1.0 is not inclusive, rather its exclusive.
tomi_random = random.random()

# returns an integer number in the range of [1,10].
# Where a and b are inclusive.
angie_random_integer = random.randint(1,10)

#Returns a random floating-point number between and (inclusive on both ends).
tomi_uniform = random.uniform(2.8,4.5)

# Returns a choosen word in the data list.
tomi_colors = ["red","yellow","green","white","turquoise"]
tomi_choice = random.choice(tomi_colors)


print(tomi_random)
print(angie_random_integer)
print(tomi_uniform)
print(tomi_choice)
