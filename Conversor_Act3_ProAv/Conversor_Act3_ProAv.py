import tkinter as tk

def Farenheint_Celsius():
    Farenheint = float(tbFarenheint.get())
    Celsius = (Farenheint-32)*5/9
    tbCelsius.delete(0, tk.END)
    tbCelsius.insert(0, f"{Celsius:.2f}" )

def Celsius_Farenheint():
    Celsius = float(tbCelsius.get())
    Farenheint = (Celsius *9/5) + 32
    tbFarenheint.delete(0, tk.END)
    tbFarenheint.insert(0, f"{Farenheint:.2f}")
    
def limpiar():
    tbCelsius.delete(0, tk.END)
    tbCelsius.insert(0,"")
    tbFarenheint.delete(0, tk.END)
    tbFarenheint.insert(0,"")
    
    
    
ventana= tk.Tk()
ventana.title("Conversor de Temperatura")
lbFarenheint = tk.Label(ventana,text = "Farenheint: ")
lbFarenheint.grid(row=0,column=0)
tbFarenheint = tk.Entry(ventana)
tbFarenheint.grid(row=0,column=1)
btnFarenheint = tk.Button(ventana, text="Convertir a Celsius",command = Farenheint_Celsius)
btnFarenheint.grid(row=0,column=2)
   
lbCelsius = tk.Label(ventana, text = "Celsius: ")
lbCelsius.grid(row=1,column=0)
tbCelsius = tk.Entry(ventana)
tbCelsius.grid(row=1,column=1)
btnCelsius= tk.Button(ventana, text = "Convertir a Farenheint",command = Celsius_Farenheint)
btnCelsius.grid(row=1, column=2)
    
btnlimpiar = tk.Button(ventana, text = "Limpiar", command = limpiar)
btnlimpiar.grid(row=2, column=1)

ventana.mainloop()
