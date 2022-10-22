src = not False and True or False and not True

# True and True or False and False  # избавились от not
# True or False  # избавились от and
# True  # избавились от or

result = True

print(src == result)
