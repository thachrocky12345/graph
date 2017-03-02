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

for row in matrix_test.letters_path:
    print [str(i) for i in row]
    print ""


print matrix_test.find_path()