from customtkinter import *
set_appearance_mode("System")
set_default_color_theme("blue")

app = CTk()
app.geometry("600x800")
app.title("Number AI")
app.resizable(0, 0)

label = CTkLabel(app, text="Draw a number", font=("Arial", 18))
label.pack()

# drown grid pixels
drown_gp = []

# canvas n to n
n = 25 * 18

# the grid k to k (grid pixels) on the canvas:
k = 25

canvas = CTkCanvas(bg="white", width=n, height=n)
canvas.pack(anchor="center")

# canvas.bind('<ButtonPress-1>', draw)
# canvas.bind('<B1-Motion>', draw)

app.mainloop()