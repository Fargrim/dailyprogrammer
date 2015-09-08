initial_cells = '                                                 X                                                 '


print str(initial_cells)

cell_count = len(initial_cells)
for k in range(0, 25):
    c = 0
    next_row = ''
    initial_cells_list = list(initial_cells)
    while c < cell_count:
        minus_one = c - 1
        plus_one = c + 1
        # handling the first entry, which has no left-hand neighbor -- assumed to be 0
        if c == 0:
            if initial_cells_list[plus_one] == '1':
                next_row = 'X'
            else:
                next_row = ' '
        # handling the last cell, which has no right-hand neighbor -- assumed to be 0
        elif c == cell_count - 1:
            if initial_cells_list[minus_one] == '1':
                next_row += 'X'
            else:
                next_row += ' '
        else:
            # an XOR evaluation of the values one cell before and after the current cell
            if initial_cells_list[minus_one] != initial_cells_list[plus_one]:
                next_row += 'X'
            else:
                next_row += ' '
        c += 1
    print str(next_row)
    initial_cells = next_row
    k += 1
