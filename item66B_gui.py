from tkinter import *
from tkinter import ttk
import shutil
import os

import item66B_func 
import item66B_main


def load_gui(self):

    #Source objects
    self.source = StringVar()
    self.source_var = ''
    self.source.set("???")
    self.source_dir = ''

    #Destination objects
    self.destination = StringVar()
    self.destination_var = ''
    self.destination.set("???")
    self.destination_dir = ''

    #Last Check objects
    self.last_check = StringVar()
    self.last_check_var = ''
    self.last_check.set("???")

    #Next Check objects
    self.next_check = StringVar()
    self.next_check_var = ''
    self.next_check.set("???")



    #LAST CHECK LABELS
    self.lbl_srch  = ttk.Label(self.master, text = 'Last Run:').pack(pady=(10,0))
    self.lbl_last = ttk.Label(self.master, textvariable = self.last_check).pack(pady=(0,0))

    self.lbl_nexth  = ttk.Label(self.master, text = 'Next Run:').pack(pady=(10,0))
    self.lbl_next = ttk.Label(self.master, textvariable = self.next_check).pack(pady=(0,10))
    
    #SELECT SOURCE button
    self.btn_src = ttk.Button(self.master,text = 'Select Source Folder',
                                    command = lambda: item66B_func.get_src(self)).pack(pady = (15,0))
    #SELECT SOURCE labels
    self.lbl_srch  = ttk.Label(self.master, text = 'Source folder:').pack(pady=(10,0))
    self.lbl_src  = ttk.Label(self.master, textvariable = self.source).pack()
    
    #SELECT DESTINATION button
    self.btn_dest = ttk.Button(self.master,text = 'Select Destination Folder',
                                    command = lambda: item66B_func.get_dest(self)).pack(pady = (10,10))
    #SELECT DESTINATION labels
    self.lbl_desth  = ttk.Label(self.master, text = 'Destination folder:').pack()
    self.lbl_dest = ttk.Label(self.master, textvariable = self.destination).pack()

    #SELECT COMBO BOX OPTIONS
    self.lbl_check_time = ttk.Label(self.master,text = 'Select Next File Run Time').pack(pady = (20,10))
    #NEXT CHECK LABELS
    self.time = StringVar()
    self.combobox = ttk.Combobox(self.master, textvariable = self.time)
    self.combobox.pack()
    self.combobox.config(values = ('12:00am','3:00am','6:00am','9:00am',
                             '12:00pm','3:00pm','6:00pm','9:00pm',))
    self.time.set('12:00am')



    
if __name__ == "__main__":
    pass
