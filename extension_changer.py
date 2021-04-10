'''
    Program: Extension changer
    Author: akr
    GitHub: a-k-r-a-k-r

'''

import os
import tkinter
from tkinter import filedialog, StringVar


#Define fonts and colors
my_font = ('Times New Roman', 12)
root_color = 'black'
button_color = '#e2cff4'
text_color = 'green'


#defining basic structure of window
root=tkinter.Tk()
root.title("Extension Manipulator")
root.geometry("500x300")
root.resizable(0,0)
root.config(bg=root_color)


#defining functions
def get_folder():
    global folder_path
    folder_path = filedialog.askdirectory(initialdir='./', title="Select Folder")
    print(folder_path)


def get_extension():
    change_to = to_extension.get()
    #change_from = from_extension.get()
    change_from = "py"

    files=os.listdir(folder_path)

    for file in files:
        if (".%s"%change_from) in file:
            #newfile=file.replace('.py','.png')
            newfile=file.replace((".%s"%change_from),".%s"%change_to)
            os.rename((folder_path+'/'+file),(folder_path+'/'+newfile))


#defining frames
from_frame = tkinter.Frame(root)
to_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
from_frame.pack()
to_frame.pack(pady=20)
button_frame.pack()

#defining widgets for frames
folder_label = tkinter.Label(from_frame)
browse_button = tkinter.Button(from_frame, text="Browse",bg="green", command=get_folder)
folder_label.grid(row=3,column=0)
browse_button.grid(row=3,column=1)
from_extension = StringVar()
from_extension.set("c")
mp3_radio = tkinter.Radiobutton(from_frame, text=".mp3", variable=from_extension, value="mp3")
mp4_radio = tkinter.Radiobutton(from_frame, text=".mp4", variable=from_extension, value="mp4")
c_radio = tkinter.Radiobutton(from_frame, text=".c", variable=from_extension, value="c")
cpp_radio = tkinter.Radiobutton(from_frame, text=".cpp", variable=from_extension, value="cpp")
py_radio = tkinter.Radiobutton(from_frame, text=".py", variable=from_extension, value="py")
js_radio = tkinter.Radiobutton(from_frame, text=".js", variable=from_extension, value="js")
jpeg_radio = tkinter.Radiobutton(from_frame, text=".jpeg", variable=from_extension, value="jpeg")
jpg_radio = tkinter.Radiobutton(from_frame, text=".jpg", variable=from_extension, value="jpg")
pdf_radio = tkinter.Radiobutton(from_frame, text=".pdf", variable=from_extension, value="pdf")
log_radio = tkinter.Radiobutton(from_frame, text=".log", variable=from_extension, value="log")
txt_radio = tkinter.Radiobutton(from_frame, text=".txt", variable=from_extension, value="txt")
md_radio = tkinter.Radiobutton(from_frame, text=".md", variable=from_extension, value="md")
json_radio = tkinter.Radiobutton(from_frame, text=".json", variable=from_extension, value="json")
java_radio = tkinter.Radiobutton(from_frame, text=".java", variable=from_extension, value="java")
ico_radio = tkinter.Radiobutton(from_frame, text=".ico", variable=from_extension, value="ico")
dll_radio = tkinter.Radiobutton(from_frame, text=".dll", variable=from_extension, value="dll")
custom_radio = tkinter.Radiobutton(from_frame, text="custom", variable=from_extension, value="custom")

mp3_radio.grid(row=0,column=0)
mp4_radio.grid(row=0,column=1)
c_radio.grid(row=0,column=2)
cpp_radio.grid(row=0,column=3)
py_radio.grid(row=0,column=4)
js_radio.grid(row=0,column=5)
jpeg_radio.grid(row=1,column=0)
jpg_radio.grid(row=1,column=1)
pdf_radio.grid(row=1,column=2)
log_radio.grid(row=1,column=3)
txt_radio.grid(row=1,column=4)
md_radio.grid(row=1,column=5)
json_radio.grid(row=2,column=0)
java_radio.grid(row=2,column=1)
ico_radio.grid(row=2,column=2)
dll_radio.grid(row=2,column=3)
custom_radio.grid(row=2,column=4,columnspan=2)



to_extension = StringVar()
to_extension.set("mp3")
mp3_radio = tkinter.Radiobutton(to_frame, text=".mp3", variable=to_extension, value="mp3")
mp4_radio = tkinter.Radiobutton(to_frame, text=".mp4", variable=to_extension, value="mp4")
c_radio = tkinter.Radiobutton(to_frame, text=".c", variable=to_extension, value="c")
cpp_radio = tkinter.Radiobutton(to_frame, text=".cpp", variable=to_extension, value="cpp")
py_radio = tkinter.Radiobutton(to_frame, text=".py", variable=to_extension, value="py")
js_radio = tkinter.Radiobutton(to_frame, text=".js", variable=to_extension, value="js")
jpeg_radio = tkinter.Radiobutton(to_frame, text=".jpeg", variable=to_extension, value="jpeg")
jpg_radio = tkinter.Radiobutton(to_frame, text=".jpg", variable=to_extension, value="jpg")
pdf_radio = tkinter.Radiobutton(to_frame, text=".pdf", variable=to_extension, value="pdf")
log_radio = tkinter.Radiobutton(to_frame, text=".log", variable=to_extension, value="log")
txt_radio = tkinter.Radiobutton(to_frame, text=".txt", variable=to_extension, value="txt")
md_radio = tkinter.Radiobutton(to_frame, text=".md", variable=to_extension, value="md")
json_radio = tkinter.Radiobutton(to_frame, text=".json", variable=to_extension, value="json")
java_radio = tkinter.Radiobutton(to_frame, text=".java", variable=to_extension, value="java")
ico_radio = tkinter.Radiobutton(to_frame, text=".ico", variable=to_extension, value="ico")
dll_radio = tkinter.Radiobutton(to_frame, text=".dll", variable=to_extension, value="dll")
custom_radio = tkinter.Radiobutton(to_frame, text="custom", variable=to_extension, value="custom")

mp3_radio.grid(row=0,column=0)
mp4_radio.grid(row=0,column=1)
c_radio.grid(row=0,column=2)
cpp_radio.grid(row=0,column=3)
py_radio.grid(row=0,column=4)
js_radio.grid(row=0,column=5)
jpeg_radio.grid(row=1,column=0)
jpg_radio.grid(row=1,column=1)
pdf_radio.grid(row=1,column=2)
log_radio.grid(row=1,column=3)
txt_radio.grid(row=1,column=4)
md_radio.grid(row=1,column=5)
json_radio.grid(row=2,column=0)
java_radio.grid(row=2,column=1)
ico_radio.grid(row=2,column=2)
dll_radio.grid(row=2,column=3)
custom_radio.grid(row=2,column=4,columnspan=2)


change_button = tkinter.Button(button_frame, text="Change Extension", command=get_extension)
change_button.pack()

#defining mainloop
root.mainloop()