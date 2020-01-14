num = [1, 2, 3, 4, 5, 6, 7, 8]

def num_divied(l):
    box = []
    box1 = []
    for i in l:
        if i%2 == 0:
            box.append(i)
        else:
            box1.append(i)
    output = [box,box1]   
    return output
print(num_divied(num))