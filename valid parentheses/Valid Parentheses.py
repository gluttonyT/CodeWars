#TESTS
"""
Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)
"""



def valid_parentheses(string):
    input = string

    #get all the parentheses out of string and save it to a list
    list = []
    for char in input:
        if char == '(' or char == ')':
            list.append(char)
    #if there is no parentheses at all, return true
    if not len(list):
        return True
    #if list has odd number of elements, obviously parentheses is
    # not balanced
    if not len(list) % 2 == 0:
        return False
    #start popping inner pairs and quit if len(list) is 0
    # check if you can pop out '()' pairs
    found = '()' in ''.join(list)
    if found:
        while '()' in ''.join(list):
            pop_index = ''.join(list).find('()')
            list.pop(pop_index)
            list.pop(pop_index)
    # if there are unpopped parentheses pair, then len(list)>0 with unmatched
    #parentheses pair
    if len(list):
        return False
    else:
        return True


valid_parentheses("vinb(jhjpv(gp(fqfghfas)ujfja)r(ntznaif)k")
"""
best pratice solution:
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
"""
print("look up for better solution")