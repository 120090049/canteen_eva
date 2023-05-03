import pandas as pd
import numpy as np
import os
# bys = [27, 28, 14, 32, 20, 21, 12, 26, 36, 2, 35, 41, 34, 43, 33, 7, 10, 39, 19, 13, 37,
#        45, 15, 38, 42, 25, 8, 17, 44, 3, 40, 6, 11, 24, 16, 23, 1, 4, 29, 22, 18, 31, 9, 30, 5]
# r = np.arange(45)
# for i in range(45):
#     r[i] += 1
# np.random.shuffle(r)
# page = np.arange(45)
# for i in range(45):
#     page[i] += 1
# np.random.shuffle(page)
# nlp = np.arange(45)
# for i in range(45):
#     nlp[i] += 1
# np.random.shuffle(nlp)
bys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nlp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
page = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if ( (len(bys) != len(r)) or (len(r) != len(nlp)) or (len(nlp) != len(page)) or (len(page) != len(bys)) ):
    raise ValueError("The length of the lists does not match")
    

total_weight = 100
remove_num = 8
# w1, w2, w3, w4 = 0
final_pair = {i: 0 for i in range(1, len(bys)+1)}

# 读取Excel文件
file_path = os.path.join('data', 'stall_want_to_remove.xlsx')
df = pd.read_excel(file_path)
rating_list = []

# 提取数据,form a dictionary
number = df.iloc[:, 2].tolist()
index = [i for i in range(1, len(bys)+1)]
for i in range(len(index)):
    rating_list.append([index[i], number[i]])
rating_list = sorted(rating_list, key=(lambda x: x[1]), reverse=True)

rating_dict = {}
for i in range(remove_num):
    rating_dict[rating_list[i][0]] = rating_list[i][1]

all_results = []
evaluation = 0

# print(rating_list)
# print(rating_dict)

for i in range(0, total_weight+1):  # for bayesian
    w1 = i
    for j in range(0, total_weight - i + 1):  # for revenue
        w2 = j
        for k in range(0, total_weight - i - j + 1):  # for page ranking
            w3 = k
            for z in range(total_weight - i - j - k, total_weight - i - j - k + 1):  # for nlp
                w4 = z
                for m in range(1, remove_num+1):  # add the borda count
                    final_pair[bys[-m]] += w1 * (remove_num + 1 - m)
                    final_pair[r[-m]] += w2 * (remove_num + 1 - m)
                    final_pair[page[-m]] += w3 * (remove_num + 1 - m)
                    final_pair[nlp[-m]] += w4 * (remove_num + 1 - m)
                # sort the final weight
                pairs = [[k, v] for k, v in final_pair.items()]
                pairs = sorted(pairs, key=(lambda x: x[1]), reverse=True)

                for t in range(remove_num):
                    # calculate the cost
                    if pairs[t][0] in rating_dict:
                        # print('yes')
                        evaluation += rating_dict[pairs[t][0]]
                all_results.append([w1, w2, w3, w4, evaluation])
                evaluation = 0

all_results = sorted(
    all_results, key=(lambda x: x[4]), reverse=True)
print(all_results[0])
