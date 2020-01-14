
num = ['orange', 'mango', 'banana', 'apple']

def revered_num(l):
    element = []
    for i in l:
         element.append(i[::-1])
    return element
print(revered_num(num))

# print(num[0])