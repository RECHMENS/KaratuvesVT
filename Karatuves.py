from tkinter import * 
from tkinter import PhotoImage


vārdi = ["Orange","Apple","Banana"]


#canva un logs
logs = Tk()
logs.title("test")
main = Canvas(logs, width=1000, height=400, bg="#E6E6E6")
main.pack()

#Bildes path
image_Karātuve = PhotoImage(file="C:\\Users\\202-04\\Documents\\26\\Capture.PNG") #Dzastina path S202-8 Fēlikssa path 202-04


image_label = Label(logs, image=image_Karātuve)
image_label.pack()



# Start the Tkinter main loop
logs.mainloop()
