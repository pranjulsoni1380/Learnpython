
user_info = {
    'name' : 'himanshu',
    'age' : 24,
    'fav_movies' : ['coco'],
    'fav_tunes' : ['itunes'],
}
# print(user_info['fav_movies'])

# check if key exist in dictionary

# if 'names' in user_info:
#     print('present')
# else:
#     print('not present')


# check if vaule exist in dictionary

# if 24 in user_info.values():
#     print('present')
# else:
#     print('not present')


# loops in dictionaries

# for i in user_info.values():
#     print(i)

# values method 
# user_info_values = user_info.values()
# print(user_info_values)

# keys method  
# user_info_keys = user_info.keys()
# print(user_info_keys)

# for i in user_info:
#     print(user_info[i])

# items method important

# user_items = user_info.items()
# print(user_items)

for key, item in user_info.items():
    print(f"key is {key} and value is {item}")