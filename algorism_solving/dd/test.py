list = [5, 1, 2, 3, 4, 5, 4]
res_list = [i for i, value in enumerate(list) if value == max(list)]
print(res_list)