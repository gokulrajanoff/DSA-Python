#R-1.1 is_multiple(n,m)
def is_multiple(n,m):
    if( m % n == 0 ):
        return True
    return False; 

print('is_multiple(2,6) answer',is_multiple(2,6))
print('is_multiple(2,5) answer',is_multiple(2,5))

#----------------------------------------------------------
#R-1.2 is_even(k)
# normal way

def is_even(k):
    if(k % 2 == 0):
        return True
    return False

print('is_even',is_even(6))

# without using math operation
def is_even_StringWay(k):
    k = str(k)
    if(k[-1] in ('0','2','4','6','8')):
        return True
    return False

print('is_even_Tricky',is_even_StringWay(68))
print('is_even_Tricky',is_even_StringWay(55))

# without using bit operation
def is_even_BitWay(k):
    return ((k & 1) == 0) if 'even' else 'odd';

print('is_even_BitWay',is_even_BitWay(68))
print('is_even_BitWay',is_even_BitWay(55))

#-----------------------------------------------------------
