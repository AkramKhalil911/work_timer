import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
break_time = False
time = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global time, reps, break_time
    timer_title.config(text="Timer", fg=GREEN)
    window.after_cancel(time)
    time = canvas.itemconfig(timer, text=f"00:00")
    reps = 0
    break_time = False
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, break_time

    reps += 1
    if reps % 8 == 0 and break_time == True:
        count_down(LONG_BREAK_MIN * 60)
        break_time = False
        timer_title.config(text="Long Break", fg=RED)
    elif break_time == True and reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        break_time = False
        timer_title.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        break_time = True
        timer_title.config(text="Work Time", fg=GREEN)


# ------------------,---------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(input):
    global time
    min = math.floor(input / 60)
    sec = input % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer, text=f"{min}:{sec}")
    if input > 0:
        time = window.after(1000,count_down, input - 1)
    else:
        start_timer()
        marks = ""
        reps_work = math.floor(reps/2)
        for mark in range(reps_work):
            marks += "✓"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

timer_title = tkinter.Label(text="Timer", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN)
timer_title.grid(column=1, row=0)

canvas = tkinter.Canvas(width=203, height=225, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
timer = canvas.create_text(103,132, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="start", width=10, font=(FONT_NAME, 14), command=start_timer)
start_button.grid(column=0, row=2)

end_button = tkinter.Button(text="reset", width=10, font=(FONT_NAME, 14), command=reset_timer)
end_button.grid(column=2, row=2)

check_mark = tkinter.Label(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)


window.mainloop()