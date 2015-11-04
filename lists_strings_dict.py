
### Dictionaries ###

## dictionary structure is like: dict_name{keys: values} 
x = {'a': 1, 'b': 2, 'c': 3}
print x
#Outputs {a:1, b:2, c:3}

## Use in to lookup or reference any key in a dictionary.
'c' in x
#Outputs True. Should I have called for d or anything else outside the x dictionary above it would have outputed False.
#Note: This does not work on a value

## To access just one element in the dictionary, you have to call that dictionary with the name of the key that you want to look up
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print dictionary['key1']
#Outputs value1 or the requested key's value 

# -----------------------------------------------------------------------------------------------------------------------------

## Dictionaries, only by keys
dict = {"a": 1, "b": 2, "c": 3}
for v in dict: #### Translates to: loop through each item/keyin the dictionary
  print v        ## Translates to: after each iteration print the item/key name.
  				### outputs each item in dictionary kind of like lists above with no mention of values.##
  				### Treats it like a list since the dictionary is essentially a list with values assciated to each item ###
#Outputs:
#a
#b
#c

# -----------------------------------------------------------------------------------------------------------------------------

## Dictionaries, with keys, printing the associated value
dict = {"a": 1, "b": 2, "c": 3}
for v in dict: ### Translates to: loop through each item/key in the dictionary.
  print dict[v] ### Translates to: after each iteration print the associated item/key value.
  				### The dictionary "dictionay name [give me the value of each key] or dict[v]"
#Outputs:
#1
#3
#2

## This is equivalent to for k in dict.keys():..., but much faster.
dict = {"a": 1, "b": 2, "c": 3}
for v in dict.keys():
	print v
#Outputs:
#1
#3
#2

## Dictionaries, by accessing only the values
dict = {"a": 1, "b": 2, "c": 3}
for v in dict.itervalues():
  print v
#Outputs:
#1
#2
#3

# -----------------------------------------------------------------------------------------------------------------------------

## Dictionaries, with unpacked keys and values
dict = {"a": 1, "b": 2, "c": 3}
for k, v in dict.items(): #or .iteritems() in Python <3.x
  print k
  print v
#Outputs:
#a
#1
#c
#3
#b
#2

# -----------------------------------------------------------------------------------------------------------------------------

## Getting a list of keys from a dictionary
dict = {"a": 1, "b": 2, "c": 3}
print dict.keys()
#Outputs:
#['a', 'c', 'b']

#----------------------------------------------------------------------------------------------------------------------------

## Getting a list of values from a dictionary
dict = {"a": 1, "b": 2, "c": 3}
print dict.values()
#Outputs:
#[1, 3, 2]

#----------------------------------------------------------------------------------------------------------------------------

### lists ###

# Lists are mutable and maintain order
# The order in which you add stuff to your list is the order that the list will retain.
# Examples:

#----------------------------------------------------------------------------------------------------------------------------

## iterating over a plain List
list = ["a", "b", "c"]
for v in list:
  print v
#Outputs:
#a
#b
#c

#----------------------------------------------------------------------------------------------------------------------------

## Delete the end of the list with .pop( )
li = [1, 5, 3]
print li
#Outputs [1, 5, 3]
li.pop()
#reomves 3
print li
#Outputs [1, 5]
#Note: works in reverse order with a tuple

#----------------------------------------------------------------------------------------------------------------------------

## lists are zero indexed ex:
# the letter L or l holds the value of 0
li[0]
#Outputs 1 the letter L (lower case)

#----------------------------------------------------------------------------------------------------------------------------

## append to the list. 
li = []
li.append(1)
li.append(5)
li.append(3)
print li
#Outputs [1, 5, 3]

#----------------------------------------------------------------------------------------------------------------------------

## Select a range between index 1 and 3 (closed/open range,math terms).
li = [1, 2, 4, 3, 5]
print li
#Outputs [1, 2, 4, 3, 5]
li[1:3]
#Outputs [2, 4]

#----------------------------------------------------------------------------------------------------------------------------

## Omit the beginning, more like start from position 2.
li = [1, 2, 4, 3, 5]
print li 
#Outputs [1, 2, 4, 3, 5]
li[2:] 
#Outputs [4, 3, 5]

#----------------------------------------------------------------------------------------------------------------------------

## Select every second entry (i.e. step by 2).
li = [1, 2, 4, 3, 5]
print li 
#Outputs [1, 2, 4, 3, 5]
li[::2] 
#Outputs[1, 4, 5]

#----------------------------------------------------------------------------------------------------------------------------

## Reverse the list order.
li = [1, 2, 4, 3, 5]
print li 
# Outputs [1, 2, 4, 3, 5]
li[::-1] 
#Outputs [5, 3, 4, 2, 1]
#Note the syntax is: li[start:end:step]

#----------------------------------------------------------------------------------------------------------------------------

## Delete an item by index number from list li.
li = [1, 2, 4, 3, 5]
print li 
#Outputs [1, 2, 4, 3, 5]
del li[2] 
print li 
#Outputs [1, 2, 3, 5]

#----------------------------------------------------------------------------------------------------------------------------

## Check if an item is in list li.
li = [1, 2, 4, 3, 5]
print li 
#Outputs [1, 2, 4, 3, 5]
1 in li 
#Outputs True

#----------------------------------------------------------------------------------------------------------------------------

## Check the length of characters of list li.
li = [1, 2, 4, 3, 5]
print li 
#Outputs [1, 2, 4, 3, 5]
len(li) 
#Outputs 4 
#Note: lists are zero indexed!!
#Note: within a list, length or .len is testing for elements (or items) within that list not each indicidual character.
#----------------------------------------------------------------------------------------------------------------------------

## Omit any item from list from a certain position onward.
li = [1, 2, 4, 3, 5]
print li 
#Outputs [1, 2, 4, 3, 5]
li[:3]
print li
#Outputs [1, 2, 4]

#----------------------------------------------------------------------------------------------------------------------------
