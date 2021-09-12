from get_matrix_number import *

def sum_diagonal(*array):
    result = 0
    for i in range(len(array)):
        result += array[i][i]

    return result

if __name__ == '__main__':
    row, col = input_row_col("Input two integer greater than 0 (separated by space): ")
    if row != col:
        print("This is not square matrix!!!")
    else:
        array = create_array(row, col)
        print("Initial array: ")
        for i in array:
            print(i)

        print(f"Sum of diagonal matrix is {sum_diagonal(*array)}")