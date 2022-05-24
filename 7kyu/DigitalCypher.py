"""Digital Cypher assigns to each letter of the alphabet unique number.
 For example:
 """
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encoded = {}

def encode(message, key=0):
    str_key = str(key)
    output = []
    for l in alphabet:
        encoded[l] = alphabet.index(l)+1

    for index, i in enumerate(message):
        i_value = encoded.get(i)
        # Each interation loops through the index
        # Grabs number assigned to index.
        # For example str_key[0] = 1
        i_value += int(str_key[index % len(str_key)])
        output.append(i_value)
    print(output)
# save all the values into a list.
encode("scout", 1939)

    # for index, i in enumerate(message):
    #     value = encoded.get(i)
    #     print(f"1 - {value}")
    #     value += int(str_key[str_key_index])
    #     str_key_index += 1
    #     if len(str_key) <= str_key_index:
    #         str_key_index = 0
    #     print(f"2 - {value}")

# "remainder of the index divided by len(str_key)"
# key = 123
# # if the i % 1, then
#
# encode("scout", 123)
# 3 % 3
# index % len(str_key)
# # 3 goes into 0 zero times.
#
# index, x enumate(list)


""" So you want to figure out an equation that will get you the index into str_key for the corresponding index in message
str_key[index] + encoded_message[index,key]""""""

# Or you could make a separate variable to track your position into str_key and check when it goes out of bounds. Either approach will work


encode("scout", 1939)

# should return 244

    # use 'letter' key to get int value
    # for char in message:
        # access number correlation to char from encoded.

# {'a':0, 'b':2, 'c':3}

#def encode(message, key):
# arr = [] for i in message:
# arr.append(map[i])
# for i in range(0,len(arr),1):
# key = str(key) 
# arr[i] += int(key[i%len(str(key))]) return arr"""