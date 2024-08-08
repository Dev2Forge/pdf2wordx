import tkinter.messagebox
from tkinter import filedialog
from tkinter import Button, Label, Entry, Tk, StringVar
from pdf2docx import Converter
import os

root = Tk()
root.geometry("700x400")
root.resizable(False, False)
root['bg'] = "#000F5A"
root.title("Convert PDF To WORD - SRM 2024")

#Texto variable del label
string = StringVar()
string3 = StringVar()
string2 = ""
filenamePDF = ""
w_width = root.winfo_screenwidth()
h_height = root.winfo_screenheight()

#Open file from explorer
def file():
    ask = filedialog.askopenfilename(filetypes=[("Sólo pdf puto", "*.pdf")])
    filename = os.path.basename(ask)
    string.set(filename)
    filenamePDF = ask
    print(filenamePDF)
    nameFILE = inputFileName.get()
    salida = dirOutput()
    convertFile(ask, nameFILE, salida)

#Convert file pdf to word
def convertFile(file, nameFile, dirOut):
    try:
        pdf_file = file
        word_file = dirOut + nameFile + ".docx"
        string3.set(word_file)
        print("pdfFile: ", pdf_file, "\nwordFile: ", word_file)
        cv = Converter(pdf_file)
        cv.convert(word_file, start=0, end=None, quality=50)
        cv.close()
        fin = tkinter.messagebox.showinfo("FIN", "Conversión terminada, puedes volver a convertir otro si deaseas BY SRM")
    except Exception as e:
        tkinter.messagebox.showwarning("WARNING - SRM", f"Algo anda mal puto. {e}\nBY SRM")

def dirOutput():
    try:
        dirOut = filedialog.askdirectory()
        string2 = dirOut + "/"
        print("String2 in dirout: ", string2)
        return string2
    except Exception as e:
        tkinter.messagebox.showwarning("Sin directorio - SRM", "Puto, al menos pon un fuck directorio.")

def howUSE():
    infoUser = """
                1. Nombrar tu archivo que se guardará en el recuadro blanco luego sólo debes presionar el botón 
                que dice, 'Abrir Archivo', ahí te pedirá que busques el PDF a convertir, cuando lo encuentres lo 
                seleccionas, después saldrá una ventana que te pedirá en donde vas a guardar el archivo, y ya luego
                solo esperas"""

    tkinter.messagebox.showinfo("How Use? - PDF TO WORD - SRM", infoUser)

#Widgets definitions
askFile = Button(root, text="Abrir Archivo", command= file)
fileNamePDF_info = Label(root, textvariable=string, fg="white", background="#000F5A", wraplength=300)
copyrightSRM = Label(root, text="\u00A9 BY SRM 2024 (Santiago Rivera Marin)", fg="white", background="#000F5A", wraplength=300)
inputFileName = Entry(root)
dirSaveInfo = Label(root, textvariable=string3, fg="white", background="#000F5A", wraplength=300)
howUSe = Button(root, text="How use?", command=howUSE)

#Widgets positions
howUSe.place(y = 10, width=700, anchor="nw")
askFile.place(relx = 0.46, rely = 0.1, anchor = "nw")
fileNamePDF_info.place(x = 100, rely = 0.3, width=520, anchor="nw")
inputFileName.place(x = 250, rely = 0.2, width=220, anchor="nw")
dirSaveInfo.place(x = 150, rely = 0.4, width=420, anchor="nw")
copyrightSRM.place(x = 100, y = 350, width=520, anchor="nw")

#Set string to stringvar
string.set("File Name: ")
string3.set("Dir out: ")
inputFileName.insert(0, "document")

#Bucle de ejecución
root.mainloop()