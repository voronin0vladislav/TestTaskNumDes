def brackets(s: str) -> bool:
    brackets = "()[]{}"
    opening = brackets[::2]
    closing = brackets[1::2]
    stack = []
    for character in s:
        if character in opening:
            stack.append(opening.index(character))
        elif character in closing:
            if stack and stack[-1] == closing.index(character):
                stack.pop()
            else:
                print('False')
                return False
    print(not stack)
    return (not stack)




#Пример 1
s = '()'
brackets(s)
#Пример 2
s = '()[]{}'
brackets(s)
#Пример 3
s = '(]'
brackets(s)
#Пример 4
s = '([)]'
brackets(s)
#Пример 5
s = '([])'
brackets(s)
#Пример 6
s = '[()'
brackets(s)
#Пример 7
s = '[)]'
brackets(s)