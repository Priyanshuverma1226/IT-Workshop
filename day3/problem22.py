# Write a function which checks if all the items of the list are of the same data type.


test_list = [1, "verma", 4, 6, 7]

# printing original list
print("The original list is : " + str(test_list))

flag = 0

# using naive method
# to check all unique list elements
for i in range(len(test_list)):
	for i1 in range(len(test_list)):
		if i != i1:
			if type(test_list[i]) != type(test_list[i1]):
				flag = 1


# printing result
if(not flag):
	print("List contains all same Datatype")
else:
	print("List contains does not contains all same Datatype")

