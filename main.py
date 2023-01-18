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
    window.config(bg='#130542')
    cognate_frame.config(bg='#130542')
    for wid in widget_lst_prim:
        wid.config(bg="#130542",bd=0,fg="white",highlightcolor="white", highlightbackground="#4C20FA")

    for wid in widget_lst_secon:
        wid.config(bg="#1d056e",bd=0,fg="white",highlightcolor="white", highlightbackground="#4C20FA")

def to_lm():
    window.config(bg='#4C20FA')
    cognate_frame.config(bg='#4C20FA')
    for wid in widget_lst_prim:
        wid.config(bg="#4C20FA",bd=0,fg="white",highlightcolor="white", highlightbackground="#130542")

    for wid in widget_lst_secon:
        wid.config(bg="#5c33ff",bd=0,fg="white",highlightcolor="white", highlightbackground="#4C20FA")


def word_analyse():
    global pho_entry 
    for i,letter in enumerate(pho_entry.get()):
        print(letter)
        tk.Label(word_analyse_frame, text=letter).grid(row=0,column=i)
        tk.Label(word_analyse_frame, text="characteristic").grid(row=1,column=i)
    

# TK

window = tk.Tk()
window.geometry('400x300')
w_title = window.title("Phonetics Inspector")


pho_frame = tk.Frame(window)
pho_header = tk.Label(pho_frame, text="Phonetic Info", font=("Arial", 15, 'bold'))
pho_entry = tk.Entry(pho_frame,width=33)
pho_b = tk.Button(pho_frame, text="Analyse", activebackground='#130542', activeforeground='black', command=word_analyse)

word_analyse_frame = tk.Frame(window)




"""
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

"""
# COGNATE
cognate_frame = tk.Frame(window)

w_header = tk.Label(cognate_frame, text="Convert to German Cognate", font=("Arial", 15, 'bold'))

# cognate label
word_entry = tk.Text(cognate_frame,width=33,height=2)

# cognate label init
label_reg = tk.Label(cognate_frame, text=f"Regular: \n")
label_cog = tk.Label(cognate_frame, text=f"Cognate: \n")

# placing widgets 
word_button = tk.Button(
    cognate_frame,
    text="Generate", 
    padx=10, 
    pady=5,
    command=printCognate
    )

dm_button = tk.Button(cognate_frame, text="Dark Mode", activebackground='#130542', activeforeground='white', command=to_dm)
lm_button = tk.Button(cognate_frame, text="Light Mode", activebackground='#4C20FA', activeforeground='white', command=to_lm)

# widget list
widget_lst_prim = [w_header,label_reg,label_cog,word_button,dm_button,lm_button]
widget_lst_secon = [word_entry]


window.config(pady=10,padx=10)

word_analyse_frame.grid(row=1,column=0)
pho_frame.grid(row=0,column=0)

pho_header.grid(row=0,column=0)
pho_entry.grid(row=1,column=0)
pho_b.grid(row=1,column=1)

"""
cognate_frame.grid(row=1,column=0)

w_header.grid(row=0,column=0,columnspan=2)
word_entry.grid(row=1,column=0,columnspan=2)
word_button.grid(row=1,column=2)
label_reg.grid(row=3,column=0,columnspan=2)
label_cog.grid(row=4,column=0,columnspan=2)
dm_button.grid(row=5,column=0)
lm_button.grid(row=5,column=1)
"""
# init widget
to_lm()
window.mainloop()