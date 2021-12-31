# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:13:37 2021

@author: Ansh Raj
"""

from tkinter import *
from PIL import ImageTk, Image
root=Tk()

root.title("Pokemon Card Gamee")
root.geometry("600x400")

root.configure(background="orange1")

img-ImageTk.PhotoImage(Image.open ("button.jpg"))

player1 = Label(root, text = "Player 1 ", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor = CENTER)

player2 = Label(root, text = "Player 2 ", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.4 , anchor = CENTER)

player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root , bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_card_label = Label(root,bg = "chocolate1", fg = "white")
random_card_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainnloop()