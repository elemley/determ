from math import *
import scipy.linalg
import numpy as np
import array as ar


# LU Decomposition and Calculate Determinant
def lu_det(a):
    determ = 1
    log_determ = 0
    for k in range(0, int(n / m)):
        P, L, U = scipy.linalg.lu(a)
        L_inv = np.linalg.inv(L)
        U_inv = np.linalg.inv(U)
        determ = determ * np.linalg.det(L) * np.linalg.det(U)
        log_determ += log(abs((np.linalg.det(L)))) + log(abs((np.linalg.det(U))))
        for i in range((k + 1), int(n / m)):
            a_mat_ik = a[i, k] * L_inv
            a_mat_ki = a[k, i] * U_inv
            for i in range((k + 1), int(n / m)):
                for j in range((k + 1), int(n / m)):
                    a_mat_jk = a[i, j] - a[i, k] * a[k, j]
                return determ, log_determ

# end


# Read the large/raw matrix and divide it into smaller block
n = int(16)
m = int(4)
lst = []
largematrix = open("m0016x0016.bin", "rb")
output = list(range(int(n / m)))
submatrix_file = []
for i in range(0, int(n / m)):
    for j in range(0, int(n / m)):
        str1 = "submatrix_" + str(i) + "_" + str(j)
        output[j] = open(str1, "w")
    for k in range(0, m):
        for j in range(0, int(n / m)):
            block = largematrix.read(8 * m)
            line = ar.array("d", block)
            output[j].write(str(line.tolist()) + "\n")
    for j in range(0, int(n / m)):
        output[j].close()
# end of reading large matrix

prod_determ = 1.0
sum_logabs_determ = 0.0

# Read the submatrix files and convert the submatrix into lists
for i in range(0, int(n / m)):
    for j in range(0, int(n / m)):
        submatrix_file = open("submatrix_" + str(i) + "_" + str(j), "r")
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
        # Calculate the determinant and log determinant of submatrix by using LU factorization
        determ,logabs_determ = lu_det(megastuffed)
        prod_determ*=determ
        sum_logabs_determ+=logabs_determ
        #print(megastuffed)
        #print('The determinant and log determinant are' + str(determinant_megastuffed))
print( prod_determ, sum_logabs_determ)
        # submatrix_file = open("submatrix_0_0")
        # blockmatrix=[]
        # for i in range (0,(n/m)):
        #     doublesub=submatrix_file.readline()
        #     doublesub1=doublesub.strip('[')
        #     doublesub1 = doublesub1.replace(']','')
        #     doublesub1=doublesub1.split(",")
        #     doublesub1 = list(map(float, doublesub1))
        #     blockmatrix.append(doublesub1)

        # blockmatrix=np.reshape(blockmatrix,(-1, int(len(blockmatrix))))
        # #print(blockmatrix)

        # b=lu_det(blockmatrix)
        # print b






        # print(main())
        # a = np.arange(16).reshape(4, 4)
        # print(np.linalg.det(a), log(abs(np.linalg.det(a))))