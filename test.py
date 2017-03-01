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

first_path = matrix_test.find_path(first_letter[0], [])

if first_path:
    for i in first_path:
        print i