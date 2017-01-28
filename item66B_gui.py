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




    #LAST CHECK LABELS
    self.lbl_srch  = ttk.Label(self.master, text = 'Last Run:').pack(pady=(10,0))
    self.lbl_last = ttk.Label(self.master, textvariable = self.last_check).pack(pady=(0,0))
    
    #SELECT SOURCE button
    self.btn_src = ttk.Button(self.master,text = 'Select Source Folder',
                                    command = lambda: item66B_func.get_src(self)).pack(pady = (30,0))
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
    self.btn_move = ttk.Button(self.master,text = 'Move Files', command = lambda: item66B_func.move_files(self)).pack(pady = (20,10))


    
if __name__ == "__main__":
    pass
