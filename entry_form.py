# Sophia M. Toliver, CIS 345 T TH 10:30, PE13

from tkinter import *
from tkinter import ttk
from student_classes import Student, GradStudent

window = Tk()
window.title('Student Entry Form')
window.geometry('500x650')
window.config(bg='cyan')

student_type = StringVar()
first = StringVar()
last = StringVar()
thesis = StringVar()
major = StringVar()
edit_mode = bool()
edit_index = int()

student_roster = []
major_options = ['ACC', 'BDA', 'CIS', 'SCM', 'FIN', 'MKT', 'MGT', 'COM']


def student_selection(student_chosen):
    """Executes once a radio button is selected to set student_type"""
    global student_type
    if student_chosen == 'S':
        thesis_entry['state'] = DISABLED
        student_type.set('S')
    else:
        thesis_entry['state'] = NORMAL
        student_type.set('G')


def save_student_click():
    """Executes upon clicking the Save Student button to create either
    a Student or GradStudent object and append it to the student roster
    and list_box widget"""
    global student_type, first, last, thesis, major, edit_mode, edit_index, student_box
    temp = None
    if student_type.get() == 'G':
        temp = GradStudent(thesis.get(), first.get(), last.get(), major.get())
    else:
        temp = Student(first.get(), last.get(), major.get())

    if edit_mode:
        student_roster[edit_index] = temp
        student_box.delete(edit_index)
        student_box.insert(edit_index, temp)
        edit_mode = False
    else:
        student_roster.append(temp)
        student_box.insert(END, temp)

    student_type.set('')
    first.set('')
    last.set('')
    thesis.set('')
    major.set('')


def edit_student(event):
    """Edits student entered when double clicked on in the list_box widget"""
    global student_type, first, last, thesis, major, edit_mode, edit_index, student_box
    edit_mode = True
    edit_index = student_box.curselection()[0]
    edit = student_roster[edit_index]
    if isinstance(edit, GradStudent):
        student_type.set('G')
    else:
        student_type.set('S')


# extra blank labels used for spacing
Label(window, text='', bg='cyan').grid(row=0, columnspan=4)

frame1 = Frame(window, bg='cornsilk', width=300, height=80, borderwidth=1, relief=SUNKEN)
frame1.grid(row=1, column=0, columnspan=4, sticky=N)
frame1.pack_propagate(0)

student_lbl = Label(frame1, text='Student Type', bg='cornsilk')
student_lbl.pack(anchor=W)

student = Radiobutton(frame1, bg='cornsilk', text='Student', value='S', command=lambda: student_selection('S'))
student.pack(side='left')
grad = Radiobutton(frame1, bg='cornsilk', text='Graduate Student', value='G', command=lambda: student_selection('G'))
grad.pack(side='right')

# extra blank labels used for spacing
Label(window, text='', bg='cyan').grid(row=2, columnspan=4)

fname_lbl = Label(window, background='cyan', justify=LEFT, width=15, text='First Name: ')
fname_lbl.grid(row=3, column=0)
fname_entry = Entry(window, justify=RIGHT, width=21, textvariable=first, relief=SUNKEN)
fname_entry.grid(row=3, column=1)

Label(window, text='', bg='cyan').grid(row=4, columnspan=4)

lname_lbl = Label(window, background='cyan', justify=LEFT, width=15, text='Last Name: ')
lname_lbl.grid(row=5, column=0)
lname_entry = Entry(window, justify=RIGHT, width=21, textvariable=last, relief=SUNKEN)
lname_entry.grid(row=5, column=1)

Label(window, text='', bg='cyan').grid(row=6, columnspan=4)

major_lbl = Label(window, background='cyan', justify=LEFT, width=15, text='Major: ')
major_lbl.grid(row=7, column=0)
major_box = ttk.Combobox(window, values=major_options, textvariable=major)
major_box.current(0)
major_box.grid(row=7, column=1)

Label(window, text='', bg='cyan').grid(row=8, columnspan=4)

thesis_lbl = Label(window, background='cyan', justify=LEFT, width=15, text='Thesis: ')
thesis_lbl.grid(row=9, column=0)
thesis_entry = Entry(window, justify=RIGHT, width=21, textvariable=thesis, relief=SUNKEN)
thesis_entry.grid(row=9, column=1)

Label(window, text='', bg='cyan').grid(row=10, columnspan=4)

submit = Button(window, text='Save Student', relief=RAISED, command=save_student_click)
submit.grid(row=11, column=1, sticky=E)

instructions = Label(window, bg='cyan', text='(Double-Click to Edit a Student)', justify=RIGHT)
instructions.grid(row=12, column=0)
student_box = Listbox(window, width=40)
student_box.bind('<Double-Button-1>', edit_student)
student_box.grid(row=13, column=0, columnspan=4)

window.mainloop()