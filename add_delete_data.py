user_info = {
    'name' : 'himahsu',
    'age' : 24,
    'fav_movies' : ['coco'],
    'fav_tunes' : ['itunes'],
}

# how to add data

# user_info['fav_songs']  = ['song1', 'song2']
# print(user_info)

# pop method

# user_info.pop('fav_tunes')
# popped_item = user_info.pop('fav_tunes')
# print(f"Popped item {popped_item}")
# print(user_info) 

# popitem method
popped_item  = user_info.popitem()
print(f"Popped item {popped_item}")
print(popped_item) 
