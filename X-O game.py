
import tkinter as tk

root = tk.Tk()
root.title("משחק איקס עיגול")
root.configure(bg="#F5F5DC")


def check_win():
    global game_over
    for j in range(3):
        row = [buttons[j*3+x]["text"] for x in range(3)]
        if row == ["X", "X", "X"]:
            msg_won["text"] = "X המנצח הוא שחקן"
            game_over = True
        elif row == ["O", "O", "O"]:
            msg_won["text"] = "O המנצח הוא שחקן"
            game_over = True
    for j in range(3):
        col = [buttons[x*3+j]["text"] for x in range(3)]
        if col == ["X", "X", "X"]:
            msg_won["text"] = "X המנצח הוא שחקן"
            game_over = True
        elif col == ["O", "O", "O"]:
            msg_won["text"] = "O המנצח הוא שחקן"
            game_over = True
    a, b = 0, 9
    for j in range(4, 0, -2):
        dia = [buttons[x]["text"]for x in range(a, b, j)]
        if dia == ["X", "X", "X"]:
            msg_won["text"] = "X המנצח הוא שחקן"
            game_over = True
        elif dia == ["O", "O", "O"]:
            msg_won["text"] = "O המנצח הוא שחקן"
            game_over = True
        a, b = 2, 7
    if all([b["text"] != "" for b in buttons]) and not game_over:
        msg_won["text"] = "אין מנצח במשחק זה"


def click(button):
    def x_o():
        global is_x
        if button["text"] == "" and not game_over:
            if is_x:
                button["text"], button["fg"], button["bg"] = "X", "red", "#FFE0E0"
            else:
                button["text"], button["fg"], button["bg"] = "O", "green", "#E0FFE0"
            is_x = not is_x
            check_win()
    return x_o


def restart_game():
    global game_over, msg_won, button
    for button in buttons:
        button["text"], button["bg"] = "", "#F5F5DC"
    msg_won["text"] = ""
    game_over = False


is_x = True
game_over = False
buttons = []
for i in range(9):
    button = tk.Button(root, text="", bg="#F5F5DC", height=2, width=4, font=("Helvetica", 28))
    button.configure(command=click(button))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)
msg_won = tk.Label(root, text="", bg="#F5F5DC", fg="#756035", width=15, height=2, font=("Helvetica", 20))
msg_won.grid(row=4, columnspan=3)
restart_button = tk.Button(root, text="משחק חדש", bg="#756035", fg="#F5F5DC", font=("Helvetica", 10), command=restart_game)
restart_button.grid(row=5, columnspan=3)


root.mainloop()


