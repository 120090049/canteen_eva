import openpyxl
import numpy as np
from numpy.linalg import *

def revenue_rating():

    # Define variable to load the dataframe
    dataframe = openpyxl.load_workbook("readTest.xlsx")

    # Define variable to read sheet
    dataframe1 = dataframe.active

    # store the raw data
    table = []
    row_num = dataframe1.max_row
    col_num = dataframe1.max_column

    # average of revenue
    r = 117450 

    # A=x*(7+41) B=(7+41)*1 C=x*1
    A_row = [0]*46
    A = []
    C = []

    # record the missed data position
    needPredict = []

    # read Excel to table
    for i in range(0, row_num):
        row = []
        for j in dataframe1.iter_cols(1, dataframe1.max_column):
            row.append(j[i].value)
        table.append(row)
        del row

    # from matrix table into A and c
    count = 0  # to record the number of known data
    for i in range(row_num):
        for j in range(col_num):
            # 对所有的点都要查看，所以是在两个for的下面
            if table[i][j] != None:
                # 对A
                A_row[i] = 1
                A_row[41+j] = 1
                count = count+1
                # print(A_row)
                A.append(A_row)
                A_row = [0]*46  # recover the row vector

                # 对c
                C.append([table[i][j]-r]) #let vector C to be colume vector

            else:
                need = [i, 41+j] #record the missed postion
                needPredict.append(need)


    # solve the optimal b*
    A = np.array(A)
    C = np.array(C)
    # print(C)
    AT = A.T
    # print(AT)
    ATA = np.dot(AT, A)
    ATC = np.dot(AT, C)

    B = solve(ATA, ATC)

    # print out the predicted data 
    for cell in range(29):
        b1 = needPredict[cell][0]
        b2 = needPredict[cell][1]
        result = B[b1][0] + B[b2][0] + r
        # print("b1 = ", b1, "b2 = ", b2, "result = ", result)

    # CANNOT WRITE into this sheet, so I copy it into Excel manually

    # read another sheet to print out the rank list
    wb = openpyxl.load_workbook('Stall Revenue.xlsx')
    ws = wb["Netflix(v1)"]

    rank = ws['M']
    rank_list = []
    for x in range(0,len(rank)): 
        # print(rank[x].value) 
        rank_list.append(rank[x].value)
    # print(rank_list)

    new_list = np.argsort(rank_list).tolist()
    new_list = new_list[:-1]
    # print(new_list)

    return new_list

if __name__ == "__main__":
    revenue_list = revenue_rating()
    print(revenue_list)