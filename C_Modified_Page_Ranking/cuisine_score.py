import openpyxl
import numpy as np
# from numpy.linalg import *
from numpy.linalg import eig


# read the excel and form a table
# Define variable to load the dataframe
def cuisine_score():
    dataframe = openpyxl.load_workbook("matrixH.xlsx")

    # Define variable to read sheet
    dataframe1 = dataframe.active

        # store the raw data
    table = []
    row_num = dataframe1.max_row
    col_num = dataframe1.max_column

    # read Excel to table
    for i in range(0, row_num):
        row = []
        for j in dataframe1.iter_cols(1, dataframe1.max_column):
            row.append(j[i].value)
        table.append(row)
        del row


    # use table to form H matrix
    H = []


    for i in range(row_num):
        H_row = []
        total = table[i][-1]
        # print(total)
        for j in range(col_num-1):
            H_row.append(0.9*(table[i][j]/total))
        H.append(H_row)
        del H_row

    I = [[1/450]*45]*45
    I = np.array(I)

    # print(I)
    H_hat =H + I

    # pi
    pi = [0.5,0,0,0,0,  0,0,0,0,0,
        0,0,0,0,0  ,0,0,0,0,0,
        0,0,0,0,0  ,0,0,0,0,0,
        0,0,0,0,0  ,0,0,0,0,0,
        0,0,0,0,0.5]

    # iteration 
    for i in range(100):
        pi = np.dot(pi, H_hat)
        # print('k= ', i+1, ' :', pi)


    sum=0
    for i in range(45):
        sum = sum+pi[i]
        element = pi[i]
        # pi[i] = 1-element
        
    sorted_indexes = np.argsort(pi).tolist()
    for i in range(45):
        element = sorted_indexes[i]
        sorted_indexes[i] = element+1

    # print("sum = ", sum)
    # print(pi)
    # print(new_list)
    index_score = [0 for i in range(len(sorted_indexes))]
    for i in range(len(sorted_indexes)):
        score = len(sorted_indexes) - i -1
        index_score[sorted_indexes[i]-1] = score
    
    return index_score

# *************************** PS *************************
# 直接用所有的来形成matrix，现在结果中有0存在，这不符合之前的设定
# 有尝试过加上thelta，结果比较接近，差异较小

if __name__ == "__main__":
    similarity_list = cuisine_score()
    print(similarity_list)