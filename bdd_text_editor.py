#!/bin/env python3.7

import json
import re
from tkinter import Tk, ttk, Frame, Entry,\
                    END, Text, Scrollbar, \
                    RIGHT, LEFT, X, Y, TOP, BOTTOM,\
                    filedialog, Listbox, SINGLE, ACTIVE

class Application():
    def __init__(self):
        "Initialize Application"

        self.root = Tk()

        # set title
        self.root.title('BDD Text Editor')
        self.root.attributes('-fullscreen',True)

        #set save button
        self.save_button()

        # set scroll bar
        self.set_scroll_bar()

        #set run button
        self.run_button()

        # set text widget
        self.text = Text(font=("Helvetica", 18))
        #self.text.bind('<Return>', self.auto_complete)
        self.text.bind('<space>', self.auto_complete)
        self.text.pack(expand=True, fill='both')
        
        # read the steps json
        self.steps = self.read_steps_json()
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


    def auto_complete(self, event):
        "Auto complete the text"
        try:
            self.list_box.destroy()
        except:
            pass
        #step = self.text.get('1.0', 'end-1c')
        self.current_step = self.text.get('end - 1 lines linestart', 'end - 1 lines lineend')
        self.check_sp_char = re.search('^\W+', self.current_step)
        if self.check_sp_char:
            self.current_step = self.current_step.strip(self.check_sp_char.group())
            print(self.check_sp_char.group())
        if len(self.current_step.split(' ')) >= 2:
            self.matching_steps = []
            re_match = re.compile(self.current_step + '.*')
            self.matching_steps = list(filter(re_match.match, self.steps))
            if self.matching_steps:
                self.list_box = Listbox(self.text, selectmode=SINGLE)
                #self.list_box.delete(0, END)
                for i in range(0,len(self.matching_steps)):
                    self.list_box.insert(i+1, self.matching_steps[i])
                self.list_box.pack(expand=True, fill=X)
                self.list_box.bind('<<ListboxSelect>>', self.on_list_box_select)


    def on_list_box_select(self, event):
        "Actions after selecting list bos"
        selection_index = int(self.list_box.curselection()[0])

        # delete the existing line & insert the new line
        self.text.delete('current linestart', 'current lineend')
        replace_string = self.matching_steps[selection_index]
        if self.check_sp_char:
            replace_string = self.check_sp_char.group() + replace_string
        self.text.insert(END, replace_string)
        #self.list_box.delete(0, END)
        #print(dir(self.list_box))
        self.list_box.destroy()
        self.matching_steps = []

    def read_steps_json(self):
        "Read the steps json file"
        with open('steps_catalog.json', 'rb') as steps_file:
            steps = json.load(steps_file)
        
        steps = [step['name'] for step in steps]
        return steps


app = Application()
