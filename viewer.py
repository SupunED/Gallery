from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image viewer')
root.iconbitmap('icon/amongus.ico')

my_img1 = ImageTk.PhotoImage(Image.open("Gallery/Eren.jfif"))
my_img2 = ImageTk.PhotoImage(Image.open("Gallery/cover.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Gallery/AttackTitan.jfif"))
my_img4 = ImageTk.PhotoImage(Image.open("Gallery/Femaletitan.jfif"))

image_list = [my_img1, my_img2, my_img3, my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def back(image_number):
    global my_label
    global button_back
    global button_forward
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command= lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command= lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    

def forward(image_number):
    global my_label
    global button_back
    global button_forward
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command= lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command= lambda: back(image_number-1))
    
    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()