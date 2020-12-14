import time
# varaible function
# Don't DO THIS ANYMORE
def case_1(i,j):
    # Declaring the variables
    a = i
    b = j
    # Switching the varibles
    a = b
    b = a
    return a,b
# Use THIS when switching variable
def case_2(i,j):
    # Declaring the variables
    a = i
    b = j
    # Switching the varibles
    a,b = b,a
    return a,b


def main():
    try:
        i = int(input('First variable: '))
        j = int(input('Second Varible: '))
        # case_1
        case_1_start = time.time()
        x,y = case_2(i, j)
        case_1_stop = time.time()
        case_1_runtime = case_1_stop - case_1_start
        print(f'The case 1 first value is now: {x}')
        print(f'The case 1 second value is now: {y}')
        print(f'The runtime for case 1 is : {case_1_runtime}')
        # case_1
        case_2_start = time.time()
        e,f = case_2(i, j)
        case_2_stop = time.time()
        case_2_runtime = case_2_stop - case_2_start
        print(f'The case 2 first value is now: {e}')
        print(f'The case 2 second value is now: {f}')
        print(f'The runtime for case 2 is : {case_2_runtime}')
    except ValueError:
        print('Invalid Value')
        i = int(input('First variable: '))
        j = int(input('Second Varible: '))
        # case_1
        case_1_start = time.time()
        x,y = case_2(i, j)
        case_1_stop = time.time()
        case_1_runtime = case_1_stop - case_1_start
        print(f'The case 1 first value is now: {x}')
        print(f'The case 1 second value is now: {y}')
        print(f'The runtime for case 1 is : {case_1_runtime}')
        # case_1
        case_2_start = time.time()
        e,f = case_2(i, j)
        case_2_stop = time.time()
        case_2_runtime = case_2_stop - case_2_start
        print(f'The case 2 first value is now: {e}')
        print(f'The case 2 second value is now: {f}')
        print(f'The runtime for case 2 is : {case_2_runtime}')

if __name__ == "__main__":
    main()