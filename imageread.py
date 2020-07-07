from tkinter import *
import pytesseract
from PIL import Image, ImageTk
root = Tk()

root.geometry('400x400')
root.minsize(400, 400)
root.maxsize(400, 400)
root.title("Image Read Application")
root.wm_iconbitmap('P:\\python\\imageread\\icon.ico')

pytesseract.pytesseract.tesseract_cmd = r"S:\\tesseract\\tesseract.exe"

img = Image.open("P:\\python\\imageread\\textImage.jpg")
output = pytesseract.image_to_string(img)
photo = ImageTk.PhotoImage(img)

image_label = Label(image=photo)
image_label.pack(pady=25)

title_label = Label(text=output)
title_label.pack()





root.mainloop()
