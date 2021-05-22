
# Problem

# The nested brackets problem is a problem that determines if a sequence of

# brackets are properly nested.  A sequence of brackets s is considered properly nested

# if any of the following conditions are true:

# - S is empty

# - S has the form (U) or [U] or {U} where U is a properly nested string

# - S has the form VW where V and W are properly nested strings

# For example, the string "( )( )[ ( ) ]" is properly nested but "[ ( ( ) ]" is not.

# The function called isBalanced takes as input a string which is a sequence of brackets and

# returns true if input is nested and false otherwise.



"""
The idea of this algorithm is constructed a list contains the following symbols ( '(,[,{' )
after any change of symbols check if you find a correct pair.
If the pair is correct then remove open symbols corresponding.
Did it so on.
If the symbol list is empty, the parantheses are balanced otherwise isn't
"""


def solution(A):
    stack = []
    for i,char in enumerate(A):
        if char in ('(', '[', '{'):
            stack.append(char)
        else:
            if len(stack)>0:
                pair = stack[len(stack)- 1] + char
                if pair not in ("[]", "()", "{}"):
                    return 0
                else:
                    stack.pop()
            else:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
