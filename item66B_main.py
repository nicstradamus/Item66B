from tkinter import *
from tkinter import ttk
import shutil
import os

import item66B_func
import item66B_gui



class start(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title("File Transfer")
        self.master.minsize(300,400) #(Height, Width)
        self.master.maxsize(300,400)

##        src_files = ''
##        dest_path = ''
##        count = 0
        item66B_func.create_db(self)
        item66B_gui.load_gui(self)
        

    
        
if __name__ == "__main__":
    root = Tk()
    my_gui = start(root)
    root.mainloop()