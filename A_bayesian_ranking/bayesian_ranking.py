import pandas as pd
import os


def ori2borda(original_score):
    sorted_score = sorted(original_score)  # 按升序排序 [2, 3, 3, 4, 5, 6, 6, 6]
    result = [0 for i in range(len(original_score))]

    for i in range(len(original_score)):
        result[i] = sorted_score.index(original_score[i]) 
    # print(result) # [4, 0, 1, 1, 3, 5, 5, 5]  8个
    count_dict = {}
    for num in result:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    index_repeated = [key for key, value in count_dict.items() if value != 1] 

    new_dict = {} # {1: 2, 5: 3} ==> {1:1.5, 5:6}
    for i in index_repeated:
        # 1 有 2 个 == i 有 times 个   1+2+3
        times = count_dict[i] 
        value = i + 0.5*(times-1)
        new_dict[i] = value        
    # number_index_repeated = 

    for i in range(len(result)):
        if result[i] in new_dict:
            result[i] = new_dict[result[i]]
            
    return result

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
        bayesian_rank_list.append(br)
    
    return bayesian_rank_list

if __name__ == "__main__":
    
    final_list = bayesian_ranking()
    # print(ori2borda( final_list) )
