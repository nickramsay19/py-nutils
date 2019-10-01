from nutils import map2range, float_range


print(map2range(5,0,10,0,255))
print(str(list((lambda x : 2 * x)(i) for i in float_range(1))))
