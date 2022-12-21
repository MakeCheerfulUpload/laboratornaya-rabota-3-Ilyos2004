import re
text = input()
sm = r"8<{\\"
result = re.findall(sm,text)
print(len(result))

