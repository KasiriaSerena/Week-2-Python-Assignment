# create an empty list
my_list = []

# append 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert value 15 at the second position in the list
my_list.insert(1,15)

#extend the list with another 60,70,80
my_list.extend([50,60,70])

#remove the last element from my_list
my_list.pop()

#sort my_list in ascending order
my_list.sort()

#Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(index_of_30)

print(my_list)