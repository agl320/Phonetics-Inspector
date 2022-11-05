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


opt = int(input("(1) Analyse or (2) German cognate: "))

if opt == 1:
    word_lst = list(input("Input string: "))


    print("-------------- CHAR, LOCATION, VOICE, MANNER --------------")
    
    for char in word_lst:
        if char in location:
            print(f"{char}, {location[char]}, {voice[char]}")
        elif char in vowels:
            print(f"{char}, vowel")
        else:
            print(f"{char}, location unknown, voice unknown")

    print("----------------------- END -----------------------")

elif opt == 2:
    while(input("Continue (y/n)? ") == "y"):
        word_lst = list(input("Input string: "))
        word_new = []

        t_pre = False
        for i in range(len(word_lst)):
                if word_lst[i] == "p":
                    word_new.append("f")
                elif word_lst[i] == "t":
                    word_new.append("s")
                    t_pre = True
                elif word_lst[i] == "b":
                    word_new.append("p")
                elif word_lst[i] == "d":
                    word_new.append("t")
                elif word_lst[i] == "h" and t_pre == True:
                    word_new.append("d")
                    word_new[i-1] = "_"
                elif word_lst[i] == "w":
                    word_new.append("v")
                else:
                    word_new.append(word_lst[i])
                
                if word_lst[i] != "h" and word_lst[i] != "t" and t_pre == True:
                    t_pre = False
        
        print("".join(word_new).replace("_",""))