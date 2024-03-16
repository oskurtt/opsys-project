import sys
import random
import math
import string
from utils import Rand48

rand48 = Rand48()
alpahbet = string.ascii_uppercase

def next_exp(lamda, upper_bound):
    iterations = 1000000
    i = 0
    while i < iterations:
        r = rand48.drand()
        x = (- (math.log(r)) / lamda)

        if ( x > upper_bound ):
            continue
        i += 1

        return x

    
def main():
    try:
        n = int(sys.argv[1])
        ncpu = int(sys.argv[2])
        seed = int(sys.argv[3])
        lamda = float(sys.argv[4])
        upper_bound = int(sys.argv[5])

    except Exception as e:
        print(f"ERROR: {e}")
        return 0
    
    rand48.srand(seed)
    if (ncpu > 1 or ncpu == 0):
        print(f"<<< PROJECT PART I -- process set (n={n}) with {ncpu} CPU-bound processes >>>")
    else:
        print(f"<<< PROJECT PART I -- process set (n={n}) with {ncpu} CPU-bound process >>>")

    for i in range(n):
        arrival_time = math.floor(next_exp(lamda, upper_bound))
        num_cpu_burst = math.ceil(rand48.drand()*64)

        if i < (n - ncpu):
            print(f"I/O-bound process {alpahbet[i]}: arrival time {arrival_time}ms; {num_cpu_burst} CPU bursts:", end ='')
        else:
            print(f"CPU-bound process {alpahbet[i]}: arrival time {arrival_time}ms; {num_cpu_burst} CPU bursts:", end = '')

        for j in range(num_cpu_burst):
            
            cpu_burst_time = math.ceil(next_exp(lamda, upper_bound))
                
            if j != num_cpu_burst - 1:
                io_burst_time = math.ceil(next_exp(lamda, upper_bound)) * 10

            if not (i < (n - ncpu)):
                cpu_burst_time = cpu_burst_time*4
                io_burst_time = math.floor(io_burst_time/8)
            

            print()
            if (j == num_cpu_burst - 1):
                print(f"--> CPU burst {cpu_burst_time}ms", end = '')
            else:
                print(f"--> CPU burst {cpu_burst_time}ms --> I/O burst {io_burst_time}ms", end = '')

        print()
    
main()