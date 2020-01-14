# for i in range(1,11):

#     print (i)

def reserver_print(l):
    # l.reverse()
    numb = []
    # return l
    for i in range(len(l)):
            popped_item = l.pop()
            numb.append(popped_item)
    return numb

number = list(range(1,11))
print(reserver_print(number))