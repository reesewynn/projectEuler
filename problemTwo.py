def fib(n2, n1, my_max, my_sum):
    if(n1 > my_max): 
        return my_sum
    elif(n1 <= my_max and not (n1 % 2)):
        my_sum += n1
    return fib(n1, n1 + n2, my_max, my_sum)
    
print(fib(1, 2, 4000000, 0)) 
