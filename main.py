import numpy as np
import json

with open("location.json","r", encoding='utf8') as json_file:
    location = json.load(json_file)
    json_file.close()

with open("vowels.json","r", encoding='utf8') as json_file:
    vowels = json.load(json_file)
    json_file.close()

with open("voice.json","r", encoding='utf8') as json_file:
    voice = json.load(json_file)
    json_file.close()


word_lst = list(input("Input string: "))


print("-------------- CHAR, LOCATION, VOICE --------------")
 
for char in word_lst:
    if char in location:
        print(f"{char}, {location[char]}, {voice[char]}")
    elif char in vowels:
        print(f"{char}, vowel")
    else:
        print(f"{char}, location unknown, voice unknown")

print("-------------- ---------END -----------------------")