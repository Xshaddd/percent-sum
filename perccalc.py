import msvcrt
def calculate_percentage(matrix: list) -> float:
    """Returns algebraic sum of a*b/100 formula, where a is value in matrix[0][n] and b is in matrix[1][n]"""
    sum = 0
    for i in range(0, len(matrix[0])):
        sum += matrix[0][i]*matrix[1][i]/100
    
    return sum

if __name__ == '__main__':
    pairs_list = []
    pairs_list.append([])
    pairs_list.append([])

    print("Enter a string in \"a b\" format. Inputs must be float or int! Enter empty string to stop inputs.")
    new_string = input()
    while new_string != "" :
        try: 
            pair = list(map(float, new_string.split()))
            if len(pair) != 2:
                raise Exception()
        except: 
            print("Wrong input type or amount of values. Enter the value again:")
            new_string = input()
            continue

        pairs_list[0].append(pair[0])
        pairs_list[1].append(pair[1])
        new_string = input()
    
    print(calculate_percentage(pairs_list),"\nPress any key to continue...")
    msvcrt.getch()