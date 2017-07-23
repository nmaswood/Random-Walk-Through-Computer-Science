res = filter(lambda x: x != 1, [1,2,3,4])

res = list(res)

print (res)

def memory_range(x):
    i = 0
    while i < x:
        yield i 
        print ("next iteration!")
        i = i + 1

fuck = list(foo(10))
print (fuck)



