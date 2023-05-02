import pandas as pd
import openpyxl
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'data', 'complaint_score.xlsx')

def complaint_analysis():

    table = openpyxl.load_workbook(file_path).active
    
    for row_index in range(1,table.max_row+1):
        
        canteen = table.cell(row_index, 1).value
        stall = table.cell(row_index, 2).value
        score = table.cell(row_index, 5).value
        
        if (first_row):
            first_row = False
            continue
        else:
            # 预测得分
        

    
    return output_list

if __name__ == "__main__":
    final_list = complaint_analysis()
    print(final_list)
