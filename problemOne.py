def findSum(n):
    threes, fives, my_sum = 3, 5, 0
    while(threes < n or fives < n):
        if(threes < n): 
            my_sum += threes
        if(fives < n and fives % 3): 
            my_sum += fives
        threes += 3
        fives += 5
    return my_sum
    
print(findSum(1000))

