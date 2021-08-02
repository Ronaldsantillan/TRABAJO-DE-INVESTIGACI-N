GREEN = '\033[32m'
import os
from rango import Basico,Intermedio
class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print (opcion)
        opc=input("Elija una opcion[1...{}]: ".format(len(self.opciones)))
        return opc
opc = ""
while opc !="11":
        os.system("clear")
        menuC= Menu(GREEN+"Menu Principal",["1) Presentar los números de 1 a n","2) Sumar los números de 1 a n","3) Múltiplo de cualquier numero","4) Presentar los divisores de un numero","5) Numero Primo","6) Factorial de cualquier numero",
        "7) Fibonacci de una serie de n número","8) Perfecto","9) Primos gemelos","10) Números amigos","11)	Salir"])
        opc=menuC.menu()

        if opc=="1":
                os.system("clear")      
                cond=Basico()
                print(cond.numerosN())
                input("presiona una tecla pa continuar...")
                
                
        elif opc=="2":
                os.system("clear")
                cond=Intermedio()
                print(cond.numerosN())
                input("presiona una tecla pa continuar...")
                
        elif opc=="3":
                os.system("clear")
                cond=Basico()
                print(cond.multiplo())
                input("presiona una tecla pa continuar...")

        elif opc=="4": 
                os.system("clear")
                cond=Basico()
                print(cond.Divisoresnumero())
                input("presiona una tecla pa continuar...")
                        
        elif opc=="5":
                os.system("clear")
                cond=Basico()
                print(cond.Primo())   
                input("presiona una tecla pa continuar...")

        elif opc=="6":
                os.system("clear")
                cond=Intermedio()
                print(cond.factorial())   
                input("presiona una tecla pa continuar...")
                        
        elif opc=="7":
                os.system("clear")
                cond=Intermedio()
                print(cond.fibonacci())   
                input("presiona una tecla pa continuar...")
                        
        elif opc=="8":
                os.system("clear")
                cond=Basico()
                print(cond.perfecto())   
                input("presiona una tecla pa continuar...")
                        
        elif opc=="9":
                os.system("clear")
                print ("Primos gemelos")
                        
        elif opc=="10":
                os.system("clear")
                print ("Números amigos")
                        
        elif opc=="11":
                os.system("clear")
                print ("Gracias por utilizarme coomo tu ex")
                print ("Cuidesese, espeo volver a verl@ pronto")        
        else :
                os.system("clear")
                print("Opcion no valida")