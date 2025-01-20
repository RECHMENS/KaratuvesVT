from tkinter import *

height = 400
width = 400

logs = Tk()
logs.title("test")
main = Canvas(logs, width=1200, height=900, bg="#E6E6E6")
main.pack()

#start

logo = PhotoImage(file='C:\\Users\\S202-8\\Documents\\26\\Capture.png')
main.create_image(100, 20, image=logo)


logs.mainloop()
