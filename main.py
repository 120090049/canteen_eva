from A_bayesian_ranking.bayesian_ranking import bayesian_ranking
from B_complaint_analysis.complaint_analysis import complaint_analysis
import pandas as pd
import os
import openpyxl


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data', 'stall_rating.xlsx')

    # 读取Excel文件
    table = openpyxl.load_workbook(file_path)
    table_sheet = table.active

    first_row = True
    
    stall_index_dict = {}
    stall_canteen_dict = {}
    for row_index in range(1,table_sheet.max_row+1):
        # 读取第一列和第二列的值
        canteen = table_sheet.cell(row_index, 1).value
        stall = table_sheet.cell(row_index, 2).value

        if (first_row):
            first_row = False
            continue
        else:
            stall_index_dict[stall] = row_index-1
            stall_canteen_dict[stall] = canteen
    
    # print(stall_dict)
    # stall_index_dict    {stall_name: index}
    # stall_canteen_dict  {stall_name: canteen}
    print(stall_index_dict)
    print(stall_canteen_dict)
    # list_A = bayesian_ranking()
    # list_B = complaint_analysis(first_row)
    # print(final_list)
