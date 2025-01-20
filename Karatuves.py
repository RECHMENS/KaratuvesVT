from tkinter import *

height = 400
width = 400

logs = Tk()
logs.title("test")
main = Canvas(logs, width=1200, height=900, bg="#E6E6E6")
main.pack()

#start
#start virsraksts
main.create_text(600,200, text = "Karatuves", font = ("MingLiU_HKSCS-ExtB", 60,"bold"))
#bilde
logo = PhotoImage(file='C:\\Users\\202-04\\Documents\\26\\Capture.png') #Dzastina path S202-8 Fēlikssa path 202-04
main.create_image(600, 450, image=logo)
#start poga 
START_POGA = PhotoImage(file='C:\\Users\\202-04\\Documents\\26\\START POGA.png')
main.create_image(600, 750, image=START_POGA)
main.create_text(600,750, text = "START", font = ("MingLiU_HKSCS-ExtB", 60,"bold"))


logs.mainloop()
