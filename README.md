# py-nutils
> Created by Nicholas Ramsay


## Map to Range (map2range)
```python
print(map2range(5,0,10,0,255))

# > 127.5
```

## Float Range (float_range)

```python

for x in float_range(3, 0, 1): # precision of 3 decimal places, 0-1
	print(x)

# --> 0.001
# --> 0.002
# ...
# --> 0.999

```

```python
print(str(list((lambda x : 2 * x)(i) for i in float_range(1))))

# > [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]

```
