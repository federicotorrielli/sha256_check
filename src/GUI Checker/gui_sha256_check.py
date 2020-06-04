from tkinter import *
from tkinter import filedialog
import hashlib
import sys
import os
#made by Lorenzo Sciandra

def main(argv):
    if argv == txtfld.get():
        finalLbl.config(fg='green',text="Hash are identical")
    else:
        finalLbl.config(fg='red',text="Hash are different")

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=window, initialdir="/", title='Please select a file')
    if len(tempdir) > 0:
        BLOCK_SIZE = 65536
        file_hash = hashlib.sha256()
        try:
            with open(tempdir, 'rb') as f:
                fb = f.read(BLOCK_SIZE)
                while len(fb) > 0:
                    file_hash.update(fb)
                    fb = f.read(BLOCK_SIZE)
            main(file_hash.hexdigest())
        except IndexError:
            print('Whoopsie! Something went wrong...\n' + 'Usage: python sha256_check *file* *sha256*')
        except OSError as err:
            print(err)
    return tempdir

window=Tk()
window.columnconfigure(0, weight=1)

btn=Button(window,width="20",height="2",text="Choose Path", fg='black',command=search_for_file_path)
end = Button(window, width="20", height="2", text="Close Window", fg='black',command=window.destroy)
finalLbl=Label(window, text="", font=("TimesNewRoman", 20))
lbl = Label(window, text= "Hash to compare:")
txtfld=Entry(window, bd=2)

window.title('SHA-256 Checker')
window.resizable(False, False)

finalLbl.grid(row = 0, column = 0, columnspan=2, sticky = W, padx=20,pady = 20)
lbl.grid(row = 1, column = 0, sticky = W, padx=20,pady = 20)
txtfld.grid(row = 1, column = 1, sticky = W, padx=20,pady = 20)
btn.grid(row = 2, column = 0, sticky = W, padx=20,pady = 20)
end.grid(row = 2, column = 1, sticky = W, padx=20,pady = 20)
window.mainloop()