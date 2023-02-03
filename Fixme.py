#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    x = range(n + 1)

    def helper(n):
        if (n % 2) == 0:
            return True
        return False
    answer = filter(helper, x)
    answer = list(answer)
    return answer
