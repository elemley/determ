from math import *
import time
import numpy as np
import scipy
import scipy.linalg
import pprint
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors
from random import *
from mpi4py import MPI

start_time = time.time()


def main():

    fname = "m0016x0016.bin"
    a = np.fromfile(fname)

    a_mat = np.reshape(a,(-1,16))
    #print(a_mat)

    P, L, U = scipy.linalg.lu(a_mat)

    #print(P)
    #print(L)
    #print(U)

    signL, detL = np.linalg.slogdet(L)
    signU, detU = np.linalg.slogdet(U)

    test1 = signL * np.exp(detL)
    test2 = signU*np.exp(detU)
    print(test1, test2)

    print(detL)
    print(detU)


    #pprint.pprint(P)
    #pprint.pprint(L)
    #pprint.pprint(U)






















if __name__ == '__main__':
    main()
print ("--- %s seconds ---" % (time.time() - start_time))
