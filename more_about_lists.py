# generate lists with range functions
# something more about pop method
# index method
# pass list to a function
# number = list(range(1,11))
# # print(number)
# # number.pop()
# # print(number)
# print(number.index(1))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))