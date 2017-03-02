from graph import *


grids = [
    ['1', 'B', 'a', 'b', 'T'],
    ['T', 'T', 'C', 'H', 'B'],
    ['H', 'A', 'H', 'B', 'E'],
    ['E', 'C', 'D', 'U', 'I']
]
string_input = 'THACHBUI'

matrix_test = Grids(grids, string_input)

# for node in matrix_test.nodes:
#     print node.__dict__


first_letter = matrix_test.letters_path[0]



print matrix_test.find_path()

for i, value in enumerate(matrix_test.string):
    print i ,value

while len(grids) != 0:
    print grids.pop()