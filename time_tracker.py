# Import time library
import time
# Start time
start_time = time.time()

# The main function to perform some calculation
def main():
    return list(i%2 for i in range(31))

# call the fubction
if __name__ == "__main__":
    
    main()
    # the time the functin finished execution
    end_time = time.time()
    # The total time 
    totalTime = end_time - start_time
    print(f'Time taken to execute code= {totalTime}')
