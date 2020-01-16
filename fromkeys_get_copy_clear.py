  # fromkeys
  
# d = {'name' : 'unknown', 'age' : 'unknown'}
  
# d = dict.fromkeys(range(1,11), 'unknown')
# d = dict.fromkeys("abc", 'unknown')
# d = dict.fromkeys(['name', 'age'], ['unknown', 'unknown'])

# print(d)


# get method
d = {'name' : 'Harshit', 'age' : 'unknown'}
print(d['name'])

# print(d.get('name')) better

if 'name' in d:
    print('present')
else:
    print('not present')

if  d.get('name'):
    print('present')
else:
    print('not present')
    
# d.clear()
# print(d)

d1 = d.copy()
print(d1)

print(d1.popitem())
print(d)
print(d1 == d)