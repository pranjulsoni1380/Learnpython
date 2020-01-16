# # looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1,2,3,4.0)

# for loop and tuple
for i in mixed:
    print(i)
    
# NOTE - You can use while loop too

# tuple with one element
nums = (1) # type <class 'int'>
nums = (1.) # type <class 'tuple'> same for strings
words = ('words')


# print(type(nums))

# print(type(words))

# tuple wihtout parenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
# print(type(guitars))

# tuple unpacking

guitarists = ('yamaha', 'baton rouge', 'taylor')
# guitarists1, guitarists2, guitarists3 = (guitarists)
# guitarists1, guitarists2 = (guitarists)  # error
# print(guitarists1)

# list inside tuples

favorites = ('southern magnolia', ['Tokya Ghoul Theme', 'landscape'])
favorites[1].pop()
print(favorites)