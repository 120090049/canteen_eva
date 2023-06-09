import pandas as pd
import numpy as np
import os
# bys = [27, 28, 14, 32, 20, 21, 12, 26, 36, 2, 35, 41, 34, 43, 33, 7, 10, 39, 19, 13, 37,
#        45, 15, 38, 42, 25, 8, 17, 44, 3, 40, 6, 11, 24, 16, 23, 1, 4, 29, 22, 18, 31, 9, 30, 5]


def infer(lists, para, remove_num):
    [list1, list2, list3, list4, list5] = lists
    [w1, w2, w3, w4, w5] = para
    final_pair = {i: 0 for i in range(1, len(list1)+1)}
    for m in range(1, 1+len(list1)):
        final_pair[m] += w1 * list1[m-1]
        final_pair[m] += w2 * list2[m-1]
        final_pair[m] += w3 * list3[m-1]
        final_pair[m] += w4 * list4[m-1]
        final_pair[m] += w5 * list5[m-1]
    pairs = [[k, v] for k, v in final_pair.items()]
    pairs = sorted(pairs, key=(lambda x: x[1]))  # 分数低在前面
    rank = []
    for i in range(len(pairs)):
        rank.append(pairs[i][0])
    # print(rank)

    # evaluation
    file_path = os.path.join('data', 'stall_like_dislike.xlsx')
    df = pd.read_excel(file_path)
    rating_list = []
    like_list = []
    # 提取数据,form a dictionary
    number = df.iloc[:, 2].tolist()
    index = [i for i in range(1, len(list1)+1)]
    for i in range(len(index)):
        rating_list.append([index[i], number[i]])
    rating_list = sorted(rating_list, key=(lambda x: x[1]), reverse=True)

    rating_dict = {}
    for i in range(remove_num):
        rating_dict[rating_list[i][0]] = rating_list[i][1]

    # 最喜欢的dic
    number2 = df.iloc[:, 3].tolist()
    index2 = [i for i in range(1, len(list1)+1)]
    for i in range(len(index)):
        like_list.append([index2[i], number2[i]])
    like_list = sorted(like_list, key=(lambda x: x[1]), reverse=True)

    like_dict = {}
    for i in range(remove_num):
        like_dict[like_list[i][0]] = like_list[i][1]

    # print(like_dict)

    removes = []
    evaluation = 0

    # 计算cost
    for t in range(remove_num):
        # mark the removed stalls
        removes.append(pairs[t][0])
        # calculate the cost
        if pairs[t][0] in rating_dict:
            # print('yes')
            evaluation += rating_dict[pairs[t][0]]
        if pairs[t][0] in like_dict:
            evaluation -= like_dict[pairs[t][0]]

    # print(evaluation)
    return rank, evaluation


def borda(remove_percent, lists):
    [bys, r,  page_sim, nlp, page_pos] = lists
    if ((len(bys) != len(r)) or (len(r) != len(nlp)) or (len(nlp) != len(page_sim)) or (len(page_sim) != len(bys))):
        raise ValueError("The length of the lists does not match")

    remove_num = int(remove_percent*len(bys))

    total_weight = 100
    # w1, w2, w3, w4 = 0
    final_pair = {i: 0 for i in range(1, len(bys)+1)}

    # 读取Excel文件
    file_path = os.path.join('data', 'stall_like_dislike.xlsx')
    df = pd.read_excel(file_path)
    rating_list = []
    like_list = []

    # 提取数据,form a dictionary
    number = df.iloc[:, 2].tolist()
    index = [i for i in range(1, len(bys)+1)]
    for i in range(len(index)):
        rating_list.append([index[i], number[i]])
    rating_list = sorted(rating_list, key=(lambda x: x[1]), reverse=True)

    rating_dict = {}
    for i in range(remove_num):
        rating_dict[rating_list[i][0]] = rating_list[i][1]

    # 最喜欢的dic
    number2 = df.iloc[:, 3].tolist()
    index2 = [i for i in range(1, len(bys)+1)]
    for i in range(len(index)):
        like_list.append([index2[i], number2[i]])
    like_list = sorted(like_list, key=(lambda x: x[1]), reverse=True)

    like_dict = {}
    for i in range(remove_num):
        like_dict[like_list[i][0]] = like_list[i][1]
    # print(like_dict)
    all_results = []
    evaluation = 0
    removes = []

    for i in range(0, total_weight+1):  # for bayesian
        w1 = i
        for j in range(0, total_weight - i + 1):  # for revenue
            w2 = j
            for k in range(0, total_weight - i - j + 1):  # for page ranking similarity
                w3 = k
                for z in range(0, total_weight - i - j - k + 1):  # for nlp
                    w4 = z
                    w5 = total_weight - i - j - k - z  # for page ranking position
                    # 找到组合以后开始操作
                    # add the borda count，key的index,value是分值
                    for m in range(1, 1 + len(bys)):
                        final_pair[m] += w1 * bys[m-1]
                        final_pair[m] += w2 * r[m-1]
                        final_pair[m] += w3 * page_sim[m-1]
                        final_pair[m] += w4 * nlp[m-1]
                        final_pair[m] += w5 * page_pos[m-1]
                    # sort the final weight，转成list
                    pairs = [[k, v] for k, v in final_pair.items()]
                    # 从低到高，排序每一对
                    pairs = sorted(pairs, key=(lambda x: x[1]))

                    # 计算cost
                    for t in range(remove_num):
                        # mark the removed stalls
                        removes.append(pairs[t][0])
                        # calculate the cost
                        if pairs[t][0] in rating_dict:
                            evaluation += rating_dict[pairs[t][0]]
                        if pairs[t][0] in like_dict:
                            evaluation -= like_dict[pairs[t][0]]
                    # 记录下每一次
                    all_results.append(
                        [w1, w2, w3, w4, w5, evaluation, removes])
                    # 每一次的cost，evaluation清零
                    evaluation = 0
                    final_pair = {i: 0 for i in range(1, len(bys)+1)}
                    removes = []

    all_results = sorted(
        all_results, key=(lambda x: x[5]), reverse=True)
    print(all_results[0])
    return all_results[0]


if __name__ == "__main__":
    bys = [27, 28, 14, 32, 20, 21, 12, 26, 36, 2, 35, 41, 34, 43, 33, 7, 10, 39, 19, 13, 37,
           45, 15, 38, 42, 25, 8, 17, 44, 3, 40, 6, 11, 24, 16, 23, 1, 4, 29, 22, 18, 31, 9, 30, 5]
    nlp = [2, 3, 4, 5, 8, 10, 13, 14, 15, 16, 37, 38, 39, 40, 41, 42, 17, 12, 6, 9, 7, 20, 23,
           24, 25, 26, 34, 36, 11, 45, 35, 43, 28, 22, 21, 1, 32, 44, 33, 30, 18, 19, 31, 27, 29]
    r = np.arange(45)
    for i in range(45):
        r[i] += 1
    np.random.shuffle(r)
    page_sim = np.arange(45)
    for i in range(45):
        page_sim[i] += 1
    np.random.shuffle(page_sim)
    page_pos = np.arange(45)
    for i in range(45):
        page_pos[i] += 1
    np.random.shuffle(page_pos)
    # bys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # nlp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # page_sim = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # page_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # borda(bys, r, nlp, page_sim, page_pos)
    print(infer([bys, r, nlp, page_sim, page_pos], [100, 0, 0, 0, 0], 4))
