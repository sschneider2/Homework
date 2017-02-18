import requests
import re
import random

# Get the text for the constitution
bilingual = open ('D23_3_LE_music.txt').read()
#print bilingual

# A useful construct I'm leaving in, commented out
# constitution_lines = constitution_text.split('\n')
# for line in constitution_lines:
# 	print "-->",line

# Define the regular expression and use it to find matches
regex = r"([yY]es|[Nn]o)\s+(\w)"
matches = re.findall(regex, bilingual)

# Do something with the matches
for match in matches:
	print "-->", match[0], "was followed by", match[1]


### With this code I opened one of my conversational text files
### from my first year project, found any instances of the
### words 'yes' or 'no', using both the capitalized and
### lowercase versions of the word. I am also given the following
### word after 'yes' or 'no', which in each case was actually the
### word 'I'.