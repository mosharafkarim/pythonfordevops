import re

text = "The quick brown fox"
pattern = r"quick"

search = re.search(pattern,text)
if search:
    print("Search found:", search.group())
else:
    print("Search not found")