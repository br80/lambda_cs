



# Returns the secret to coding
def secretToCoding1():
  print ""
  print "Beautiful code is both ELEGANT and EFFICIENT"
  print "  ELEGANT: short, easy to read, easy to understand, easy to maintain, easy to modify"
  print "  EFFICIENT: minimal CPU operations, minimal memory/storage requirements"
  print ""

# Returns the secret to coding
def secretToCoding2():
  print "\nBeautiful code is both ELEGANT and EFFICIENT\n  ELEGANT: short, easy to read, easy to understand, easy to maintain, easy to modify\n  EFFICIENT: minimal CPU operations, minimal memory/storage requirements\n"


# Which is correct: secretToCoding1() or secretToCoding2()?


# Big-O stands for "order of"




import math
import random
import time
from datetime import datetime



books = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']



##########
# O(1)
##########

# Return the name of all books
def getBooks():
  return books


##########
# O(n)
##########

# O(n) == (n)

# Returns the number of books
def getNumBooks():
  num_books = 0
  for book in books:
    num_books += 1
  return num_books

# Returns each book with all letters lowercase
def getLowercaseBooks():
  lowercase_books = books
  book_index = 0
  for book in books:
    lowercase_books[book_index] = lowercase_books[book_index].lower()
    book_index += 1
  return lowercase_books

# Given the name of a book,
# Return True if that book is in the list, False otherwise
def hasBook(book_name):
  for book in books:
    if book == book_name:
      return True
  return False

# Given the name of a book,
# Return the book's index if that book is in the list, -1 otherwise
def findBook(book_name):
  book_index = 0
  for book in books:
    if book == book_name:
      return book_index
    book_index += 1
  return -1

# Shuffle the order of the stored books
def shuffleBooks():
  num_books = getNumBooks()
  for i in xrange(num_books):
    random_i = random.randrange(num_books)
    temp_storage = books[i]
    books[i] = books[random_i]
    books[random_i] = temp_storage



##########
# O(n^2)
##########

# Print a list of all possible book pairs
def printBookPairs():
  for book1 in books:
    for book2 in books:
      print book1 + " - " + book2



##########
# O(n^3)
##########

# Print a list of all possible book triples
def printBookTriples():
  for book1 in books:
    for book2 in books:
      for book3 in books:
        print book1 + " - " + book2 + " - " + book3



##########
# O(2^n)
##########

# Given a list,
# Return a list of all possible combination of list items that can be checked out
def getListOfCheckoutCombos(l):
  list_length = getLengthOfList(l)
  if list_length == 0:
    return [ [] ]
  else:
    checkoutCombos = []
    previousCombos = getListOfCheckoutCombos( l[1:] )
    for combo in previousCombos:
      checkoutCombos.append( combo )
      checkoutCombos.append( combo + [l[0]] )
    return checkoutCombos



##########
# O(n!)
##########

# Given a list,
# Return a list of all possible arrangements of list items
def getAllArrangements(l):
  list_length = getLengthOfList(l)
  if list_length <= 1:
    return [l]
  else:
    arrangements = []
    previousArrangements = getAllArrangements( l[1:] )
    for previousArrangement in previousArrangements:
      for i in xrange(getLengthOfList(previousArrangement) + 1):
        arrangements.append( previousArrangement[i:] + [l[0]] + previousArrangement[:i] )
    return arrangements



# Given a list,
# Return the list's length
# O(n)
def getLengthOfList(l):
  list_length = 0
  for i in l:
    list_length += 1
  return list_length


# Given a list,
# Return the list's length
# O(1)
def betterGetLengthOfList(l):
  return len(l)


# This can be used to time the runtime of various functions
def printFunctionRuntime():
  start_time = datetime.now()
  x = getAllArrangements(books_10 + ["Kangaroo"])
  end_time = datetime.now()
  print end_time - start_time


# num_books = 9
# num_arrangements = 362,880
# runtime = 1.2 seconds

# num_books = 10
# num_arrangements = 3,628,800
# runtime = 9.6 seconds

# num_books = 11
# num_arrangements = 39,916,800
# runtime = 2 minutes 40.7 seconds


####
# Summarize Big-O
# Google, Facebook test algorithms/computer science because they have the biggest Ns
####


books_1 = ["Aardvark"]
books_2 = ["Aardvark", "Bear"]
books_3 = ["Aardvark", "Bear", "Cat"]
books_4 = ["Aardvark", "Bear", "Cat", "Duck"]
books_5 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant"]
books_6 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo"]
books_7 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe"]
books_8 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo"]
books_9 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana"]
books_10 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana", "Jackal"]
books_sorted = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana", "Jackal"]





