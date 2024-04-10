"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    input_list = [1,2,3]
    character_to_insert = "@"

    result = [item for sublist in [[x, character_to_insert] for x in input_list] for item in sublist]

    return result

r = fn_hack_9()

print(r)