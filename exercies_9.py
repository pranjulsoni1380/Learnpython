



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1 = ['word1', 'word2','word3', 'word4']
# numbers = int(4)
# print(numbers*numbers)


def negative_list(l):
    negative = []
    for i in l:
        negative.append(i)
    return negative

print(negative_list(numbers[::-1]))
print(negative_list(numbers1[::-1]))