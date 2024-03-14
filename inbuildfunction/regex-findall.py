import re

text = "This is regex expression"

pattern = r"regex"

search = re.search(pattern,text)

if search :
    print("Pattern found", search.group())
else:
    print("Pattern not found")