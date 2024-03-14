import re

text = "This is regex expression"

pattern = r"regex"

new_text="replaced regex"

output=re.sub(pattern, new_text, text)

print("Modified text", output)