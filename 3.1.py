
def Lower(s):
    r=''
    for i in s:
        if 'A'<=i<='Z':
            r+=chr(ord(i)+32)
        else:
            r+=i
    return r

def Upper(s):
    r=''
    for i in s:
        if 'a'<=i<='z':
            r+=chr(ord(i)-32)
        else:
            r+=i
    return r

def Toggle(s):
    r=''
    for i in s:
        if 'A'<=i<='Z':
            r+=chr(ord(i)+32)
        elif 'a'<=i<='z':
            r+=chr(ord(i)-32)
        else:
            r+=i
    return r


s=str(input('enter a string: '))
print(Lower(s))
print(Upper(s))
print(Toggle(s))
