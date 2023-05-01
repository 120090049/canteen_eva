# import xlrd


# def open_excel(file='test1.xlsx'):  # 感觉最好用绝对路径，比相对路径更保险点
#     try:
#         data = xlrd.open_workbook(file)
#         return data
#     except Exception as e:
#         print(str(e))


# def excel_table_byname(file='test1.xlsx', colnameindex=0, by_name='Sheet1'):
#     data = open_excel(file)  # 打开excel文件
#     table = data.sheet_by_name(by_name)  # 根据sheet名字来获取excel
#     nrows = table.nrows  # 行数
#     colnames = table.row_values(colnameindex)  # 某一行数据
#     list = []  # 装读取结果的序列
#     for rownum in range(0, nrows):  # 遍历每一行的内容
#         row = table.row_values(rownum)  # 根据行号获取行
#         if row:  # 如果行存在
#             app = []  # 一行的内容
#             for i in range(len(colnames)):  # 一列列地读取行的内容
#                 app.append(row[i])
#             list.append(app)  # 装载数据
#     return list


# def main():
#     tables = excel_table_byname()
#     list_image = []
#     list_label = []
#     list_label_1 = []
#     for row in tables:
#         list_image.append(row[2])
#         for i in row[5:22]:
#             if i == "null":
#                 list_label_1.append(0)
#             else:
#                 list_label_1.append(1)
#         list_label.append(list_label_1)
#         list_label_1 = []

#     return list_image, list_label


# if __name__ == "__main__":
#     image, label = main()
#     print(image)
#     print(label)

import pandas as pd

# 读取Excel文件
df = pd.read_excel('new_bayesian_ranking.xlsx')

# 提取第1列数据
number = df.iloc[:, 2].tolist()
stall = df.iloc[:, 1].tolist()
canteen = df.iloc[:, 0].tolist()
grade = df.iloc[:, 3].tolist()

name = []
for i in range(len(stall)):
    name.append(canteen[i] + stall[i])

total_list = []
N = 0
NR = 0
for i in range(len(grade)):
    total_list.append([number[i], name[i], grade[i], i+1])
    N += number[i]
    NR += number[i] * grade[i]

bayesian_rank_list = []
for i in range(len(total_list)):
    br = (NR + number[i] * grade[i]) / (N + number[i])
    bayesian_rank_list.append([i+1, name[i], br])

bayasian2 = sorted(bayesian_rank_list, key=(lambda x: x[2]), reverse=True)

final_list = []
for i in range(len(bayasian2)):
    final_list.append([bayasian2[i][0], bayasian2[i][1], i+1])

output_list = []
for i in range(len(final_list)):
    output_list.append(final_list[i][0])

# 打印第1列数据
# print(number)
# print(name)
# print(grade)
# print(total_list)
# print(N)
# print(NR)
# print(bayesian_rank_list)
# print(bayasian2)
# print(final_list)
print(output_list)
