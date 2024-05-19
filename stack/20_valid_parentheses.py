# def isValid(s):
#     stack = []
#     closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

#     for c in s:
#         if c in closeToOpen:
#             if stack and stack[-1] == closeToOpen[c]:
#                 stack.pop()
#             else: return False
#         else:
#             stack.append(c)
#             print(f'else append {stack}')
        
#     print(stack)
#     print(True if not stack else False)

# s = "()[]{}"

# isValid(s)

s = "()[]{}"
closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

for c in s:
    if c in closeToOpen:
        print(f'{c} is in closeToOpen')
    else:
        print(f'{c} is not in closeToOpen')

for k in closeToOpen:
    print(k)
