
# def cube_finder(l):
#     first = {}
#     for i in range(1,l+1):
#         first[i] == i*i*i
#         return first 
# print(cube_finder(10))


# def number_cube(n):
#       cubes = {}
#   for i in range(1,n+1):
#     cubes[i]=i**3
#   return cubes
# print(number_cube(10))
  
  
def cube_finder(n):
    
    cubes = {}

    for i in range(1,n+1):

        cubes[i] = i**3

    return cubes

x = int(input("enter a number : "))

print(cube_finder(x))        