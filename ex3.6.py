def create_matrix(length, width):
    h_line, v_line, square = '+', '|', ''
    for i in range(width):
        h_line += '---+'
        v_line += '   |'

    square += (h_line + '\n' + v_line + '\n') * \
              length + h_line
    return square


print(createMatrix(7, 5))
