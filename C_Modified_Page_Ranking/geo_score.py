dict1 = {
    1: '开饭了', 2: '包子铺', 3: '三两粉', 4: '扒餐', 5: '韩式拌饭', 6: '粤式烧腊', 7: '重庆小面', 8: '麻辣香锅', 9: '黄焖水煮', 10: '锅盔', 11: '兰州拉面', 12: '书亦烧仙草', 13: '小小花果山', 14: '烤盘饭', 15: '牛肉饭', 16: '轻食沙拉', 17: '米线', 18: '小碗菜', 19:
    '自选', 20: '牛腩粉面', 21: '烧腊', 22: '麻辣烫、香锅', 23: '水吧、甜品', 24: '猪肚鸡', 25: '紫金八刀汤粉', 26: '红荔村肠粉', 27: '包点', 28: '面档', 29: '小碗菜', 30: '水饺', 31: '自选', 32: '烧腊', 33: '粉面', 34: '拌饭', 35: '铁板', 36: '水吧', 37: '水吧', 38:
    '面包', 39: '沙拉', 40: '小火锅', 41: '炸鸡', 42: '粉面', 43: '扒餐', 44: '小碗菜', 45: '东南亚菜'
}


dict2 = {
    1: '学一食堂', 2: '学一食堂', 3: '学一食堂', 4: '学一食堂', 5: '学一食堂', 6: '学一食堂', 7: '学一食堂',
    8: '学一食堂', 9: '学一食堂', 10: '学一食堂', 11: '学一食堂', 12: '学一食堂', 13: '学一食堂', 14: '学一食堂',
    15: '学一食堂', 16: '学一食堂', 17: '学一食堂', 18: '学二食堂', 19: '学二食堂', 20: '学二食堂',
    21: '学二食堂', 22: '学二食堂', 23: '学二食堂', 24: '学二食堂', 25: '学二食堂', 26: '学二食堂', 27: '逸夫',
    28: '逸夫', 29: '逸夫', 30: '逸夫', 31: '思廷', 32: '思廷', 33: '思廷', 34: '思廷', 35: '思廷', 36: '思廷',
    37: '香波', 38: '香波', 39: '香波', 40: '香波', 41: '香波', 42: '香波', 43: '香波', 44: '香波', 45: '香波'
}


# geo_dict = {'学一食堂': '下园', '学二食堂': '下园', '逸夫': '下园', '思廷': '上园', '香波': '上园'}


def geo_score(dict_stall, dict_canteen):
    #记得别算已取消的
    dict_score = {
        '学一食堂': 1.987,#0
        '学二食堂': 2.066,#1
        '逸夫': 2.316,#2
        '思廷': 2.500,#4
        '香波': 2.421#3
    }

    length = len(dict_stall)
    if len(dict_stall) == len(dict_canteen):
        list_score = [''] * length
        for key, val in dict_canteen.items():
            list_score[key-1] = dict_score[val]
        rank_list4 = list()
        count = 0
        while count < length:
            
            rank_list4.append(list_score.index(max(list_score))+1)
            list_score[list_score.index(max(list_score))] = 0
            count +=1
        

        return rank_list4
    else:
        print('data error')
        return


# print(geo_score(dict1, dict2))