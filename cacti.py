def cacti_number(array2d):
    counter = 0
    rows = len(array2d)
    columns = len(array2d[0])

    for i in range(rows):
        for j in range(columns):
            while i = 0:
                if array2d[i][j+1]:
                    empty = False
                
            if array2d[i][j+1] == 1:
                empty = False
            if array2d[i][j-1] == 1:
                empty = False
            if array2d[i+1][j] == 1:
                empty = False
            if array2d[i-1][j] == 1:
                empty = False
            if array2d[i+1][j+1] == 1:
                empty = False
            if array2d[i-1][j-1] == 1:
                empty = False
        
            if empty:
                counter += 1

    return counter