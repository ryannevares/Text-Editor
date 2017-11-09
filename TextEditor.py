"""
Author: Ryan Nevares
Title: Python GUI Text Editor
Version 1.0

This is a simple Python3-based text editor

Please report any bugs to ryannevares@gmail.com
"""

from tkinter import *
import tkinter.filedialog
from tkinter import messagebox


class text_editor:

    def open_file(self):
        text_file = tkinter.filedialog.askopenfilename(parent=root, initialdir='/$USER/Desktop')
        if text_file:
            self.text_area.delete(1.0, END)  # Delete everyting in the current text area
            with open(text_file) as file:
                self.text_area.insert(1.0, file.read())  # add the contents of the file to the text area
                root.update_idletasks()

    def save(self):
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file != None:
            data = self.text_area.get(1.0, END + "-1c")
            file.write(data)
            file.close()

    def change_font(self):
        print("Font Picked: ", self.font.get())

    def show_about(self):
        messagebox.showwarning("About Text Editor", "Created by Ryan Nevares November 2017.  Please report any bugs to ryannevares@gmail.com")

    def __init__(self, root):
        self.text_to_write = ""
        root.title("Text Editor")
        root.geometry("800x600")
        frame = Frame(root, width=800, height=600)
        scroll = Scrollbar(frame)
        self.text_area = Text(frame, width=800, height=600, yscrollcommand=scroll.set, padx=10, pady=10)
        scroll.config(command=self.text_area.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.text_area.pack(side=LEFT, fill=BOTH, expand=True)
        frame.pack()

        # file menu
        main_menu = Menu(root)
        file_menu = Menu(main_menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=root.quit())

        # Font menu
        self.font = StringVar()
        self.font.set("Times")

        font_menu = Menu(main_menu, tearoff=0)
        font_menu.add_radiobutton(label="Times", variable=self.font, command=self.change_font)
        font_menu.add_radiobutton(label="Ariel", variable=self.font, command=self.change_font)
        font_menu.add_radiobutton(label="Comic Sans", variable=self.font, command=self.change_font)

        # view menu
        view_menu = Menu(main_menu, tearoff=0)
        line_numbers = IntVar()
        line_numbers.set(1)
        view_menu.add_checkbutton(label="Line Numbers", variable = line_numbers)
        view_menu.add_cascade(label="Fonts", menu=font_menu)

        # Help menu
        help_menu = Menu(main_menu, tearoff=0)
        help_menu.add_command(label="About", accelerator="ctrl-H", command=self.show_about)

        main_menu.add_cascade(label="File", menu=file_menu)
        main_menu.add_cascade(label="View", menu=view_menu)
        main_menu.add_cascade(label="Help", menu=help_menu)


        root.config(menu=main_menu)

root = Tk()
text_editor = text_editor(root)

root.mainloop()


""" FUTRE SUGGESTIONS:
Changeable fonts
Line numbers
More menus with more features
add more accelerators <ctrl-H>
"""