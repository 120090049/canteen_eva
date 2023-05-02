import pandas as pd
import openpyxl
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'data', 'complaint_score.xlsx')

def complaint_analysis(stall_index_dict, stall_canteen_dict):

    table = openpyxl.load_workbook(file_path).active
    stall_score_list = [5] * 45
    first_row = True
    for row_index in range(1,table.max_row+1):  
        if (first_row):
            first_row = False
            continue
        else:
            canteen = table.cell(row_index, 1).value
            stall = table.cell(row_index, 2).value
            score = table.cell(row_index, 5).value
            
            stall_index = stall_index_dict(stall)
            break

    return stall_score_list

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    file_path = os.path.join(parent_dir, 'data', 'stall_rating.xlsx')

    # 读取Excel文件
    table = openpyxl.load_workbook(file_path)
    table_sheet = table.active

    first_row = True
    
    stall_index_dict = {} # {stall_name: index}
    stall_canteen_dict = {} #  {stall_name: canteen}
    for row_index in range(1,table_sheet.max_row+1):
        # 读取第一列和第二列的值
        canteen = table_sheet.cell(row_index, 1).value
        stall = table_sheet.cell(row_index, 2).value
        score = table_sheet.cell(row_index, 5).value

        if (first_row):
            first_row = False
            continue
        else:
            stall_index_dict[stall] = row_index-1
            stall_canteen_dict[stall] = canteen
            
            
    final_list = complaint_analysis(stall_index_dict, stall_canteen_dict)
    print(final_list)
