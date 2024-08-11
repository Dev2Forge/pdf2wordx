from tkinter import messagebox, filedialog, Label, Button
from pdf2docx import Converter
import os

class Funcs:
    def __init__(self) -> None:
        self.filedialog = filedialog
        self.file:str

        # StringVar (to output, info, directory)
        self.file_name_original:str
        self.file_name_out: str
        self.directory_out:str

    # Open File read mode
    def _askFile(self, button:Button) -> None:
        try:
            file = self.filedialog.askopenfilename(filetypes=[('Seleccionar PDF: ', '*.pdf')])
            self.file_name_original = self.__getFileBaseName(file)
            self.file = file
            self._activeButton(button)
        except Exception as e:
            print('Error in _askFile(): ', e)
            messagebox.showerror('Error Selección Archivo', 'Asegúrate de seleccionar un archivo correcto')

    # Set oputput directory
    def _askDirOut(self, button:Button) -> None:
        try:
            self.directory_out = str(filedialog.askdirectory(title='Busca la ruta de salida del archivo'))+'/'+self.file_name_out
            self._activeButton(button)
        except Exception as e:
            print('Error in _askDirOut(): ', e)
            messagebox.showerror('Error Selección Directorio', 'Asegúrate de seleccionar un directorio/ruta correcta/o')

    # Set file name output
    def _fileNameOut(self, txt:str) -> None:
        self.file_name_out = f'{txt}.docx'

    # Extract filename not path
    def __getFileBaseName(self, file:str) -> str:
        return os.path.basename(file)

    # File converter
    def _convertFile(self, button) -> None:
        try:
            convertFile = Converter(self.file)
            convertFile.convert(self.directory_out)
            convertFile.close()
            self._disableButton(button)
            messagebox.showinfo('Conversión Exitosa',f'Se ha convertido el archivo {self.file_name_original} exitosamente')
        except Exception as e:
            print('Error in _convertFile(): ', e)
            messagebox.showerror('Error En Conversión De Archivo', 'Hubo un error convirtiendo el archivo, intente nuevamente')
    
    # Set text label (info)
    def _setTextLabel(self, label:Label, labelStr:str, txt:str) -> None:
        try:
            text = labelStr + txt
            print(txt)
            label.configure(text=text)
        except Exception as e:
            print('Error in _setTextLabel(): ', e)
            messagebox.showerror('Error al asignar texto en Label', 'Hubo un error interno')

    # Change disabled state to normal
    def _activeButton(self, button:Button) -> None:
        button.configure(state='normal')
    
    # Disable buttons
    def _disableButton(self, button:Button | list) -> None:
        print(type(button))
        if type(button) == list:
            for item in button:
                if type(item) == Button:
                    getattr(item, 'configure')(state='disabled')
        
        if type(button) == Button:
            getattr(button, 'configure')(state='disabled')

    def _help(self) -> None:
        try:
            with open('files\info\help', 'r', encoding='utf-8') as fileHelp:
                message = fileHelp.read()
                messagebox.showinfo('How to use this program?', message)
        except Exception as e:
            print('Error in _help(): ', e)
