# from time import time
#
# a = list(range(10000000))
# b = set(range(10000000))
# c = tuple(range(10000000))
#
# d = 9500000
#
# t = time()
# if d in a:
#     pass
# ta = time() -t
#
# t = time()
# if d in b:
#     pass
# tb = time() -t
#
# t = time()
# if d in c:
#     pass
# tc = time() -t
#
# print(ta,tb,tc)


def app(a):
    in_l = a
    in_l.append('end')
    return in_l

ls = ['beg', 'mid']
ls2 = app(ls)

print(ls, ls2)