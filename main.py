import numpy as np
import json

import tkinter as tk

# data import
with open("location.json","r", encoding='utf8') as json_file:
    location = json.load(json_file)
    json_file.close()

# includes CLICKS
with open("manner.json","r", encoding='utf8') as json_file:
    manner = json.load(json_file)
    json_file.close()

with open("vowels.json","r", encoding='utf8') as json_file:
    vowels = json.load(json_file)
    json_file.close()

with open("voice.json","r", encoding='utf8') as json_file:
    voice = json.load(json_file)
    json_file.close()
        

"""
opt = int(input("(1) Analyse or (2) German cognate: "))

if opt == 1:
    while(True):
        word_lst = list(input("Input string: "))
        if word_lst == []:
            break

        print("-------------- CHAR, LOCATION, VOICE, MANNER --------------")
        
        for char in word_lst:
            if char in location:
                print(f"{char}, {location[char]}, {voice[char]}, {manner[char]}")
            elif char in vowels:
                print(f"{char}, vowel")
            elif char == " ":
                print("-+-+-+-")
            else:
                print(f"{char}, location unknown, voice unknown, manner unknown")

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
"""

# MAIN

def generateCognate(word_lst):
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
        
        word_result = ("".join(word_new).replace("_",""))
        return word_result

def printCognate():
    var = word_entry.get("1.0",tk.END)
    #var = word_entry.get()
    var_cognate = generateCognate(list(var))

    label_reg.config(text=f"Regular: {var}")
    label_cog.config(text=f"Cognate: {var_cognate}")

def to_dm():
    window.config(bg='black')

# TK

window = tk.Tk()
window.geometry('400x300')
w_title = window.title("IPA-String-info")
w_header = tk.Label(text="Convert to German Cognate", font=("Arial", 15, 'bold'))

# cognate label
word_entry = tk.Text(window,width=33,height=2)

# cognate label init
label_reg = tk.Label(window, text=f"Regular: ")
label_cog = tk.Label(window, text=f"Cognate: ")

# placing widgets 
word_button = tk.Button(
    window,
    text="Generate", 
    padx=10, 
    pady=5,
    command=printCognate
    )

dm_button = tk.Button(window, activebackground='black', command=to_dm)

w_header.grid(row=0,column=0)
word_entry.grid(row=1,column=0)
word_button.grid(row=1,column=1)
label_reg.grid(row=3,column=0)
label_cog.grid(row=4,column=0)
dm_button.grid(row=5,column=0)


window.mainloop()