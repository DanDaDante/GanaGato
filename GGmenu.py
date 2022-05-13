from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from GridLayoutColor import GridLayoutColor

class GGmenu(App):
    def __init__(self,**kwargs):
        #Llamar al constructor de la clase base (App)
        super().__init__(**kwargs)   
        
    def build(self):
        self.gdl_principal = GridLayoutColor(cols=3,rows=1)
        self.gdl_principal._update_color([0,0,1,1])
        #1.Etiqueta
        self.lbl_blank = Label(text="")
        self.gdl_principal.add_widget(self.lbl_blank)
        #2.Grid medio
        self.gdl_medio = GridLayoutColor(rows=3)
			#Widgets
        self.lbl_ruta = Label(text="Ruta del Archivo")
        self.txi_ruta = TextInput(text="", multiline=False)
        self.btn = Button(text="OK")
			#Modificaciones
        self.gdl_medio._update_color([0,128/255,128/255,1])
        self.btn.background_color = (216/255,250/255,8/255,1)
			#Agregar
        self.gdl_medio.add_widget(self.lbl_ruta)
        self.gdl_medio.add_widget(self.txi_ruta)
        self.gdl_medio.add_widget(self.btn)
        self.gdl_principal.add_widget(self.gdl_medio)
		#3.Etiqueta
        self.lbl_blank2 = Label(text="")
        self.gdl_principal.add_widget(self.lbl_blank2)
        return self.gdl_principal

if __name__ == '__main__':
    gg = GGmenu()
    gg.run()
