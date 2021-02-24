# Sophia M. Toliver, CIS 345 TTH 10:30, A8

from socket import *
from tkinter import *
from threading import Thread
from tkinter import messagebox

window = Tk()
window.geometry('350x120')
window.title('CIS IM Client')
window.config(background='lightgray')

server = StringVar()
name = StringVar()
message = StringVar()
sock = socket(AF_INET, SOCK_STREAM)

server.set('')
name.set('')
message.set('')


def valid_keys_for_server(event):
    """When keys are pressed in the server name entry box, only the following valid keys will show up"""
    global server, server_entry
    valid_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'period', '.', 'space', ' ',
                  'BackSpace', '', 'Left', '\b', 'Right']
    if event.keysym not in valid_keys:
        return "break"
    else:
        pass


def open_window():
    """When the connect button is pressed, the chat window appears"""
    window.geometry('350x500')
    connect_button['text'] = 'Disconnect'
    connect_button['bg'] = 'gold'
    connect_button['command'] = 'disconnect'
    chat_frame.pack(pady=10)
    chat_frame.pack_propagate(0)
    messages_frame.pack(pady=10, padx=10, ipady=5, ipadx=5)
    messages.pack(side=LEFT, fill=BOTH, padx=2, pady=2)
    scrollbar.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=messages.yview)

    message_entry = Entry(chat_frame, bg='white', textvariable=message, width=25)
    message_entry.pack(side=LEFT, padx=15)

    send = Button(chat_frame, bg='gold', relief=RAISED, text='Send', command=send_message)
    send.pack(side=LEFT, padx=5, ipady=3, ipadx=3)


def connect():
    """Creates a client socket and connects it to the server socket"""
    global server, name, connect_button, window, chat_frame, sock
    if len(server.get()) > 6 and len(name.get()) >= 1:
        try:
            host = server.get()
            addr = (host, 49000)
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect(addr)
            screen_name_reformatted = name.get().capitalize()
            sock.send(screen_name_reformatted.encode())
            # join_msg = f'{name.get()} joined chat...'
            # messages.insert(END, join_msg)
        except Exception as ex:
            print(ex)
            sock.close()
            sock = None
        else:
            thread_to_receive = Thread(target=receive, daemon=True)
            thread_to_receive.start()
            open_window()
    else:
        messagebox.showinfo(title="Error connecting to server.", message="You must enter: \n - a valid Server IP "
                                                                         "(ex: 127.0.0.1) \n - a valid Screen Name "
                                                                         "(ex: Sophia)")


def disconnect():
    """If a client sends the exit command [Q], it closes their client socket"""
    global sock, server, name, connect_button, window, chat_frame
    try:
        sock.send('[Q]'.encode())
    except Exception as ex:
        print(ex)
        pass
    finally:
        sock.close()
        sock = None

    connect_button['text'] = 'Connect'
    connect_button['bg'] = 'SystemButtonFace'
    connect_button['command'] = 'connect'
    chat_frame.pack_forget()
    window.geometry('350x120')
    server.set('')
    name.set('')


def receive():
    """Recieves and decodes a message sent from a client"""
    global sock, name
    while True:
        try:
            msg = sock.recv(1024)
        except OSError:
            msg = None
            break

        if msg is None:
            disconnect()
            break
        else:
            messages.insert(END, msg.decode())


def send_message():
    """Retrieves message wrote in message entry box, encodes it and sends it to the server"""
    global sock, message
    entered_msg = message.get()
    if entered_msg == '[Q]':
        disconnect()
    elif len(entered_msg) > 0:
        try:
            sock.send(entered_msg.encode())
        except OSError:
            disconnect()
        message.set('')


def close_window():
    """Will be called if the user wants to close the GUI application"""
    global sock
    if sock:
        disconnect()

    window.quit()


server_and_name_frame = Frame(window, bg='lightgray')
server_and_name_frame.pack(pady=10)

server_lbl = Label(server_and_name_frame, bg='lightgray', text='Server IP:      ')
server_lbl.grid(row=0, column=0)
server_entry = Entry(server_and_name_frame, bg='white', textvariable=server, width=25)
server_entry.grid(row=0, column=1)
server_entry.bind("<Key>", valid_keys_for_server)

name_lbl = Label(server_and_name_frame, bg='lightgray', text='Screen Name:')
name_lbl.grid(row=1, column=0)
name_entry = Entry(server_and_name_frame, bg='white', textvariable=name, width=25)
name_entry.grid(row=1, column=1)

connect_button = Button(window, bg='white', text='Connect', width=37, command=connect)
connect_button.pack(ipady=5, padx=5)

chat_frame = Frame(window, bg='maroon', width=335, height=370)
messages_frame = Frame(chat_frame, bg='white', height=200)
scrollbar = Scrollbar(messages_frame)
messages = Listbox(messages_frame, bg='white', yscrollcommand=scrollbar.set,
                   width=33, height=17, selectbackground='white')

window.protocol("WM_DELETE_WINDOW", close_window)
window.mainloop()
