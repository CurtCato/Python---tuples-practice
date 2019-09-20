# Practice: Tuples
zoo = ("dog", "cat", "flamingo", "python", "stingray", "shark", "anteater", "fish", "mouse", "elephant")
print(zoo.index("cat"))

animal_to_find = "flamingo"
if animal_to_find in zoo:
    print(animal_to_find)

(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth) = zoo
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)
print(eighth)
print(ninth)
print(tenth)

zoo_list = list(zoo)
print(zoo_list)

zoo_list.extend(["buffalo", "chicken", "hippo"])

tup_list = tuple(zoo_list)
print(tup_list)