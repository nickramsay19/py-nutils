from nutils import map2range, float_range


for x in float_range(3, 0, 1): # precision of 3 decimal places, 0-1
    print(x)

print(map2range(5,0,10,0,255))
print(str(list((lambda x : 2 * x)(i) for i in float_range(1))))
