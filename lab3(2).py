import re
text = input()
a = r"\w+\s[А-ЯЁИа-яёи]{1}\.[А-ЯЁа-яё]{1}"
print(sorted(map(lambda x: x.split()[0], re.findall(a,text))))
