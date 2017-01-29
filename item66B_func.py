from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os
import time
import datetime 
import sqlite3

import item66B_main
import item66B_gui



def create_db(self):
    conn = sqlite3.connect('Tech66.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists fileCheck( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            checkTime TEXT, \
            srcDir TEXT, \
            destDir TEXT, \
            modDateTime TEXT, \
            createDateTime TEXT \
            );")
        
        conn.commit()
    count_records(self,cur)
    if self.count < 1:
        self.last_check.set("No records found")
##        cur = conn.cursor()
##        cur.execute("INSERT INTO fileCheck (checkTime,srcDir,destDir,modDateTime,createDateTime)\
##                    VALUES(?,?,?,?,?)",(datetime.datetime.now(),'NUll','NUll','NUll','NUll'))
##        conn.commit()
        #conn.close()

def count_records(self,cur):
    self.count = ""
    cur.execute("""SELECT COUNT(*) FROM fileCheck""")
    self.count = cur.fetchone()[0]
    return cur,self.count


def lastCheck(self):
    conn = sqlite3.connect('Tech66.db')
    with conn:
        cur = conn.cursor()
        #self.last_check = ""
        cur.execute("""SELECT checkTime FROM fileCheck ORDER BY checkTime DESC""")
        self.last_check.set(cur.fetchone()[0])
        
        
        conn.commit()
        #conn.close()
    return self.last_check

def get_src(self):
    self.source_dir = filedialog.askdirectory()
    self.source_files = (os.listdir(self.source_dir))
    if source_dir != '':
        self.source.set(self.source_dir)
    

    
def get_dest(self):
    self.destination_dir = filedialog.askdirectory()
    if destination_dir != '' or destination_dir != '???':
        self.destination.set(self.destination_dir)

#def convert_time(self):


       
    

def move_files(self):
    self.time_now     = time.time()
    self.day          = 86400
    self.count        = False
    
    if (self.source) == '???' and (self.destination) == '???':
        messagebox.showinfo(title='Alert', message = 'You must first select files and a destination path.')
    elif (self.source_dir) == (self.destination_dir):
        messagebox.showinfo(title='Alert', message = 'Source and Destination paths cannot be the same.')

    else:
        for i in self.source_files:
            self.source_path = (os.path.join(self.source_dir,i))
            self.diff_mod    = self.time_now - (os.path.getmtime(self.source_path))
            self.diff_create = self.time_now - (os.path.getctime(self.source_path))

            if (self.diff_mod < self.day) or (self.diff_create < self.day):
                shutil.move((os.path.join(self.source_dir,i)),self.destination_dir)
                self.count = True
                #create_db(self)
                log_move(self)
                
    if self.count == True:
        messagebox.showinfo(title='Success', message = "Files transferred successfully!")
    else:
        messagebox.showinfo(title='Success', message = "No files meet transfer criteria.")



def log_move(self):
    self.time_now = datetime.datetime.today()
    conn = sqlite3.connect('Tech66.db')
    
    
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO fileCheck (checkTime,srcDir,destDir,modDateTime,createDateTime)\
                    VALUES(?,?,?,?,?)",(self.time_now,self.source_dir,self.destination_dir,self.diff_mod,self.diff_create))
        conn.commit()
        #conn.close()
    self.time_now = time.time()

if __name__ == "__main__":
    pass
