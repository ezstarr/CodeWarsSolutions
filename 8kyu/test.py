#ex_string = "this is a test string"

#for i, ex in ex_string:
   # print(ex_string[i])

days = {'Mon', 'Tue', 'Wed', 'Thu'}
enum_days = enumerate(days)
print(type(enum_days))


# converting it to alist
print(list(enum_days))

# changing the default counter to 5
enum_days = enumerate(days, 5)
print(list(enum_days))
