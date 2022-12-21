import re
email = input()
rex = r"@([a-z0-9._-]+\.+[a-z]{1,})"
a = re.findall(rex, email)
if a:
    print(a)
else:
    print("Fail!") 
##q@q.a.b
