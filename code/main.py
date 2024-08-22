import files.interfaz as win
import files.functions as funcs
from tkinter import Button, Label, Entry, Tk



class App(win.Window):
    def __init__(self, root: Tk, width: int = 300, height: int = 300, bgColor: str = 'green', title: str = 'Window', resizable: list = [False, False]) -> None:
        super().__init__(root, width, height, bgColor, title, resizable)
        self.width = width
        self.root = root

        root.iconbitmap('favicon.ico')
        # Funcs instance
        self.funcs = funcs.Funcs()

        # Main window
        self.root = root

        # Elements (widgets)
        self.elements = [Label, Button, Label, Entry, Button, Button, Label, Label, Label, Button, Label]

        # Options elements
        self.op_elements = [
                {'text':'PDF TO DOCX - SRM', 'font':('Helvetica', 20, 'bold'), 'bg':'#001223', 'fg':'white'},
                {'text':'?','bg':'#9e2900','width':30, 'height':30, 'bitmap':'questhead', 'fg':'#66ff02', 'relief':'sunken', 'command':self.help},
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
        self.widget.widgetsList[3].insert(0, 'hola')

    def fileSet(self) -> None:
        button = self.widget.widgetsList[5]
        self.funcs._askFile(button)
        label = self.widget.widgetsList[6]
        txt = self.funcs.file_name_original
        self.funcs._setTextLabel(label, 'Archivo PDF: ', txt)
    
    # Select directory out
    def fileOutSet(self) -> None:
        entry = self.widget.getText(3)
        self.funcs._fileNameOut(entry)
        button = self.widget.widgetsList[9]
        self.funcs._askDirOut(button)
        label = self.widget.widgetsList[7]
        txt = self.funcs.file_name_out
        self.funcs._setTextLabel(label, 'Archivo De Salida: ', txt)

    # Convetr File
    def convertFile(self) -> None:
        label = self.widget.widgetsList[8]
        buttons = [self.widget.widgetsList[5], self.widget.widgetsList[9]]
        try:    
            #button = self.widget.widgetsList[5]
            self.funcs._convertFile(buttons)
            txt = self.funcs.directory_out
            self.funcs._setTextLabel(label, 'Directorio De Salida: ', txt)
        except Exception as e:
            print('Error: ', e)

    def help(self) -> None:
        self.funcs._help()


def run():
    # Instance App
    app = App(Tk(), 500, 300, '#001223', 'PDF To WORD', [False, False])
    # Loop main window
    app.loopWindow()