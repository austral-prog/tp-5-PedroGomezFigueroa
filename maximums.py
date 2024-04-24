def max_of_two(x, y):
    
    if (x>y):
        return(x)
    else:
        return(y)
    
print (max_of_two(1,2))

def max_of_three(x, y, z):

    if (x>y)and(x>z):
        return(z)
    elif(y>x)and(y>z):
        return(y)
    else:
        return(z)

print (max_of_three(5,6,7))
