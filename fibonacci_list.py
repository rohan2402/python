a=0
b=2
fib=[a,b]
while b<100:
    a, b=b, a+b
    fib.append(b)
print (fib)    
