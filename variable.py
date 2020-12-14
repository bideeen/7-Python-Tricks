# varaible function
def switch(i,j):
    # Declaring the variables
    a = i
    b = j
    # Switching the varibles
    a = b
    b = a
    return a,b

def main():
    try:
        i = int(input('First variable: '))
        j = int(input('Second Varible: '))
        x,y = switch(i, j)
        print(f'The first value is now: {x}')
        print(f'The second value is now: {y}')
    except ValueError:
        print('Invalid Value')
        i = int(input('First variable: '))
        j = int(input('Second Varible: '))
        x,y = switch(i, j)
        print(f'The first value is now: {x}')
        print(f'The second value is now: {y}')

if __name__ == "__main__":
    main()