#In Python a list is a data structure that holds an ordered collection of items which can include various data types and even lists within the list
#Lists are mutable which means we can change their content without changing the identity

#example list
my_list = [1,2,6,7]
print(my_list)

#You can access different positions using bracket notation as per usual. Also you can replace data in certain positions using bracket notation as well
print(my_list[2])

my_list[0] = 0
print(f"{my_list} replaced pos 0 with 0")

#using the .append method we can add data to the end of the list
my_list.append(19)
print(my_list)

#Insert method can add any element in a list. Key word is add not replace. The method needs 2 arguments the position and the data you want to replace
my_list.insert(1, 1)

print(my_list)

#pop method will remove the last element of the list
#By deafult it removes the last element but you can pass an index as an arguement to choose to index to remove
my_list.pop()
print(my_list)