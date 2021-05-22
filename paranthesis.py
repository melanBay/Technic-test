
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
