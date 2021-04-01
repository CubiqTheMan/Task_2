s = input()
legalbrakets = ['(', '{', '[', '<']
braketstype = input()
for j in range(len(braketstype)):
    if braketstype[j] not in legalbrakets:
        print('Wrong brackets')
        quit()
def checkbrackets(s):
    counter = 0
    a = ()
    b = ()
    sopen = {1 : '(',2: '{',3: '[',4: '<'}
    sclose = {1:')', 2: '}', 3: ']', 4: '>'}
    for i in range(len(s)):
        stack = []
        if s[i] in sopen:
            #counter = counter + 1
            stack.append(s[i])
        elif s[i] in sclose:
            if stack[-1] == sclose.get(stack[-1]):
                #counter = counter - 1
                try:
                    stack.remove(s[i])
                except ValueError:
                    #a = (s[i], s.index(i))
                    print('can do that')
        if counter == 0:
                return True
        else:
                return False
print(checkbrackets(s))
