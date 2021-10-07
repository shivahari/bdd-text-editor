#!/bin/env python3.7

from tkinter import Tk, ttk, Frame, Entry,\
                    END, Text, Scrollbar, \
                    RIGHT, LEFT, Y, TOP, BOTTOM,\
                    filedialog

class Application():
    def __init__(self):
        "Initialize Application"

        self.root = Tk()

        # set title
        self.root.title('BDD Text Editor')

        #set save button
        self.save_button()

        # set scroll bar
        self.set_scroll_bar()

        #set run button
        self.run_button()

        # set text widget
        self.text = Text()
        self.text.pack()

        self.root.mainloop()


    def set_scroll_bar(self):
        "Set a scroll bar to text widget"
        scroll_bar = Scrollbar(self.root)
        scroll_bar.pack(side=RIGHT, fill=Y)


    def save_button(self):
        "Save button"
        save_button = ttk.Button(self.root, text='Save', command=self.saveas)
        save_button.pack(anchor='e', side=BOTTOM)


    def saveas(self):
        "Save a file"
        text = self.text.get('1.0', 'end-1c')
        save_location = filedialog.asksaveasfilename()
        file = open(save_location, 'w+')
        file.write(text)
        file.close()


    def run_button(self):
        "Run the file"
        run_button = ttk.Button(self.root, text='Run', command=self.run_file)
        run_button.pack(anchor='w', side=BOTTOM)


    def run_file(self):
        "Run the file"
        pass


app = Application()
