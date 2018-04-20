from math import *
import time
import os
import numpy as np
from mpi4py import MPI

start_time = time.time()

def main():
    #open up communications for MPI # of nodes/cores established from command line call:
    #mpiexec -n 8 -f machinefile python parallel_test1.py
    comm = MPI.COMM_WORLD
    #print(comm.rank, comm.size)
    #KEEP IN MIND -- this code will execute on all pis!
    #SO, wherever you see something like: if comm.rank == x:
    #THIS IS HOW YOU EXECUTE ON ONLY ONE PI
    #NOTE: head node is referred to 0, the worker nodes (pis) are 1-7

    filebase="submatrix_"

    # modify as necessary
    #full matrix = 16x16
    #block = 4x4
    n = 16
    m = 4

    block_count = 1 # this will keep track of which processor / pi we are doing work on.. not using rank = 0 to do actual work

    if comm.rank == 0:  #only do this if head node
        determs = []    #make a list of results arrays

    for i in range(0,int(n/m)):
        for j in range(0,int(n/m)):
            filestr = filebase+ str(i) + "_" + str(j)
            #next read in each file but only on head node
            if comm.rank == 0:  #only do this if head node
                submatrix_file = open(filestr, "r")
                megastuffed = []
                for k in range(0, int(n / m)):
                    doublestuffed = submatrix_file.readline()
                    singlestuffed = doublestuffed.strip('[')
                    singlestuffed = singlestuffed.replace(']', '')
                    singlestuffed = singlestuffed.split(",")
                    singlestuffed = list(map(float, singlestuffed))
                    megastuffed.append(singlestuffed)
                # Reshape the list into matrix shape
                megastuffed = np.reshape(megastuffed, (-1, int(len(megastuffed))))
                #now send array to a selected pi (block_count)
                comm.Send([megastuffed, MPI.DOUBLE], dest = block_count, tag = 99)
                #Ignore the tags for now

            if comm.rank == block_count:    #only executed if processor = block_count
                #make a place to receive the matrix to do work on
                my_block = np.empty(m * m, dtype=np.float64)
                my_block = np.reshape(my_block, (m, m))
                #Next line is to receive the matrix into my_block from the head node (0)
                comm.Recv([my_block , MPI.DOUBLE], source = 0, tag=99)
                #print(my_block, comm.rank)

            if comm.rank == block_count:
                # here is where work can be done on each block (i.e. LU decomp)
                result = np.linalg.det(my_block)
                my_determ = np.empty(1, dtype=np.float64)
                my_determ[0] = result
                #you have to send back to the head node... but you can't send back a float/double -- so here's a 1x1 array
                comm.Send([my_determ, MPI.DOUBLE], dest=0, tag=88)

            if comm.rank == 0:
                curr_determ = np.empty(1, dtype=np.float64)
                comm.Recv([curr_determ, MPI.DOUBLE], source=block_count, tag=88)
                determs.append(curr_determ)

            if block_count < comm.size -2:
                block_count+=1
            else:
                block_count = 1
                comm.Barrier()  # wait for everybody to synchronize _here_

    if comm.rank == 0:
        print(determs)

    """
    for r in range(comm.size):
        if comm.rank == r:
            print("[%d] %s" % (comm.rank, my_block))
        comm.Barrier()
    """

    #a = np.fromfile(fname)







if __name__ == '__main__':
    main()
print ("--- %s seconds ---" % (time.time() - start_time))




