'''
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''
limit = 5
num_of_rows = limit * 2 -1
total=[]
for i in range (limit):
    if i == 0:
        total.append([limit]*num_of_rows)
    else:
        prev_row = total[i-1][:]
        total.append(prev_row)
        # print(id(total[i-1]), id(total[i]))
    total[i][0+i:num_of_rows-i]= [limit - i]*((num_of_rows-i)-(0+i))
# for i in total:
#     print(i)
# print()

remaining_part = total[:-1]
total = total + remaining_part[::-1] # vertical mirror image
for i in total:
    print(i)