def revers(s):
    return s[::-1]
def palindrom(s):
    res=revers(s)
    if (s == res):
        return True
    return False
s=input("enter charater");
ans=palindrom(s)
if ans==1:
    print('yes')
else:
    print('no')