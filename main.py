from A_bayesian_ranking.bayesian_ranking import bayesian_ranking
from B_complaint_analysis.complaint_analysis import complaint_analysis
import pandas as pd
import os
import openpyxl


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data', 'stall_canteen_campus.xlsx')

    # 读取Excel文件
    table = openpyxl.load_workbook(file_path)
    table_sheet = table.active

    first_row = True
    
    stall_dict = {} # {stall_name: index}
    canteen_dict = {} #  {stall_name: canteen}
    campus_dict = {}
    for row_index in range(1,table_sheet.max_row+1):
        # 读取第一列和第二列的值
        canteen = table_sheet.cell(row_index, 1).value
        stall = table_sheet.cell(row_index, 2).value
        campus = table_sheet.cell(row_index, 3).value

        if (first_row):
            first_row = False
            continue
        else:
            stall_dict[int(row_index)-1] = stall
            canteen_dict[int(row_index)-1] = canteen
            campus_dict[canteen] = campus
            
    
    print(stall_dict)
    print()
    print(canteen_dict)
    print()
    print(campus_dict) # 食堂-上下园

    # list_A = bayesian_ranking()
    list_B = complaint_analysis(stall_dict, canteen_dict)
    # print(list_A)
    print(list_B)

# [27, 28, 14, 32, 20, 21, 12, 26, 36, 2, 35, 41, 34, 43, 33, 7, 10, 39, 19, 13, 37, 45, 15, 38, 42, 25, 8, 17, 44, 3, 40, 6, 11, 24, 16, 23, 1, 4, 29, 22, 18, 31, 9, 30, 5]
# [2, 3, 4, 5, 8, 10, 13, 14, 15, 16, 37, 38, 39, 40, 41, 42, 17, 12, 6, 9, 7, 20, 23, 24, 25, 26, 34, 36, 11, 45, 35, 43, 28, 22, 21, 1, 32, 44, 33, 30, 18, 19, 31, 27, 29]