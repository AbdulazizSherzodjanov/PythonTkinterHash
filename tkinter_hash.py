"""
21/09/2022
TKINTER :  HASHLASH DASTURI
MUALLIF : SHERZODJANOV ABDULAZIZ
TELEGRAM : @command_python404
E-MAIL : abdulazizsherzodjanov@gmail.com
"""


from tkinter import *
import hashlib

root = Tk()
root.title("Hash!")  # title
root.config(bg="black")  # background qora
root.geometry("600x700")  # oynaning razmeri
root.resizable(False, False)

"""
TEXT
"""
joylash = Text(width=40, height=5, wrap=WORD, font=('Arial', 15))
joylash.place(x=125, y=200)

"""
MD5 hashlash uchun funksiya
"""


def md5():
    global sozhash
    hashsoz = soz.get()
    hashkey = hashlib.md5()
    hashkey.update(hashsoz.encode())
    sozhash = hashkey.hexdigest()
    joylash.delete(1.0, END)
    joylash.insert(1.0, str(f"Md5 Hashlangan so'z>>>\n\n{sozhash}"))


"""
SHA1 hashlash uchun funksiya
"""


def sha1():
    global word
    hashsha1 = soz.get()
    hashshak1ey = hashlib.sha1()
    hashshak1ey.update(hashsha1.encode())
    word = hashshak1ey.hexdigest()
    joylash.delete(1.0, END)
    joylash.insert(1.0, str(f"Sha1 Hashlangan so'z>>>\n\n{word}"))


"""
SHA256 hashlash uchun funksiya
"""


def sha256():
    global gap
    hashsha1 = soz.get()
    hashshak1ey1 = hashlib.sha256()
    hashshak1ey1.update(hashsha1.encode())
    gap = hashshak1ey1.hexdigest()
    joylash.delete(1.0, END)
    joylash.insert(1.0, str(f"Sha256 Hashlangan so'z>>>\n\n{gap}"))


def sha384():
    global p
    hashsha12 = soz.get()
    hashshak1ey12 = hashlib.sha384()
    hashshak1ey12.update(hashsha12.encode())
    p = hashshak1ey12.hexdigest()
    joylash.delete(1.0, END)
    joylash.insert(1.0, str(f"Sha384 Hashlangan so'z>>>\n\n{p}"))


def clear():
    joylash.delete(1.0, END)


"""
LABEL
"""
soztxt = Label(text="So'z Kiriting", bg="black", fg="green", font=("Arial", 15))
soztxt.place(x=10, y=80)

"""ENTRY"""
soz = Entry(width=28, font=('Arial', 15))
soz.place(x=130, y=80)

"""
TUGMALAR
"""
hashtugmamd5 = Button(text="Md5", bg="black", fg="blue", font=('Arial', 15), command=md5)
hashtugmamd5.place(x=10, y=140)

hashsh1 = Button(text="Sha1", bg="black", fg="blue", font=("Arial", 15), command=sha1)
hashsh1.place(x=80, y=140)

hashsh256 = Button(text="Sha256", bg="black", fg="blue", font=("Arial", 15), command=sha256)
hashsh256.place(x=160, y=140)

sha384k = Button(text="Sha384", bg="black", fg="blue", font=("Arial", 15), command=sha384)
sha384k.place(x=265, y=140)

clearb = Button(text="Tozala", bg="black", fg="blue", font=("Arial", 15), command=clear)
clearb.place(x=370, y=140)
root.mainloop()
