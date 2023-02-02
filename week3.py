#Week3

def biggest(a ,b, c, d):
    biggest = 0
    if a>=b and a>=c and a>=d:
        biggest = a
    if b>=a and b>=c and b>=d:
        biggest = b
    if c>=a and c>=b and c>=d:
        biggest = c
    else:
        biggest = d
    return biggest
