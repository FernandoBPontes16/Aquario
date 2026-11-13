import tkinter as tk
import math
import random

root = tk.Tk()
root.title("Aquario")
root.geometry("600x400")
fish_h = 0.5 # go to right
t = 0 # time
desired_height = 100

canvas = tk.Canvas(root, width=600, height=400, bg='black')
canvas.pack(anchor=tk.CENTER, expand=True)
fish = canvas.create_text((300, 100),text="><(((°>", fill="white", font='TkDefaultFont 12')
sand = canvas.create_text((300, 390), text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", fill="white", font='TkDefaultFont 12')
little_bublle1 = canvas.create_text((100, 350),text=".", fill="white", font='TkDefaultFont 12')
little_bublle2 = canvas.create_text((523, 360),text=".", fill="white", font='TkDefaultFont 12')
little_bublle3 = canvas.create_text((34, 300),text=".", fill="white", font='TkDefaultFont 12')
little_bublle4 = canvas.create_text((420, 323),text=".", fill="white", font='TkDefaultFont 12')
medium_bublle1 = canvas.create_text((54, 321),text="o", fill="white", font='TkDefaultFont 12')
medium_bublle2 = canvas.create_text((275, 361),text="o", fill="white", font='TkDefaultFont 12')
medium_bublle3 = canvas.create_text((332, 323),text="o", fill="white", font='TkDefaultFont 12')
medium_bublle4 = canvas.create_text((554, 353),text="o", fill="white", font='TkDefaultFont 12')
medium_bublle5 = canvas.create_text((471, 371),text="o", fill="white", font='TkDefaultFont 12')
big_bublle1 = canvas.create_text((321, 341),text="O", fill="white", font='TkDefaultFont 12')
big_bublle2 = canvas.create_text((123, 280),text="O", fill="white", font='TkDefaultFont 12')
big_bublle3 = canvas.create_text((170, 364),text="O", fill="white", font='TkDefaultFont 12')

def bubble_move(bubble):
    #fazer dps
    print("fds")

def choose_height():
    global desired_height
    if 50 <= desired_height <= 100:
        desired_height = random.randint(50, 110)
    if 100 <= desired_height <= 150:
        desired_height = random.randint(90, 160)
    if 150 <= desired_height <= 200:
        desired_height = random.randint(140, 210)
    if 200 <= desired_height <= 250:
        desired_height = random.randint(190, 260)
    if 250 <= desired_height <= 300:
        desired_height = random.randint(240, 290)


    root.after(1000, choose_height)

def fish_move():
    global fish_h, t, desired_height
    t += 0.025

    fish_pos = canvas.bbox(fish) # [x_esquerda, y_superior, x_direita, y_inferior]
    desloc_y = desired_height - fish_pos[1]
    fish_v = desloc_y * 0.02

    canvas.move(fish, fish_h, fish_v)
    root.after(10, fish_move)
    if(fish_pos[2] >= 599):
        fish_h = -0.5 # go to left
        canvas.itemconfig(fish,text="<°)))><")
    if(fish_pos[0] <= 1):
        fish_h = 0.5 # go to right
        canvas.itemconfig(fish,text="><(((°>")

choose_height()    
fish_move()    
root.mainloop()