import random
# ar = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
#
# for nr in ar:
#     if not (ar.count(nr) % 2 == 0):
#         print(nr)
#         break
#
# high_and_low = "15 -2 3 -4 5"
#
# vals = high_and_low.split(" ")
# print(type(vals))
# hoch = int(vals[0])
# niedrig = int(vals[0])
# print(type(niedrig))
# for nr in vals:
#     if int(nr) > hoch:
#         hoch = int(nr)
#     if int(nr) < niedrig:
#         niedrig = int(nr)
# print(hoch, niedrig)
# print (type (str(hoch)))
# print(type(hoch))
#
#
# n = map(int, high_and_low.split(' '))
# print(list(n))
# print( str(max(n)) + ' ' + str(min(n)) )
#
# a = [0,0,0]
# b = a.copy()
# b[0] = 1
#
# print(a)
# print(b)

game1 = ['x', 'x', 'x', 'x', 'x', 'x', 'o', 'o', 'o']
game2 = ['x', 'o', 'x', 'x', 'x', 'x', 'o', 'o', 'o']
game3 = ['x', 'x', 'x', 'x', 'x', 'x', 'o', 'o', 'o']

gamelist = []
gamelist.append(game1)

if game2 not in gamelist:
    gamelist.append(game2)

if game3 not in gamelist:
    gamelist.append(game3)

for game in gamelist:
    print(game)