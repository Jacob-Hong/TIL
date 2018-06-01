import re
s = "fast campus datascience fighting. \
datascience fighting. 1234 fast campus fighting"


# match
a = re.match(pattern="fast" , string=s)
print(a)

# search
b = re.search("campus", s)
print(b)
