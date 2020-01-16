# Q - What are dictionaries
# A - unordered collections of data in key : value pair.

# How to create dictionaries

user = {'name' : 'Himanshu', 'age' : 24}
print(user)

# second method to create dictionary
user1 = dict(name = 'himanshu', age = 24)
print(user1)

# how to access data form dictionary
# note - There is no indexing because of unordered collections of data.
print(user['name'])
print(user['age'])

# which type of data a dictionary can store ?
# anything
# number, strings, list , dictionary

user_info = {
    'name' : 'himahsu',
    'age' : 24,
    'fav_movies' : ['coco'],
    'fav_tunes' : ['itunes'],
}
print(user_info['fav_movies'])
