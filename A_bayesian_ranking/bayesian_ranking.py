import pandas as pd
import os

def bayesian_ranking():
    # 获取当前文件所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)

    # 构造文件的相对路径
    file_path = os.path.join(parent_dir, 'data', 'stall_rating.xlsx')

    # 读取Excel文件
    df = pd.read_excel(file_path)

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

    sorted_indexes = []
    for i in range(len(final_list)):
        sorted_indexes.append(final_list[i][0])
    
    index_score = [0 for i in range(len(sorted_indexes))]
    for i in range(len(sorted_indexes)):
        score = len(sorted_indexes) - i -1
        index_score[sorted_indexes[i]-1] = score
    
    return index_score

if __name__ == "__main__":
    final_list = bayesian_ranking()
    print(final_list)
