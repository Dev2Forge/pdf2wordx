from .files import interfaz as win
from .files import functions as funcs
from tkinter import Button, Label, Entry, Tk
from threading import Thread
import asyncio
from chromologger import Logger
from importlib.resources import files
import pdf2wordx

log_path:str = files(pdf2wordx).joinpath('log.log')
logger:Logger = Logger(str(log_path))

class App(win.Window):
    def __init__(self, root: Tk, width: int = 300, height: int = 300, bgColor: str = 'green', title: str = 'Window', resizable: list = [False, False]) -> None:
        super().__init__(root, width, height, bgColor, title, resizable)
        self.width = width
        self.root = root
        icon_path = files(pdf2wordx).joinpath('favicon.ico')
        root.iconbitmap(str(icon_path))
        # Funcs instance
        self.funcs = funcs.Funcs()

        # Main window
        self.root = root

        # Elements (widgets)
        self.elements = [Label, Button, Button, Label, Entry, Button, Button, Label, Label, Label, Button, Label]

        # Options elements
        self.op_elements = [
                {'text':'PDF2WORDX - SRM', 'font':('Helvetica', 20, 'bold'), 'bg':'#001223', 'fg':'white'},
                {'text':'Ayuda','bg':'#001223','width':4, 'height':1, 'fg':'#66ff02', 'relief':'sunken', 'command':self.help},
                {'text':'OSL','bg':'#001223','width':4, 'height':1, 'fg':'#66ff02', 'relief':'sunken', 'command':self.osl},
                {'text':'Nombre Archivo: ', 'bg':'#001223', 'fg':'white'},
                {'bg':'#13004d','fg':'#ffdd02','font':('Consolas', 12, 'bold'), 'justify':'center'},
                {'text':'Abrir Archivo','bg':'#d1ff00', 'width':15, 'pady':5, 'padx':3, 'font':('Helvetica', -12, 'bold'), 'command':self.fileSet},
                {'text':'Elegir Directorio','bg':'#d1ff00', 'width':15, 'pady':5, 'padx':3, 'font':('Helvetica', -12, 'bold'), 'command':self.fileOutSet, 'state':'disabled'},
                {'text':'Archivo PDF: ', 'bg':'#001223', 'fg':'white', 'anchor':'w', 'width':54},
                {'text':'Archivo De Salida: ', 'bg':'#001223', 'fg':'white', 'anchor':'w', 'width':54},
                {'text':'Directorio De Salida: ', 'bg':'#001223', 'fg':'white', 'anchor':'w', 'width':54},
                {'text':'Convertir', 'bg':'#d1ff00', 'width':15, 'pady':5, 'padx':3, 'font':('Helvetica', -12, 'bold'), 'command':self.convertFile, 'state':'disabled'},
                {'text':'© SRM - TRG 2024', 'bg':'#001223', 'font':('Consolas', 7, 'bold'), 'fg':'white'}
            ]

        # Package type
        self.type_package = ['place' for _ in self.op_elements]

        # Pack options
        self.pack_op = [
                {'relx':0.23,'rely':0.05}, # Label (Program Name)
                {'relx':0.02,'rely':0.05}, # Help button
                {'relx':0.1,'rely':0.05}, # Open Source License button
                {'relx':0.23, 'rely':0.23}, # Label (new name file)
                {'relx':0.43,'rely':0.23}, # Entry (Name File out)
                {'relx':0.14,'rely':0.35}, # Open File (button)
                {'relx':0.4,'rely':0.35}, # Set directory (button)
                {'relx':0.13,'rely':0.48}, # Info file name (label)
                {'relx':0.13,'rely':0.568}, # Info file output (label)
                {'relx':0.13,'rely':0.65}, # Info output directory (label)
                {'relx':0.66, 'rely':0.35}, # Convert File (button
                {'relx':0.4, 'rely':0.95}
            ]

        # Widget instance (wigets options)
        self.widget = win.Widgets(self.root,self.elements)
        # Create the widgets 
        self.widget.widgetsCreate(self.op_elements, self.type_package, self.pack_op)

        # Set default filename
        self.widget.widgetsList[4].insert(0, 'document-pdf2wordx')

    def osl(self) -> None:
        __path:str = files(pdf2wordx).joinpath('files/info/NOTICE')
        self.funcs.msgbox(__path, 'Open Source Licenses - Notice')

    def fileSet(self) -> None:
        button = self.widget.widgetsList[6]
        self.funcs._askFile(button)
        label = self.widget.widgetsList[7]
        txt = self.funcs.file_name_original
        self.funcs._setTextLabel(label, 'Archivo PDF: ', txt)
    
    # Select directory out
    def fileOutSet(self) -> None:
        entry = self.widget.getText(4)
        self.funcs._fileNameOut(entry)
        button = self.widget.widgetsList[10]
        self.funcs._askDirOut(button)
        label = self.widget.widgetsList[9]
        txt = self.funcs.file_name_out
        self.funcs._setTextLabel(label, 'Archivo De Salida: ', txt)

    # Convetr File
    def convertFile(self) -> None:
        label = self.widget.widgetsList[8]
        buttons = [self.widget.widgetsList[6], self.widget.widgetsList[10]]
        try:
            # Exe func in other Thread
            Thread(target=lambda: asyncio.run(self.funcs._convertFile(buttons))).start()
            txt = self.funcs.directory_out
            self.funcs._setTextLabel(label, 'Directorio De Salida: ', txt)
        except Exception as e:
            logger.log_e(e)

    def help(self) -> None:
        __path:str = files(pdf2wordx).joinpath('files/info/help')
        self.funcs.msgbox(__path, '¿Cómo usar este programa?')


def run():
    # Instance App
    app = App(Tk(), 500, 300, '#001223', 'PDF2WORDX', [False, False])
    # Loop main window
    app.loopWindow()

if __name__ == "__main__":
    run()