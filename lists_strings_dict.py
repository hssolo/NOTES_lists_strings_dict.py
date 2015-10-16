#Plain Lists
list = ["a", "b", "c"]
for v in list:
  print v
#Outputs:
#a
#b
#c

# -----------------------------------------------------------------------------------------------------------------------------

#Dictionaries, only by keys
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

#Dictionaries, with keys, printing the associated value
dict = {"a": 1, "b": 2, "c": 3}
for v in dict: ### Translates to: loop through each item/key in the dictionary.
  print dict[v] ### Translates to: after each iteration print the associated item/key value.
  				### The dictionary "dictionay name [give me the value of each key] or dict[v]"
#Outputs:
#1
#3
#2

#This is equivalent to for k in dict.keys():..., but much faster.
dict = {"a": 1, "b": 2, "c": 3}
for v in dict.keys():
	print v
#Outputs:
#1
#3
#2

#Dictionaries, by accessing only the values
dict = {"a": 1, "b": 2, "c": 3}
for v in dict.itervalues():
  print v
#Outputs:
#1
#2
#3

# -----------------------------------------------------------------------------------------------------------------------------

#Dictionaries, with unpacked keys and values
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



# -----------------------------------------------------------------------------------------------------------------------------

#Getting a list of keys from a dictionary
dict = {"a": 1, "b": 2, "c": 3}
print dict.keys()
#Outputs:
#['a', 'c', 'b']

# -----------------------------------------------------------------------------------------------------------------------------

#Getting a list of values from a dictionary
dict = {"a": 1, "b": 2, "c": 3}
print dict.values()
#Outputs:
#[1, 3, 2]