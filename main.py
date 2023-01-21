from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 








# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("The Pomodoro app")
window.minsize(width=300, height=100)
window.config(padx=80, pady=20, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)

# Label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)
timer_label.config(padx=5, pady=5)

check_label = Label(text="✓", font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=4, column=1)
check_label.config(padx=10, pady=10)

# Start and reset Buttons
start_button = Button(text="Star", font=(FONT_NAME, 10, "bold"), highlightthickness=0) #, #command=button_clicked)
start_button.grid(row=4, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0) #, #command=button_clicked)
reset_button.grid(row=4, column=5)

window.mainloop()
