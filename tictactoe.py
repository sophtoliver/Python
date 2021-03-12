from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Tic Tac Toe')

playerX = True
count = int()


def button_chosen(button):
    """Handles all button clicks: disables buttons, marks sports,
    tracks turn count, and calls check for winner"""
    global count, playerX
    if button['text'] == ' ' and playerX is True:
        button['text'] = 'X'
        playerX = False
    elif button['text'] == ' ' and playerX is False:
        button['text'] = 'O'
        playerX = True

    button['state'] = DISABLED
    count += 1
    check_for_winner()


def check_for_winner():
    """Determines when either player 1 or player 2 has won the game
    in any of the possible winning combinations"""
    if count >= 9:
        messagebox.showinfo(title='Draw', message='Cats Game')
        clear_board()

    winnings = [[one, two, three], [four, five, six], [seven, eight, nine], [one, five, nine],
                [three, five, seven], [one, four, seven], [three, six, nine], [two, five, eight]]
    x = 0
    y = 1
    z = 2
    for win in winnings:
        if win[x]['text'] == 'X' and win[y]['text'] == 'X' and win[z]['text'] == 'X':
            messagebox.showinfo(title='Winner', message='Player X Won!')
            clear_board()
            break

    for win in winnings:
        if win[x]['text'] == 'O' and win[y]['text'] == 'O' and win[z]['text'] == 'O':
            messagebox.showinfo(title='Winner', message='Player O Won!')
            clear_board()
            break


def clear_board():
    """Resets the game back: clears the board, enables buttons,
    reset back to player 1's turn and turn count to 0"""
    global count, playerX
    count = 0
    playerX = True
    buttons = [one, two, three, four, five, six, seven, eight, nine]
    for x in buttons:
        x.config(text=' ')
        x.config(state='normal')


button = StringVar()

one = Button(window, text=" ", font=20, height=10, width=20, command=lambda: button_chosen(one))
one.grid(row=0, column=0)

two = Button(window, text=" ", height=10, width=20, command=lambda: button_chosen(two))
two.grid(row=0, column=1)

three = Button(window, text=" ", height=10, width=20, command=lambda: button_chosen(three))
three.grid(row=0, column=2)

four = Button(window, text=" ", height=10, width=20, command=lambda: button_chosen(four))
four.grid(row=1, column=0)

five = Button(window, text=" ", height=10, width=20, command=lambda: button_chosen(five))
five.grid(row=1, column=1)

six = Button(window, text=" ", height=10, width=20, command=lambda: button_chosen(six))
six.grid(row=1, column=2)

seven = Button(window, text=" ", height=10, width=20, command=lambda: button_chosen(seven))
seven.grid(row=2, column=0)

eight = Button(window, text=" ", height=10, width=20, command=lambda: button_chosen(eight))
eight.grid(row=2, column=1)

nine = Button(window, text=" ", height=10, width=20, command=lambda: button_chosen(nine))
nine.grid(row=2, column=2)

window.mainloop()
