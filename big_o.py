



# Returns the secret to beautiful code
def secret_to_coding_1():
  print ("")
  print ("Beautiful code is both ELEGANT and EFFICIENT")
  print ("  ELEGANT: concise, easy to read, easy to understand, easy to maintain, easy to modify")
  print ("  EFFICIENT: minimal CPU operations, minimal memory/storage requirements")
  print ("")


# Returns the secret to beautiful code
def secret_to_coding_2():
  print ("\nBeautiful code is both ELEGANT and EFFICIENT\n  ELEGANT: short, easy to read, easy to understand, easy to maintain, easy to modify\n  EFFICIENT: minimal CPU operations, minimal memory/storage requirements\n")


# Which code is more beautiful: secretToCoding1() or secretToCoding2()?



import math
import random
import time
from datetime import datetime

animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


##########
# O(1)
##########

# Return the name of all animals
def get_animals():
  return animals


##########
# O(n)
##########

# Returns the number of animals
def count_animals():
    num_animals = 0
    for animal in animals:
        num_animals += 1
    return num_animals




# Returns each animal with all letters lowercase
def get_lowercase_animals():
    lowercase_animals = list(animals)
    animal_index = 0
    for animal in animals:
        lowercase_animals[animal_index] = lowercase_animals[animal_index].lower()
        animal_index += 1
    return lowercase_animals



# Given the name of a animal,
# Return True if that animal is in the list, False otherwise
def has_animal(animal_name):
    for animal in animals:
        counter += 1
        if animal == animal_name:
            return True
    return False




# Given the name of a animal,
# Return the animal's index if that animal is in the list, -1 otherwise
def find_animal(animal_name):
    animal_index = 0
    for animal in animals:
        if animal == animal_name:
            return animal_index
        animal_index += 1
    return -1




# Shuffle the order of the stored animals
def shuffle_animals():
    num_animals = count_animals()
    for i in range(num_animals):
        random_i = random.randrange(num_animals)
        temp_storage = animals[i]
        animals[i] = animals[random_i]
        animals[random_i] = temp_storage



##########
# O(n^2)
##########

# Print a list of all possible animal pairs
def print_animal_pairs():
    for animal_1 in animals:
        for animal_2 in animals:
            print (f"{animal_1} - {animal_2}")



##########
# O(n^3)
##########

# Print a list of all possible animal triples
def print_animal_triples():
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print (f"{animal_1} - {animal_2} - {animal_3}")



##########
# O(2^n)
##########

# Given a list,
# Return a list of all possible combination of animals
def get_animal_combos(l):
    list_length = len(l)
    if list_length == 0:
        return [ [] ]
    else:
        animal_combos = []
        previous_combos = get_animal_combos( l[1:] )
        for combo in previous_combos:
            animal_combos.append( combo )
            animal_combos.append( combo + [l[0]] )
        return animal_combos



##########
# O(n!)
##########

# Given a list,
# Return a list of all possible arrangements of list items
def get_all_arrangements(l):
    list_length = len(l)
    if list_length <= 1:
        return [l]
    else:
        arrangements = []
        previous_arrangements = get_all_arrangements( l[1:] )
        for previous_arrangement in previous_arrangements:
            for i in range(len(previous_arrangement) + 1):
                arrangements.append( previous_arrangement[i:] + [l[0]] + previous_arrangement[:i] )
        return arrangements



# Given a list,
# Return the list's length
# O(n)
def get_length_of_list(l):
    list_length = 0
    for i in l:
        list_length += 1
    return list_length


# Given a list,
# Return the list's length
# O(1)
def better_get_length_of_list(l):
    return len(l)


# This can be used to time the runtime of various functions
def print_function_runtime():
    start_time = datetime.now()
    x = get_all_arrangements(animals_11)
    # x = get_all_arrangements(animals_10 + ["Kangaroo"])
    end_time = datetime.now()
    print (end_time - start_time)


# num_animals = 9
# num_arrangements = 362,880
# runtime = 1.2 seconds

# num_animals = 10
# num_arrangements = 3,628,800
# runtime = 9.6 seconds

# num_animals = 11
# num_arrangements = 39,916,800
# runtime = 2 minutes 40.7 seconds


animals_1 = ["Aardvark"]
animals_2 = ["Aardvark", "Bear"]
animals_3 = ["Aardvark", "Bear", "Cat"]
animals_4 = ["Aardvark", "Bear", "Cat", "Duck"]
animals_5 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant"]
animals_6 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo"]
animals_7 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe"]
animals_8 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo"]
animals_9 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana"]
animals_10 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana", "Jackal"]
animals_11 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana", "Jackal", "Kangaroo"]

animals_sorted = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana", "Jackal"]





