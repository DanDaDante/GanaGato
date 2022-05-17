from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from GridLayoutColor import GridLayoutColor
#####
import csv
import json
from pathlib import Path
from datetime import datetime
import pymysql.cursors


class GGmenu(App):
    def btn_press(self, obj):
        if self.connection:
            print("Existe")
            RutaCSV = Path(self.txi_ruta.text)
            if RutaCSV.exists():
                Datos = []
                with RutaCSV.open() as ArchivoCSV:
                    ArchivoCSV.readline()
                    Lector = csv.reader(ArchivoCSV)
                    for fila in Lector:
                        #print(fila)
                        Datos.insert(0,fila)
                MiCursor = self.connection.cursor()
                SQL = """
                    insert into ganagato
                    values (20,null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
                for fila in Datos:
                    D = []
                    D.append( int(fila[2]))
                    D.append( int(fila[3]))
                    D.append( int(fila[4]))
                    D.append( int(fila[5]))
                    D.append( int(fila[6]))
                    D.append( int(fila[7]))
                    D.append( int(fila[8]))
                    D.append( int(fila[9]))
                    D.append( int(fila[10]))
                    D.append( datetime.strptime(fila[11], '%d/%m/%Y'))
                    print(D)
                    MiCursor.execute(SQL,D)
                self.connection.commit()
        else:
            print("No existe")
    
    def iniciarDB(self):
        self.Conf = None
        with open("db.json") as jsonfile:
            self.Conf = json.load(jsonfile)
        self.connection = pymysql.connect(
            host=self.Conf['HOST'],user=self.Conf['DBUSER'],
            password=self.Conf['DBPASS'],database=self.Conf['DBNAME'],
            charset='utf8mb4',port=self.Conf['PORT']
        )
    
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
        self.btn.bind(on_press=self.btn_press)
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
    gg.iniciarDB()
    gg.run()
