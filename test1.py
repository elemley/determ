from math import *
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors
from random import *
from mpi4py import MPI



ARRAYSIZE = 16
start_time = time.time()


def main():
    comm = MPI.COMM_WORLD
    print("Hello! I'm rank %d from %d running in total..." % (comm.rank, comm.size))
    comm.Barrier()  # wait for everybody to synchronize _here_

    fname = "m0016x0016.bin"
    a = np.fromfile(fname)
    print(a)
        #.empty(shape=(ARRAYSIZE, ARRAYSIZE))

    """
    with open(fname, mode='rb') as f:
        test=True
        while test:
            data = f.read(64)
            print(data[2:])
            if len(data) < 64:
                test = False
    """


if __name__ == '__main__':
    main()
print ("--- %s seconds ---" % (time.time() - start_time))






"""
            for i in range(0,ARRAYSIZE):
                for j in range(0,ARRAYSIZE):
                    hex_str = f.read(64)
                    hex_int = int(hex_str, 16)
                    final = float.fromhex(new_int)
                    a[i, j] = final
                    new_int = hex_int + 0x200

                    print("a["+i+","+j+"] = "+a[i,j])
"""
