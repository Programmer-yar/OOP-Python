"""
'Yield' statement gives the output of a function as soon as it is generated
"""
def even(test_list):
    for i in test_list:
        if i % 2 == 0:
            yield i


test_list = [1, 4, 5, 6, 9]

print('The original list is: ' + str(test_list))

print('The even number in the list are: ', end = " ")
for j in even(test_list):
    print(j, end = " ")
