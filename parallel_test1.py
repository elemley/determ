from math import *
import time
import numpy as np
from mpi4py import MPI

start_time = time.time()

def main():
    comm = MPI.COMM_WORLD
    print("Hello! I'm rank %d from %d running in total..." % (comm.rank, comm.size))
    comm.Barrier()  # wait for everybody to synchronize _here_



if __name__ == '__main__':
    main()
print ("--- %s seconds ---" % (time.time() - start_time))




