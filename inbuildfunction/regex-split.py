import re

text = "apple,banana,orange,grape"
pattern = r","

split_result=re.split(pattern,text)
print("After split by pattern", split_result)