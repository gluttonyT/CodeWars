#TESTS
"""
Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)
"""




#the function
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
    while len(list):
        
        # check if you can pop out '()' pairs
        found = '()' in ''.join(list)
        if found:
            while found:
                pop_index = ''.join(list).find('()')
                list.pop(pop_index)
                list.pop(pop_index)

    if len(list):
        return False
    else:
        return True

valid_parentheses("vinb(jhjpv(gp(fqfghfas)ujfja)r(ntznaif)k")