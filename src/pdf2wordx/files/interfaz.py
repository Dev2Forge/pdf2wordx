from tkinter import Button,Label,Entry,Tk

# Clase encargada de crear la ventana base
class Window:
	def __init__(self,root:any,width:int=300,height:int=300,bgColor:str='green',title:str='Window',resizable:list=[False,False]) -> None:
		self.root=root
		self.width=width
		self.height=height
		self.bgColor=bgColor
		self.title=title
		self.resizable=resizable
		self.__window()

	# Método encargado de craer la ventana con sus atributos
	def __window(self) -> None:
		self.root['bg']=self.bgColor
		self.root.title(self.title)
		self.root.geometry(f'{self.width}x{self.height}{self.__centerWindow()}')
		self.root.resizable(self.resizable[0],self.resizable[1])

	# Centrar ventana
	def __centerWindow(self) -> str:
		screenWidth:int=self.root.winfo_screenwidth()
		screenHeight:int=self.root.winfo_screenheight()
		winWidthCenter:int=(screenWidth-self.width)//2
		winHeightCenter:int=(screenHeight-self.height)//2
		geometry:str=f'+{winWidthCenter}-{winHeightCenter}'
		return geometry

	# Loop ventana principal
	def loopWindow(self):
		self.root.mainloop()

# Clase encargada de los widgets
class Widgets:
	def __init__(self,master:any,elements:list) -> None:
		self.master=master # Ventana Tk
		self.elements=elements # [[element],...,n,[element]]
		self.widgetsList=[] # [Elemntos en pantalla]
		self.configItems=[]

	# Crear botones idénticos
	def widgetsCreate(self,itemsOptions:list[dict]=[{}],package:list=[],optionsPack:list[dict]=[{}]):
		try:
			# Acceder tanto al índice como al elemento |0,Button| |1,Label|
			for i,item in enumerate(self.elements):
				# Manejo del flujo del programa, verificar que i sea menor a longitud de "itemsOptions"
				self.__createWidget(itemsOptions,package,optionsPack,i,item)
		except Exception as e:
			print('Error in normalButton(): ',e)

	def __createWidget(self,opcionItem,packType,packOps,i,widget):
		if self.__verifyIndexRange(i,opcionItem):
			# widget será igual a el elemento con sus atributos: Button(master=tkinter.Tk(),text='Click Me',command=click)
			widget = widget(self.master,opcionItem[i])
			# Se agrega cada widget a la listad e widgets (si en un momento se necesita información adicional)
			self.widgetsList.append(widget)
			# Obteneer atributos del elemento
			self.__getAtributtesItem(opcionItem[i])
			# Verificar que i sea menor a la longitud de "packOps"
			self.__choosePackOptions(i,packOps,packType,widget)
			

	def __choosePackOptions(self,i,opPack,packList,wid):
		if self.__verifyIndexRange(i,opPack):
			if i < len(packList):
				# Forma 1 para llamar __packItem() sin errores
				self.__packItem(wid,packList[i],opPack[i])
			else:
				# Forma 1 para llamar __packItem() sin errores
				self.__packItem(wid,opPack[i])
		else:
			self.__exePack(i,packList,wid)
	
	def __exePack(self,pos,packs,wid):
		if pos < len(packs):
			# cuando i sea mayor a "opPack", significará que no existe 
			# y por tanto ese elemento tendrá sus configuraciones (configure()) en blanco
			self.__packItem(wid,packs[pos])
		else:
			# cuando i sea mayor a "opPack", significará que no existe 
			# y por tanto ese elemento tendrá sus configuraciones (configure()) en blanco
			self.__packItem(wid)

	# Método para empaquetar elementos, uno a uno
	def __packItem(self,item:any,typePack:str='pack',opsPack:dict={}):
		# Se comprueba si el "typePack" corresponde a un método válido, ejemplo con 'pack': item.pack()
		# Retorna True o False
		# getattr(item,typePack) -> item.typePack()
		if callable(getattr(item,typePack)):
			# Se llama el método empaquetador y se le dan sus opcines correspondientes
			getattr(item,typePack)(opsPack)

	# Agregar los atributos de cada item a la lista de configuraciones
	def __getAtributtesItem(self,option):
		self.configItems.append(option)

	def getText(self,pos):
		return self.widgetsList[pos].get()

	def __verifyIndexRange(self,value,item):
		if value < len(item):
			return True
		else:
			return False


if __name__ == '__main__':
	# Clase encargada de unir todas las partes y ejecutarlas
	class App(Window):
		def __init__(self,root:any,width:int,height:int,colorBg:str,title:str):
			Window.__init__(self,root,width,height,colorBg,title)
			self.root=root
			self.elements=[Button,Label,Entry,Entry]
			# Objetos widgets
			self.widgets=Widgets(self.root,self.elements)
			self.elementsOptions=[
							{'width':3,'wrap':5,'text':'Say Hello','bg':'yellow'},
							{'text':'Hello World','fg':'green','bg':'Black'},
							{'bg':'red','fg':'white','font':('Helvetica',10,'bold')},
							{'bg':'green','fg':'white','font':12,'insertwidth':2}
						]
			self.elementsPack=['pack','pack','place']
			self.optionsPack=[
							{'fill':'both','expand':False,'side':'right'},
							{'expand':True},
							{'relx':0.3,'rely':0.2}
						]
			
			# Método para crear botones
			self.widgets.widgetsCreate(self.elementsOptions,self.elementsPack,self.optionsPack)
			
			# Añadir comando a botón
			self.widgets.widgetsList[0].configure(command=lambda:self.click(self.widgets.getText(2)))

		# Obtener texto de un entry
		def click(self,txt):
			#txt=item.get()
			self.widgets.widgetsList[1].configure(text=f'Hello {txt}')

	tk=Tk()
	app=App(tk,300,200,'Black','Window')
	tk.mainloop()