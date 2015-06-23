# -*- coding: utf-8 -*-
#我自己的写法
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for x in range(5):
    if isinstance(L1[x],str):
        L2.append(L1[x])
print([s.lower() for s in L2])
#最简单的写法
#是生成公式的算式，for中的S是前面的带入变量，if则提供了判断对象，通过不停的判断，赋值给前面的S，从而达到目的
print([s.lower() for s in L1 if isinstance(s,str) ])