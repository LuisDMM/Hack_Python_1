"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = []
    number= 0,1,2,3,4,5
    result = list(number)
    return result

r = fn_hack_6()

print(r)