# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.

# Any right parenthesis ')' must have a corresponding left parenthesis '('.

# Left parenthesis '(' must go before the corresponding right parenthesis ')'.

# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.

# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True
# Note:
# The string size will be in the range [1, 100].


def checkValidString(s) -> bool:
    stack = []
    stars = []

    for idx, i in enumerate(s):
        # if i is (, add it's index to the stack
        if i == '(':
            stack.append(idx)
            continue

        # if i is *, add it's index to the star stack
        if i == '*':
            stars.append(idx)
            continue

        # else if i is ) and both stacks are empty, return false
        # because it is not balanced
        else:
            if len(stack) == 0 and len(stars) == 0:
                return False

            # else if the there is stars or ), the pop accordingly
            else:
                if len(stack) > 0:
                    stack.pop()
                elif len(stars) > 0:
                    stars.pop()

    # if at the end of the for loop, both stacks have elements in them
    # loop over both and compare the indices
    # stars will be used to rep the ')'
    while len(stars) > 0 and len(stack) > 0:
        # ')' comes before '(', return false because it is not balanced
        if stars.pop() < stack.pop():
            return False

    # if after popping of in the while loop above stack isn't empty
    # return false
    if len(stack) > 0:
        return False

    # else return true
    return True


print(checkValidString("(*))"))
