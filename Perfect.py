def perfect_numbers(limit):
    my_list=[]
    limit=1000
    for i in range (1,limit):
        divisor_sum=0
        for j in range(1,i):
            if 1%j==0:
                divisor_sum+=j
                if divisor_sum==i:
                    my_list.append(i)
    return my_list
print(f"perfect numbers are:{perfect_numbers (list)}"                    
        
        