# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

import string

my_text = "She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells."
print(my_text)
# my_set = set(my_text.split())
# print(my_set)
# print(len(my_set))


punct = list(string.punctuation) + ['\n', '\t']
print(punct)

for char in punct:
    my_text.replace(char, '')

my_text = my_text.lower().split()
print(my_text)
dict_count = {}
for key in my_text:
    dict_count[key] = dict_count.get(key, 0) + 1
print(*dict_count.items(), sep='\n')
print(len(set(my_text)))