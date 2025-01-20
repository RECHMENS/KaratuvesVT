from tkinter import *
from tkinter import PhotoImage

vārdi = ["Orange","Apple","Banana"]

height = 400
width = 400

logs = Tk()
logs.title("test")
main = Canvas(logs, width=1000, height=400, bg="#edf2ef")
main.pack()

# Make sure the path to the image is correct
image = PhotoImage(file="C:\\Users\\S202-8\\Documents\\26\\Capture.PNG")

# To prevent the image from being garbage collected, keep a reference to it
image_label = Label(logs, image=image)
image_label.pack()

# Start the Tkinter main loop
logs.mainloop()
