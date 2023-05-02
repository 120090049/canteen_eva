import os
import pandas as pd

# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# 构造文件的相对路径
file_path = os.path.join(parent_dir, 'data', 'stall_rating.xlsx')

# 读取Excel文件
df = pd.read_excel(file_path)

# # 打印前5行
print(df.head())
