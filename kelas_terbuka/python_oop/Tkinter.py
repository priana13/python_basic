import tkinter

main_window = tkinter.Tk()

# print(main_window.__dict__)

label1 = tkinter.Label(main_window,text="label1")
label2 = tkinter.Label(main_window,text="label2")

#method positioning
label1.pack()
label2.pack()

tombol1 = tkinter.Button(main_window, text="Tombol1")
tombol2 = tkinter.Button(main_window, text="Tombol2")
#method positioning
tombol1.pack()
tombol2.pack()

# method menampilkan layar / GUI
main_window.mainloop()
