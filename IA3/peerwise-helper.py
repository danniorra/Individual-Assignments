# The package 'random' is used in this code

import random
#Page ranges
# 113 - 155
# 208 - 216
# 1 - 2

# Defining the page numbers
pages = [1, 2, *range(113,155), *range(208,216)]

# Asking for no. of questions
qs = int(input('How many pages? '))

# Generating the specified amount of random pages
for i in range(0,qs):
    ind = random.randint(0,len(pages)-1)
    print(pages[ind])
    pages.pop(ind)