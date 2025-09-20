from typing import List
'''
Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.

Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

Constraints:

    1 <= tokens.length <= 1000.
    tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].



Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

'''
symbols ={
    '+' : lambda a, b: a+b,
    '-' : lambda a, b: a-b, 
    '*' : lambda a, b: a*b, 
    '/' : lambda a, b: int(float(a) / b)
    }


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for element in tokens:
        try:
            stack.append(int(element))
        except ValueError:
            b = stack.pop()
            a = stack.pop()
            result = symbols[element](a, b)
            print(result)
            stack.append(result)
    return stack.pop()



tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))
        