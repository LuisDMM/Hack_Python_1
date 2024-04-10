"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    number = 5,4,3,2,1,0
    result = list(number)
    return result  

r = fn_hack_7()

print(r)