def incript(initial_word, key_word):
    # initial_word = input()
    # key_word = input()
    # combined_word = key_word[: len(key_word)+1]
    combined_word = key_word + initial_word[: (len(initial_word)- len(key_word))]

    decripte_text = ""

    print(initial_word)
    print(key_word)
    print(combined_word)
    # dic_data = {}
    # for i in range(26):
    for i in range (len(initial_word)):
        for j in range (len(combined_word)):
            if i == j:
                new_char = (ord(initial_word[i])- 65) + (ord(combined_word[j])- 65)
                real_new_char = chr( (new_char % 26) + 65)
                decripte_text += real_new_char

    return decripte_text

# print(incript("SENDMOREMONKEYS", "ACM"))

def decript(sphered_text, key_word):
    combined_word = key_word + sphered_text[: (len(sphered_text)- len(key_word))]
    incripte_message  =  ""
    print(sphered_text)
    print(key_word)
    print(combined_word)
    for i in range (len(sphered_text)):
        for j in range (len(combined_word)):
            if i == j:
                new_char = (ord(sphered_text[i])- 65) - (ord(combined_word[j])- 65)
                real_new_char = chr( (new_char % 26) + 65)
                incripte_message += real_new_char
    return incripte_message

print(decript("SGZVQBUQAFRWSLC", "ACM"))



# 
# def decript(sphered_text, key_word):
#     combined_word = key_word + sphered_text[: (len(sphered_text)- len(key_word))]
#     incripte_message  =  ""
#     for i in range (len(sphered_text)):
#         for j in range (len(key_word)):
#             if i == j:
#                 new_char = (ord(combined_word[i])- 65) - (ord(key_word[j])- 65)
#                 real_new_char = chr( (new_char % 26) + 65)
#                 incripte_message += real_new_char
#     return incripte_message
