string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# x = 1
# my_list = []
# while x < 7:
#   my_list.append("string"+str(x))
#   x += 1
#
# new_list = []
# for my_var in my_list:
#   holder = vars().get(my_var)
#   new_list.append(holder)
#
# message = ''
# for x in new_list:
#   message = message + ''.join(x)
#
# print(message)

my_strings = []
for k, v in globals().copy().items():
    if k.startswith('string'):
        my_strings.append((k, v))

my_strings.sort()

print(''.join(i[1] for i in my_strings))

print(f"{string1}{string2}{string3}{string4}{string5}{string6}")
