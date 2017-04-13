# Given a two-dimensional array in which each row and each column is sorted,
# detect if a given element is in the array

def search_2d(matrix, value):
    """
    Search through the matrix by first excluding the rows and colums not worth the search.
   
    A row will not be worth searching in if its last (highest) value is < target_value, 
    same goes for columns.
   
    """
    start_x, start_y = 0, 0
    
    # Search for the index of the first "interesting" row
    for x in range(len(matrix)):
        if matrix[x][-1] == value:
            return True
        elif matrix[x][-1] < value:
            start_x += 1

    # Search for the index of the first "interesting" column
    for y in range(len(matrix[0])):
        if matrix[-1][y] == value:
            return True
        elif matrix[-1][y] < value:
            start_y += 1

    # Scan remaining values
    for x in range(start_x, len(matrix)):
        for y in range(start_x, len(matrix[0])):
            if matrix[x][y] == value:
                return True
    return False
