# Sophia M. Toliver, CIS 345 10:30 T TH, Project

import csv
from tkinter import *
# messageboxes only used for exception handling
from tkinter import messagebox
from difflib import get_close_matches
import random
from PIL import Image, ImageTk


class Questions:

    def __init__(self, question_text='', option1='', option2='', option3='', option4='',
                 correct_feedback='', incorrect_feedback='', answer='', point_value=''):
        self.question_text = question_text
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct_feedback = correct_feedback
        self.incorrect_feedback = incorrect_feedback
        self.answer = answer
        self.point_value = point_value

    @property
    def question_text(self):
        return self.__question_text

    @question_text.setter
    def question_text(self, new):
        if new == '' or new == ' ':
            self.__question_text = 'Unknown'
        else:
            self.__question_text = new

    @property
    def option1(self):
        return self.__option1

    @option1.setter
    def option1(self, new):
        if new == '' or new == ' ':
            self.__option1 = 'Unknown'
        else:
            self.__option1 = new

    @property
    def option2(self):
        return self.__option2

    @option2.setter
    def option2(self, new):
        if new == '' or new == ' ':
            self.__option2 = 'Unknown'
        else:
            self.__option2 = new

    @property
    def option3(self):
        return self.__option3

    @option3.setter
    def option3(self, new):
        if new == '' or new == ' ':
            self.__option3 = 'Unknown'
        else:
            self.__option3 = new

    @property
    def option4(self):
        return self.__option4

    @option4.setter
    def option4(self, new):
        if new == '' or new == ' ':
            self.__option4 = 'Unknown'
        else:
            self.__option4 = new

    @property
    def correct_feedback(self):
        return self.__correct_feedback

    @correct_feedback.setter
    def correct_feedback(self, new):
        if new == '' or new == ' ':
            self.__correct_feedback = 'Unknown'
        else:
            self.__correct_feedback = new

    @property
    def incorrect_feedback(self):
        return self.__incorrect_feedback

    @incorrect_feedback.setter
    def incorrect_feedback(self, new):
        if new == '' or new == ' ':
            self.__incorrect_feedback = 'Unknown'
        else:
            self.__incorrect_feedback = new

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, new):
        answer_options = [self.option1, self.option2, self.option3, self.option4]
        if new in answer_options:
            self.__answer = new
        else:
            self.__answer = 'Unknown'

    @property
    def point_value(self):
        return self.__point_value

    @point_value.setter
    def point_value(self, new):
        num = int(new)
        if 0 < num < 4:
            self.__point_value = new

        else:
            self.__point_value = '1'

    def __str__(self):
        return f'{self.__question_text}, {self.__option1}, {self.__option2}, {self.__option3}, {self.__option4},' \
               f'{self.__correct_feedback}, {self.__incorrect_feedback}, {self.__answer}, {self.__point_value}'

    # create a @classmethod for adding questions


# I am very unsure with putting variable names in camel case
# Why did you originally teach us to do snake_case if you want camel case now?
question_pool = []
editMode = bool()
editIndex = int()
widgets_currently_in_window = list()

# I went to put my functions and methods in pascal case and it
# gave me a pep8 error saying they must be lowercase
# so I left them as snake_case


def exit_window():
    global window
    save_file()
    window.destroy()


def clear_form():
    """Sets all StringVar()'s back to an empty string"""
    global text, selection1, selection2, selection3, selection4, positive_feedback, negative_feedback, \
        correct_answer, points, user_answer, feedback
    text.set('')
    selection1.set('')
    selection2.set('')
    selection3.set('')
    selection4.set('')
    positive_feedback.set('')
    negative_feedback.set('')
    correct_answer.set('')
    points.set('')
    user_answer.set('')
    feedback.set('')


def forget_widgets_in_window():
    """Clears the widgets that are currently in the window
    so that the new widgets of a newly selected menu item can appear properly"""
    for widget in widgets_currently_in_window:
        widget.pack_forget()


def read_file():
    """Reads csv file that holds the questions' data"""
    global text, selection1, selection2, selection3, selection4, \
        positive_feedback, negative_feedback, correct_answer, points, question_pool
    try:
        with open('questions.csv', encoding='utf-8-sig') as fp:
            reader = csv.reader(fp)
            for row in reader:
                text.set(row[0])
                selection1.set(row[1])
                selection2.set(row[2])
                selection3.set(row[3])
                selection4.set(row[4])
                positive_feedback.set(row[5])
                negative_feedback.set(row[6])
                correct_answer.set(row[7])
                points.set(row[8])
                temp = Questions(text.get(), selection1.get(), selection2.get(), selection3.get(),
                                 selection4.get(), positive_feedback.get(), negative_feedback.get(),
                                 correct_answer.get(), points.get())
                question_pool.append(temp)
    except FileNotFoundError:
        messagebox.showwarning(title='Error', message='Error Loading the Questions.')


def home():
    global widgets_currently_in_window
    forget_widgets_in_window()
    welcome_message.pack(pady=10)
    home_page_message.config(text='Below is the pool of questions that will be used to test your knowledge. '
                                  'Are you ready to play?')
    home_page_message.config(font=('Courier', 10))
    home_page_message.pack()
    application_frame.pack(pady=20)
    application_frame.pack_propagate(0)
    view_questions_listbox.pack(padx=20, pady=20)
    vertical_scrollbar_for_questions_listbox.config(command=view_questions_listbox.yview)
    # vertical_scrollbar.pack()
    horizontal_scrollbar_for_questions_listbox.config(command=view_questions_listbox.xview)
    # horizontal_scrollbar.pack()

    # maintain a list of widgets used in each function so that they can be forgotten
    # when no longer utilizing that function
    widgets_currently_in_window = [application_frame, welcome_message, view_questions_listbox, home_page_message,
                                   vertical_scrollbar_for_questions_listbox, horizontal_scrollbar_for_questions_listbox]

    view_questions()


def instructions():
    """Presents the user the instructions to manage the quiz management system"""
    global widgets_currently_in_window
    forget_widgets_in_window()
    application_frame.pack(pady=20)
    application_frame.pack_propagate(0)
    instructions_label = Label(application_frame, bg='lightyellow', text='Instructions',
                               font=('Courier', 18), borderwidth=3, relief=RAISED)
    instructions_label.pack(pady=25, ipady=5, ipadx=5)
    instructions_message = Label(application_frame, text='In this quiz management system, you can navigate the \nmenu '
                                                         'bar to edit, add, or delete questions. You can also '
                                                         '\nsearch through and view the questions that are already '
                                                         'present. \n\nWhen you are ready to play the game, \ngo '
                                                         'to the "Quiz" drop down menu, and hit "Take a Quiz." '
                                                         '\n\nGood luck and happy playing!', bg='lightyellow',
                                 font=('Courier', 10), borderwidth=3, relief=RAISED)
    instructions_message.pack(pady=10, ipadx=5, ipady=5, padx=10)
    widgets_currently_in_window = [application_frame, instructions_message, instructions_label]


def view_questions_and_details():
    """Shows user the questions, the questions' selections, feedback, answers, and point value"""
    global question_pool, widgets_currently_in_window
    forget_widgets_in_window()
    # clear listboxes of previous information
    question_listbox_for_viewing_question_information.delete(0, END)
    details_listbox.delete(0, END)
    welcome_message.config(text='Double click one of the questions to view its details.')
    welcome_message.config(font=('Courier', 12))
    welcome_message.pack(pady=10)
    home_page_message.config(text='Scroll left and right for line continuation.')
    home_page_message.config(font=('Courier', 12))
    home_page_message.pack(pady=10)
    questions_to_view_frame.pack(ipadx=10, pady=5, padx=20, anchor=W, side=LEFT)
    questions_to_view_frame.pack_propagate(0)
    question_listbox_for_viewing_question_information.pack(padx=20, pady=20)
    # show questions in the listbox
    if len(question_pool) >= 1:
        for info in question_pool:
            question_listbox_for_viewing_question_information.insert(END, info.question_text)
    else:
        try:
            read_file()
        except (FileNotFoundError, IndexError):
            messagebox.showwarning(title='Error!', message='Unable to retrieve questions!')
        else:
            for info in question_pool:
                question_listbox_for_viewing_question_information.insert(END, info.question_text)
    question_listbox_for_viewing_question_information.bind('<Double-Button-1>', view_details)
    view_details_frame.pack(ipadx=5, pady=5, padx=20, anchor=E, side=LEFT)
    view_details_frame.pack_propagate(0)
    details_listbox.pack(padx=20, pady=20)

    widgets_currently_in_window = [home_page_message, welcome_message, questions_to_view_frame, view_details_frame]


def view_details(event):
    """When a question in the 'View Questions' menu is double clicked on, it's details appear in the adjacent listbox"""
    global text, selection1, selection2, selection3, selection4, positive_feedback, negative_feedback, correct_answer, \
        points, editIndex, question_pool, details_listbox
    details_listbox.delete(0, END)
    if len(question_pool) == 0:
        read_file()
    # set each entry to the selected question's variables
    editIndex = question_listbox_for_viewing_question_information.curselection()[0]
    edit = question_pool[editIndex]
    insert_into_details_listbox = ['QUESTION:', edit.question_text, 'OPTION A:', edit.option1, 'OPTION B:',
                                   edit.option2, 'OPTION C:', edit.option3, 'OPTION D:', edit.option4,
                                   'POSITIVE FEEDBACK:', edit.correct_feedback, 'NEGATIVE FEEDBACK:',
                                   edit.incorrect_feedback, 'CORRECT ANSWER:', edit.answer, 'POINT VALUE:',
                                   edit.point_value]
    for info in insert_into_details_listbox:
        details_listbox.insert(END, info)


def view_questions():
    """Shows the user the questions upon opening the quiz management system"""
    global question_pool
    view_questions_listbox.delete(0, END)
    if len(question_pool) >= 1:
        for info in question_pool:
            view_questions_listbox.insert(END, info.question_text)
    else:
        try:
            read_file()
        except (FileNotFoundError, IndexError):
            messagebox.showwarning(title='Error!', message='Unable to retrieve questions!')
        else:
            for info in question_pool:
                view_questions_listbox.insert(END, info.question_text)


def search_interface():
    """Frame and widgets used to allow user to search for keywords within the questions"""
    global widgets_currently_in_window
    forget_widgets_in_window()
    search_through_questions_frame.pack(ipadx=5, pady=5, padx=20, anchor=CENTER)
    search_through_questions_frame.pack_propagate(0)
    # empty labels used for formatting
    empty_label_for_formatting_1 = Label(search_through_questions_frame, text='', bg='lightpink')
    empty_label_for_formatting_1.grid(row=0, column=0, columnspan=3)
    instructions_label = Label(search_through_questions_frame, text='  Enter a keyword you would like to search for.',
                               bg='lightpink', font='Courier')
    instructions_label.grid(row=1, column=0, columnspan=2)
    empty_label_for_formatting_2 = Label(search_through_questions_frame, text='', bg='lightpink')
    empty_label_for_formatting_2.grid(row=2, column=0, columnspan=3)

    search_label = Label(search_through_questions_frame, background='lightpink', justify=LEFT,
                         width=15, text='Search: ', font='Courier')
    search_label.grid(row=3, column=0)
    search_entry = Entry(search_through_questions_frame, justify=RIGHT, width=21, textvariable=keyword, relief=SUNKEN)
    search_entry.grid(row=3, column=1)
    empty_label_for_formatting_3 = Label(search_through_questions_frame, text='', bg='lightpink')
    empty_label_for_formatting_3.grid(row=4, column=0, columnspan=3)
    go_button_for_searching = Button(search_through_questions_frame, text='Search', background='lightpink',
                                     command=search_through_questions, width=10, height=2)
    go_button_for_searching.grid(row=5, column=1)
    empty_label_for_formatting_4 = Label(search_through_questions_frame, text='', bg='lightpink')
    empty_label_for_formatting_4.grid(row=6, column=0, columnspan=3)
    search_results_frame.pack(ipadx=5, pady=5, padx=20, anchor=CENTER)
    message_above_search_results = Label(search_results_frame,
                                         text='Questions that contain the keyword provided or something similar: ',
                                         bg='lightpink', font=('Courier', 10))
    message_above_search_results.pack(anchor=W, padx=20, pady=13)
    search_results_listbox.pack(padx=20, pady=10)
    widgets_currently_in_window = [search_through_questions_frame, search_results_frame]


def search_through_questions():
    """Executes when 'Go' button is pressed in the search interface
    - takes the keyword given by the user and finds if it's present in any of the questions"""
    global keyword, question_pool
    # clears list box if there's previous info in it
    search_results_listbox.delete(0, END)
    if len(question_pool) == 0:
        read_file()
    results_from_search = []
    i = 0
    while i < len(question_pool):
        match = get_close_matches(keyword.get(), question_pool[i].question_text.casefold(), n=10)
        if keyword.get().casefold() in question_pool[i].question_text.casefold():
            results_from_search.append(i)
        elif match:
            results_from_search.append(i)
        i += 1

    # exception handling
    if keyword.get() == '':
        messagebox.showwarning(title='Entry Not Allowed', message="An empty keyword was entered.")
    elif len(results_from_search) < 1:
        messagebox.showwarning(title='Error', message='No results were found. Please try again!')
    else:
        for result in results_from_search:
            search_results_listbox.insert(END, question_pool[result].question_text)


def edit_questions_interface():
    """Creates an interactive interface for the user to edit questions"""
    global text, selection1, selection2, selection3, selection4, positive_feedback, negative_feedback, \
        correct_answer, points, editIndex, editMode, widgets_currently_in_window, question_pool
    clear_form()
    forget_widgets_in_window()
    questions_to_edit_frame.pack(ipadx=10, pady=5, padx=20, anchor=W, side=LEFT)
    questions_to_edit_frame.pack_propagate(0)
    # vertical_scrollbar_for_edit_questions_interface = Scrollbar(questions_to_edit_frame, orient=VERTICAL)
    # horizontal_scrollbar_for_edit_questions_interface = Scrollbar(questions_to_edit_frame, orient=HORIZONTAL)
    question_listbox_for_editing_question_information.pack(padx=20, pady=20)
    question_listbox_for_editing_question_information.delete(0, END)
    question_listbox_for_editing_question_information.bind('<Double-Button-1>', edit_question)
    # vertical_scrollbar_for_edit_questions_interface.pack()
    # horizontal_scrollbar_for_edit_questions_interface.pack()
    if len(question_pool) == 0:
        try:
            read_file()
        except FileNotFoundError:
            messagebox.showerror(title='Error!', message='Unable to retrieve questions!')
        else:
            for info in question_pool:
                question_listbox_for_editing_question_information.insert(END, info)
    else:
        for info in question_pool:
            question_listbox_for_editing_question_information.insert(END, info)
    edit_questions_frame.pack(ipadx=5, pady=5, padx=20, anchor=E, side=LEFT)
    edit_questions_frame.pack_propagate(0)
    # empty labels used for formatting
    empty_label_for_formatting_1 = Label(edit_questions_frame, text='', bg='lightpink')
    empty_label_for_formatting_1.grid(row=0, column=0, columnspan=3)
    instructions_label = Label(edit_questions_frame, text='  Double Click One of the Questions to Edit/ Delete',
                               bg='lightpink', font=('Arial', 10))
    instructions_label.grid(row=1, column=0, columnspan=2)
    empty_label_for_formatting_2 = Label(edit_questions_frame, text='', bg='lightpink')
    empty_label_for_formatting_2.grid(row=2, column=0, columnspan=3)

    question_label_for_editing = Label(edit_questions_frame, background='lightpink', justify=LEFT,
                                       width=15, text='Question: ', font=('Arial', 10))
    question_label_for_editing.grid(row=3, column=0, ipadx=20)
    question_entry = Entry(edit_questions_frame, justify=RIGHT, width=21, textvariable=text, relief=SUNKEN)
    question_entry.grid(row=3, column=1)

    selection1_label = Label(edit_questions_frame, background='lightpink', justify=LEFT,
                             width=15, text='Option 1: ', font=('Arial', 10))
    selection1_label.grid(row=4, column=0)
    selection1_entry = Entry(edit_questions_frame, justify=RIGHT, width=21, textvariable=selection1, relief=SUNKEN)
    selection1_entry.grid(row=4, column=1)

    selection2_label = Label(edit_questions_frame, background='lightpink', justify=LEFT,
                             width=15, text='Option 2: ', font=('Arial', 10))
    selection2_label.grid(row=5, column=0)
    selection2_entry = Entry(edit_questions_frame, justify=RIGHT, width=21, textvariable=selection2, relief=SUNKEN)
    selection2_entry.grid(row=5, column=1)

    selection3_label = Label(edit_questions_frame, background='lightpink', justify=LEFT,
                             width=15, text='Option 3: ', font=('Arial', 10))
    selection3_label.grid(row=6, column=0)
    selection3_entry = Entry(edit_questions_frame, justify=RIGHT, width=21, textvariable=selection3, relief=SUNKEN)
    selection3_entry.grid(row=6, column=1)

    selection4_label = Label(edit_questions_frame, background='lightpink', justify=LEFT,
                             width=15, text='Option 4: ', font=('Arial', 10))
    selection4_label.grid(row=7, column=0)
    selection4_entry = Entry(edit_questions_frame, justify=RIGHT, width=21, textvariable=selection4, relief=SUNKEN)
    selection4_entry.grid(row=7, column=1)

    positive_feedback_label = Label(edit_questions_frame, background='lightpink', justify=LEFT,
                                    width=15, text='Positive Feedback: ', font=('Arial', 10))
    positive_feedback_label.grid(row=8, column=0)
    positive_feedback_entry = Entry(edit_questions_frame, justify=RIGHT, width=21,
                                    textvariable=positive_feedback, relief=SUNKEN)
    positive_feedback_entry.grid(row=8, column=1)

    negative_feedback_label = Label(edit_questions_frame, background='lightpink', justify=LEFT,
                                    width=15, text='Negative Feedback: ', font=('Arial', 10))
    negative_feedback_label.grid(row=9, column=0)
    negative_feedback_entry = Entry(edit_questions_frame, justify=RIGHT, width=21,
                                    textvariable=negative_feedback, relief=SUNKEN)
    negative_feedback_entry.grid(row=9, column=1)

    answer_label = Label(edit_questions_frame, background='lightpink', justify=LEFT,
                         width=15, text='Correct Answer: ', font=('Arial', 10))
    answer_label.grid(row=10, column=0)
    correct_answer_entry = Entry(edit_questions_frame, justify=RIGHT, width=21,
                                 textvariable=correct_answer, relief=SUNKEN)
    correct_answer_entry.grid(row=10, column=1)

    point_value_label_for_editing = Label(edit_questions_frame, background='lightpink', justify=LEFT,
                                          width=15, text='Point Value: ', font=('Arial', 10))
    point_value_label_for_editing.grid(row=11, column=0)
    point_value_entry = Entry(edit_questions_frame, justify=RIGHT, width=21, textvariable=points, relief=SUNKEN)
    point_value_entry.grid(row=11, column=1)

    empty_label_for_formatting_3 = Label(edit_questions_frame, text='', bg='lightpink')
    empty_label_for_formatting_3.grid(row=12, column=0, columnspan=3)

    submit_edit_to_question_button = Button(edit_questions_frame, background='lightpink', text='Save Question Data',
                                            font=('Arial', 10), relief=RAISED, command=save_question)
    submit_edit_to_question_button.grid(row=13, column=1)

    delete_question_button = Button(edit_questions_frame, background='lightpink', text='Delete Question',
                                    font=('Arial', 10), relief=RAISED, command=delete_question)
    delete_question_button.grid(row=13, column=0)

    empty_label_for_formatting_4 = Label(edit_questions_frame, text=' ', bg='lightpink')
    empty_label_for_formatting_4.grid(row=14, column=0, columnspan=3)
    widgets_currently_in_window = [questions_to_edit_frame, edit_questions_frame]


def edit_question(event):
    """Sets the user entry boxes with what the user selected from the question list box"""
    global text, selection1, selection2, selection3, selection4, positive_feedback, negative_feedback, correct_answer, \
        points, editMode, editIndex, question_pool
    editMode = True
    empty_label_for_formatting_5.grid(row=15, column=0, columnspan=3)
    delete_status['text'] = ''
    if len(question_pool) == 0:
        read_file()
    # set each entry to the selected question's variables
    editIndex = question_listbox_for_editing_question_information.curselection()[0]
    edit = question_pool[editIndex]
    text.set(edit.question_text)
    selection1.set(edit.option1)
    selection2.set(edit.option2)
    selection3.set(edit.option3)
    selection4.set(edit.option4)
    positive_feedback.set(edit.correct_feedback)
    negative_feedback.set(edit.incorrect_feedback)
    correct_answer.set(edit.answer)
    points.set(edit.point_value)


def save_question():
    """Creates a Question object to edit the question chosen by the user that is currently in the system"""
    global text, selection1, selection2, selection3, selection4, positive_feedback, negative_feedback, correct_answer, \
        points, editMode, editIndex, question_pool, question_listbox_for_editing_question_information
    new = Questions(text.get(), selection1.get(), selection2.get(), selection3.get(), selection4.get(),
                    positive_feedback.get(), negative_feedback.get(), correct_answer.get(), points.get())
    if editMode:
        question_pool[editIndex] = new
        question_listbox_for_editing_question_information.delete(editIndex)
        question_listbox_for_editing_question_information.insert(editIndex, new)
        editMode = False
        messagebox.showinfo(title='Success', message='Edited Question was Successfully Saved')

    clear_form()
    save_file()


def save_file():
    """Saves the list of questions and all details to the csv file"""
    global question_pool

    try:
        with open('questions.csv', 'w', newline='', encoding='utf-8-sig') as filename:
            writer = csv.writer(filename)
            if len(question_pool) == 0:
                read_file()
                for question in question_pool:
                    row = [question.question_text, question.option1, question.option2, question.option3,
                           question.option4, question.correct_feedback, question.incorrect_feedback,
                           question.answer, question.point_value]
                    writer.writerow(row)
            else:
                for question in question_pool:
                    row = [question.question_text, question.option1, question.option2, question.option3,
                           question.option4, question.correct_feedback, question.incorrect_feedback,
                           question.answer, question.point_value]
                    writer.writerow(row)

    except FileNotFoundError:
        messagebox.showerror(title='Error', message='Error saving questions to file.')


def add_interface():
    """Takes user entries to create a Question object and add a new question to the pool"""
    global widgets_currently_in_window, editMode
    clear_form()
    forget_widgets_in_window()
    add_question_frame.pack(ipadx=5, pady=5, padx=20, anchor=CENTER)
    add_question_frame.pack_propagate(0)
    # empty labels used for formatting
    empty_label_for_formatting_1 = Label(add_question_frame, text='', bg='lightpink')
    empty_label_for_formatting_1.grid(row=0, column=0, columnspan=3)
    instructions_label = Label(add_question_frame,
                               text='  Fill out the form below to add a new question to the quiz system.',
                               bg='lightpink', font=('Arial', 15))
    instructions_label.grid(row=1, column=0, columnspan=2)
    empty_label_for_formatting_2 = Label(add_question_frame, text='', bg='lightpink')
    empty_label_for_formatting_2.grid(row=2, column=0, columnspan=3)

    question_label_for_adding = Label(add_question_frame, background='lightpink', justify=LEFT,
                                      width=20, text='Question: ', font=('Arial', 15))
    question_label_for_adding.grid(row=3, column=0)
    question_entry = Entry(add_question_frame, justify=RIGHT, width=21, textvariable=text, relief=SUNKEN)
    question_entry.grid(row=3, column=1)

    selection1_label = Label(add_question_frame, background='lightpink', justify=LEFT,
                             width=20, text='Option 1: ', font=('Arial', 15))
    selection1_label.grid(row=4, column=0)
    selection1_entry = Entry(add_question_frame, justify=RIGHT, width=21, textvariable=selection1, relief=SUNKEN)
    selection1_entry.grid(row=4, column=1)

    selection2_label = Label(add_question_frame, background='lightpink', justify=LEFT,
                             width=20, text='Option 2: ', font=('Arial', 15))
    selection2_label.grid(row=5, column=0)
    selection2_entry = Entry(add_question_frame, justify=RIGHT, width=21, textvariable=selection2, relief=SUNKEN)
    selection2_entry.grid(row=5, column=1)

    selection3_label = Label(add_question_frame, background='lightpink', justify=LEFT,
                             width=20, text='Option 3: ', font=('Arial', 15))
    selection3_label.grid(row=6, column=0)
    selection3_entry = Entry(add_question_frame, justify=RIGHT, width=21, textvariable=selection3, relief=SUNKEN)
    selection3_entry.grid(row=6, column=1)

    selection4_label = Label(add_question_frame, background='lightpink', justify=LEFT,
                             width=20, text='Option 4: ', font=('Arial', 15))
    selection4_label.grid(row=7, column=0)
    selection4_entry = Entry(add_question_frame, justify=RIGHT, width=21, textvariable=selection4, relief=SUNKEN)
    selection4_entry.grid(row=7, column=1)

    positive_feedback_label = Label(add_question_frame, background='lightpink', justify=LEFT,
                                    width=20, text='Positive Feedback: ', font=('Arial', 15))
    positive_feedback_label.grid(row=8, column=0)
    positive_feedback_entry = Entry(add_question_frame, justify=RIGHT, width=21,
                                    textvariable=positive_feedback, relief=SUNKEN)
    positive_feedback_entry.grid(row=8, column=1)

    negative_feedback_label = Label(add_question_frame, background='lightpink', justify=LEFT,
                                    width=20, text='Negative Feedback: ', font=('Arial', 15))
    negative_feedback_label.grid(row=9, column=0)
    negative_feedback_entry = Entry(add_question_frame, justify=RIGHT, width=21,
                                    textvariable=negative_feedback, relief=SUNKEN)
    negative_feedback_entry.grid(row=9, column=1)

    answer_label = Label(add_question_frame, background='lightpink', justify=LEFT,
                         width=20, text='Correct Answer: ', font=('Arial', 15))
    answer_label.grid(row=10, column=0)
    correct_answer_entry = Entry(add_question_frame, justify=RIGHT, width=21,
                                 textvariable=correct_answer, relief=SUNKEN)
    correct_answer_entry.grid(row=10, column=1)

    point_value_label_for_adding = Label(add_question_frame, background='lightpink', justify=LEFT,
                                         width=20, text='Point Value: ', font=('Arial', 15))
    point_value_label_for_adding.grid(row=11, column=0)
    point_value_entry = Entry(add_question_frame, justify=RIGHT, width=21, textvariable=points, relief=SUNKEN)
    point_value_entry.grid(row=11, column=1)

    empty_label_for_formatting_3 = Label(add_question_frame, text='', bg='lightpink')
    empty_label_for_formatting_3.grid(row=12, column=0, columnspan=3)

    add_question_button = Button(add_question_frame, background='lightpink',
                                 text='Add Question Data', font=('Arial', 15), relief=RAISED, command=add_questions)
    add_question_button.grid(row=13, column=0, columnspan=2)
    empty_label_for_formatting_4 = Label(add_question_frame, text=' ', bg='lightpink')
    empty_label_for_formatting_4.grid(row=14, column=0, columnspan=3)

    widgets_currently_in_window = [add_question_frame, questions_to_edit_frame, edit_questions_frame]


def add_questions():
    """Creates a Question object and converts it to a list in order to save the new question
    and all its details to the question pool"""
    global text, selection1, selection2, selection3, selection4, positive_feedback, negative_feedback, correct_answer, \
        points, editMode, editIndex, question_pool, question_listbox_for_editing_question_information
    valid_points = ['1', '2', '3']
    if text.get() == '' or selection1.get() == '' or selection2.get() == '' or selection3.get() == '' or \
            selection4.get() == '' or positive_feedback.get() == '' or negative_feedback.get() == '' or \
            correct_answer.get() == '' or points.get() == '':
        messagebox.showwarning(title='Error', message='One or many of the fields are empty. Please try Again!')
    elif points.get() not in valid_points:
        messagebox.showwarning(title='Error', message='Point value must be an integer of  1, 2, or 3.')
    else:
        new = Questions(text.get(), selection1.get(), selection2.get(), selection3.get(), selection4.get(),
                        positive_feedback.get(), negative_feedback.get(), correct_answer.get(), points.get())

        if len(question_pool) == 0:
            read_file()
        question_pool.append(new)
        messagebox.showinfo(title='Success', message='New Question was Successfully Added')

        clear_form()
        save_file()


def delete_question():
    """Deletes a question chosen by the user from the question pool"""
    global question_listbox_for_editing_question_information, editIndex, widgets_currently_in_window
    confirmation = messagebox.askquestion("Confirm", "Are you sure you want to delete this question?", icon='warning')
    if confirmation == 'yes':
        question_pool.pop(editIndex)
        question_listbox_for_editing_question_information.delete(editIndex)
        empty_label_for_formatting_5.grid_forget()
        delete_status.grid(row=15, column=0, columnspan=3)
        delete_status['text'] = '--Question was Successfully Deleted--'
        # messagebox.showinfo(title='Success', message="Question was successfully deleted!")
    else:
        empty_label_for_formatting_5.grid_forget()
        delete_status.grid(row=15, column=0, columnspan=3)
        delete_status['text'] = '--Question was Not Deleted--'

    clear_form()
    save_file()


def quiz_interface():
    """Executes when 'Take a Quiz' is selected in the menu bar 'Quiz' dropdown"""
    global question_number, question_pool, earned_points, text, selection1, selection2, \
        selection3, selection4, correct_answer, points, positive_feedback, negative_feedback, \
        total_questions, widgets_currently_in_window, total_points, feedback, index1, index2, index3
    forget_widgets_in_window()
    clear_form()

    quiz_frame.pack(padx=10, pady=10, ipadx=30, ipady=30)
    quiz_frame.pack_propagate()

    question_frame.pack(pady=10)
    point_value_label.grid(row=0, column=0, sticky=W)
    point_value_label_2.grid(row=0, column=1, sticky=W)
    question_number_label.grid(row=1, column=0, sticky=E)
    question_label.grid(row=1, column=1, sticky=W)

    selection_frame.pack(pady=10)
    Label(selection_frame, bg='lightyellow', text="A.").grid(row=0, column=0)
    selection1_label = Label(selection_frame, bg='lightyellow', textvariable=selection1)
    selection1_label.grid(row=0, column=1, padx=2, pady=2, sticky=W)
    Label(selection_frame, bg='lightyellow', text="B.").grid(row=1, column=0)
    selection2_label = Label(selection_frame, bg='lightyellow', textvariable=selection2)
    selection2_label.grid(row=1, column=1, padx=2, pady=2, sticky=W)
    Label(selection_frame, bg='lightyellow', text="C.").grid(row=2, column=0)
    selection3_label = Label(selection_frame, bg='lightyellow', textvariable=selection3)
    selection3_label.grid(row=2, column=1, padx=2, pady=2, sticky=W)
    Label(selection_frame, bg='lightyellow', text="D.").grid(row=3, column=0)
    selection4_label = Label(selection_frame, bg='lightyellow', textvariable=selection4)
    selection4_label.grid(row=3, column=1, padx=2, pady=2, sticky=W)

    answer_frame.pack(pady=0)
    instructions_for_quiz_label.pack(side=LEFT, padx=8)
    answer_entry.pack(side=LEFT)
    submit_answer_button.pack(padx=10, pady=10, ipady=2)
    correct_answer_label.pack(pady=5)
    feedback_label.pack(pady=5)
    points_earned_label.pack(ipady=5, ipadx=2)

    widgets_currently_in_window = [quiz_frame, question_frame, answer_frame, selection_frame, points_earned_label,
                                   point_value_label_2, question_number_label, question_label,
                                   instructions_for_quiz_label, answer_entry, submit_answer_button,
                                   correct_answer_label, feedback_label,
                                   points_earned_label, feedback_image]

    # picks three indexes to pick three random questions in the question pool
    # if any of the indexes are the same, a new index is chosen
    index1 = random.randint(0, len(question_pool))
    while True:
        index2 = random.randint(0, len(question_pool))
        if index2 == index1:
            index2 = random.randint(0, len(question_pool))
        index3 = random.randint(0, len(question_pool))
        if index3 == index1:
            index3 = random.randint(0, len(question_pool))
        if index1 != index2 and index2 != index3 and index1 != index3:
            break

    question_number.set('1/3')
    show_question(index1)


def show_question(index_number):
    """Displays the first question for the quiz game"""
    global question_pool, index1, index2, index3
    index = index_number
    try:
        random_question = question_pool[index]
    except IndexError:
        messagebox.showwarning(title='Error loading the quiz!',
                               message='Something went wrong. You are being sent back to the home page.')
        home()

    else:
        text.set(random_question.question_text)
        selection1.set(random_question.option1)
        selection2.set(random_question.option2)
        selection3.set(random_question.option3)
        selection4.set(random_question.option4)
        correct_answer.set(random_question.answer)
        positive_feedback.set(random_question.correct_feedback)
        negative_feedback.set(random_question.incorrect_feedback)
        points.set(random_question.point_value)

        # if the random question chosen contains invalid data, choose a new random question
        if text.get() == 'Unknown' or selection1.get() == 'Unknown' or selection2.get() == 'Unknown' \
            or selection3.get() == 'Unknown' or selection4.get() == 'Unknown' or correct_answer.get() == 'Unknown' \
                or positive_feedback.get() == 'Unknown' or negative_feedback.get() == 'Unknown':
            new_index1 = random.randint(0, len(question_pool))
            while True:
                new_index2 = random.randint(0, len(question_pool))
                if new_index2 == new_index1:
                    new_index2 = random.randint(0, len(question_pool))
                new_index3 = random.randint(0, len(question_pool))
                if new_index3 == new_index1:
                    new_index3 = random.randint(0, len(question_pool))
                if new_index1 != new_index2 and new_index2 != new_index3 and new_index1 != new_index3:
                    break

            # recall show question function and pass in the new index depending on what question number the quiz is on
            if question_number.get() == '1/3':
                show_question(new_index1)
            elif question_number.get() == '2/3':
                show_question(new_index2)
            else:
                show_question(new_index3)


def check_answer():
    """Executes when submit button during quiz is pressed
    to check user answer if of correct format"""
    global user_answer, selection1, selection2, selection3, selection4
    if user_answer.get() == 'A' or user_answer.get() == 'a':
        user_answer.set(selection1.get())
    elif user_answer.get() == 'B' or user_answer.get() == 'b':
        user_answer.set(selection2.get())
    elif user_answer.get() == 'C' or user_answer.get() == 'c':
        user_answer.set(selection3.get())
    elif user_answer.get() == 'D' or user_answer.get() == 'd':
        user_answer.set(selection4.get())
    else:
        messagebox.showwarning(title='Error', message='Please enter A, B, C or D as your answer.')

    acceptable_answers = [selection1.get(), selection2.get(), selection3.get(), selection4.get()]
    if user_answer.get() in acceptable_answers:
        is_answer_correct()


def is_answer_correct():
    """Checks to see if user answer is the correct answer"""
    global feedback, earned_points, question_number, total_points, correct_answer
    if user_answer.get() == correct_answer.get():
        feedback.set(positive_feedback.get())
        feedback_label.config(textvariable=feedback)
        earned_points += int(points.get())
        total_points += int(points.get())
        points_earned_label.config(text=f'Points Earned: {earned_points}/{total_points}')

        correct_answer_img_list = [load_correct_answer_img_1, load_correct_answer_img_2,
                                   load_correct_answer_img_3, load_correct_answer_img_4]
        random_photo = random.choice(correct_answer_img_list)
        feedback_image.config(image=random_photo)
        feedback.image = random_photo
        feedback_image.pack(pady=8)

    else:
        correct_answer_label.config(text=f'The correct answer was: {correct_answer.get()}')
        feedback.set(negative_feedback.get())
        feedback_label.config(textvariable=feedback)
        total_points += int(points.get())
        points_earned_label.config(text=f'Points Earned: {earned_points}/{total_points}')

        incorrect_answer_img_list = [load_incorrect_answer_img_1, load_incorrect_answer_img_2,
                                     load_incorrect_answer_img_3]
        random_photo = random.choice(incorrect_answer_img_list)
        feedback_image.config(image=random_photo)
        feedback.image = random_photo
    feedback_image.pack(pady=8)

    if question_number.get() == '3/3':
        submit_answer_button.config(text='End Quiz', command=end_quiz)
    else:
        submit_answer_button.config(text='Continue', command=continue_to_next_question)


def continue_to_next_question():
    """Displays question two and three of the quiz game"""
    global question_number, index2, index3, user_answer
    submit_answer_button.config(text='Submit', command=check_answer)
    correct_answer_label['text'] = ''
    feedback.set('')
    feedback_label.config(textvariable=feedback)
    user_answer.set('')
    feedback_image.pack_forget()

    if question_number.get() == '1/3':
        show_question(index2)
        question_number.set('2/3')
    elif question_number.get() == '2/3':
        show_question(index3)
        question_number.set('3/3')


def end_quiz():
    """Ends the current quiz and takes user back to the home page"""
    forget_widgets_in_window()
    clear_form()
    submit_answer_button.config(text='Submit', command=check_answer)
    correct_answer_label['text'] = ''
    feedback.set('')
    feedback_label.config(textvariable=feedback)
    user_answer.set('')
    feedback_image.pack_forget()
    home()


# main application window
window = Tk()
window.title('Mental Anguish Quiz Management System')
window.geometry("800x600")
window['background'] = 'lightblue'
window.iconbitmap('images/icon_pic.ico')
C = Canvas(bg='lightblue', height=800, width=600)
file = PhotoImage(file='images/brain_resize.png')
background_image = Label(image=file)
background_image.place(x=0, y=0, relwidth=1, relheight=1)

# variables needed for application
text = StringVar()
selection1 = StringVar()
selection2 = StringVar()
selection3 = StringVar()
selection4 = StringVar()
positive_feedback = StringVar()
negative_feedback = StringVar()
correct_answer = StringVar()
points = StringVar()
keyword = StringVar()
keyword.set('')

# variables needed for quiz game
question_number = StringVar()
total_questions = 3
earned_points = int()
total_points = int()
user_answer = StringVar()
feedback = StringVar()
question_number.set('')
index1 = int()
index2 = int()
index3 = int()

# images for quiz
correct_answer_img_1 = Image.open('images/Congrats.jpg')
load_correct_answer_img_1 = ImageTk.PhotoImage(correct_answer_img_1)
correct_answer_img_2 = Image.open('images/yay.jpg')
load_correct_answer_img_2 = ImageTk.PhotoImage(correct_answer_img_2)
correct_answer_img_3 = Image.open('images/good_job_resize.jpg')
load_correct_answer_img_3 = ImageTk.PhotoImage(correct_answer_img_3)
correct_answer_img_4 = Image.open('images/seal_of_approval_img_resize.png')
load_correct_answer_img_4 = ImageTk.PhotoImage(correct_answer_img_4)

incorrect_answer_img_1 = Image.open('images/oh_no.jpg')
load_incorrect_answer_img_1 = ImageTk.PhotoImage(incorrect_answer_img_1)
incorrect_answer_img_2 = Image.open('images/incorrect_resize.jpg')
load_incorrect_answer_img_2 = ImageTk.PhotoImage(incorrect_answer_img_2)
incorrect_answer_img_3 = Image.open('images/try-again-stamp.jpg')
load_incorrect_answer_img_3 = ImageTk.PhotoImage(incorrect_answer_img_3)


# menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=False)
edit_menu = Menu(menu_bar, tearoff=False)
quiz_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_cascade(label='Quiz', menu=quiz_menu)
file_menu.add_command(label='Home Page', command=home)
file_menu.add_command(label='Instructions', command=instructions)
file_menu.add_command(label='View Questions', command=view_questions_and_details)
file_menu.add_command(label='Search', command=search_interface)
file_menu.add_command(label='Exit', command=exit_window)
edit_menu.add_command(label='Edit/ Delete Questions', command=edit_questions_interface)
edit_menu.add_command(label='Add Questions', command=add_interface)
quiz_menu.add_command(label='Take a Quiz', command=quiz_interface)

# title frame
title_frame = Frame(window, bg='lightpink', borderwidth=2, relief=RAISED, width=300, height=50)
title_frame.pack(pady=15)
title_frame.pack_propagate(0)
title = Label(title_frame, text='Mental Anguish', bg='lightpink', font=('Courier', 24))
title.pack(pady=6)

# global widgets needed for application
welcome_message = Label(window, bg='lightblue', text='Welcome to the Mental Anguish Quiz!',
                        font=('Courier', 18), relief=SUNKEN)
home_page_message = Label(window, bg='lightblue', text='', relief=SUNKEN)
application_frame = Frame(window, bg='lightpink', borderwidth=2, relief=RAISED, width=600, height=300)
vertical_scrollbar_for_questions_listbox = Scrollbar(application_frame, orient=VERTICAL)
horizontal_scrollbar_for_questions_listbox = Scrollbar(application_frame, orient=HORIZONTAL)

# view questions interface widgets
view_questions_listbox = Listbox(application_frame, yscrollcommand=vertical_scrollbar_for_questions_listbox,
                                 xscrollcommand=horizontal_scrollbar_for_questions_listbox, width=500, height=200)
view_details_frame = Frame(window, bg='lightpink', borderwidth=2, relief=SUNKEN, width=500, height=400)
questions_to_view_frame = Frame(window, bg='lightpink', borderwidth=2, relief=RAISED, width=340, height=400)
question_listbox_for_viewing_question_information = Listbox(questions_to_view_frame,
                                                            yscrollcommand=vertical_scrollbar_for_questions_listbox,
                                                            xscrollcommand=horizontal_scrollbar_for_questions_listbox,
                                                            width=300, height=200)
details_listbox = Listbox(view_details_frame,  yscrollcommand=vertical_scrollbar_for_questions_listbox,
                          xscrollcommand=horizontal_scrollbar_for_questions_listbox, width=500, height=200)

# edit question interface widgets
edit_questions_frame = Frame(window, bg='lightpink', borderwidth=2, relief=SUNKEN, width=300, height=400)
questions_to_edit_frame = Frame(window, bg='lightpink', borderwidth=2, relief=SUNKEN, width=340, height=400)
question_listbox_for_editing_question_information = Listbox(questions_to_edit_frame,
                                                            yscrollcommand=vertical_scrollbar_for_questions_listbox,
                                                            xscrollcommand=horizontal_scrollbar_for_questions_listbox,
                                                            width=300, height=200)
delete_status = Label(edit_questions_frame, text="", bg='lightpink', font="Courier")
empty_label_for_formatting_5 = Label(edit_questions_frame, text=' ', bg='lightpink')

# add question interface widgets
add_question_frame = Frame(window, bg='lightpink', borderwidth=2, relief=RAISED, width=600, height=410)

# search through questions interface widgets
search_through_questions_frame = Frame(window, bg='lightpink', borderwidth=2, relief=RAISED, width=600, height=300)
search_results_frame = Frame(window, bg='lightpink', borderwidth=2, relief=RAISED, width=600, height=300)
search_results_listbox = Listbox(search_results_frame, yscrollcommand=vertical_scrollbar_for_questions_listbox,
                                 xscrollcommand=horizontal_scrollbar_for_questions_listbox, width=100, height=80)


# quiz interface widgets
quiz_frame = Frame(window, bg='lightyellow', borderwidth=2, relief=SUNKEN, width=500, height=400)
submit_answer_button = Button(quiz_frame, bg='white', text='Submit', command=check_answer)
correct_answer_label = Label(quiz_frame, bg='lightyellow')
feedback_label = Label(quiz_frame, bg='lightyellow')
points_earned_label = Label(quiz_frame, bg='lightblue', relief=SUNKEN, text='Points Earned: 0/0')
question_frame = Frame(quiz_frame, bg='lightyellow', width=300, height=50)
point_value_label = Label(question_frame, bg='lightyellow', text='Point Value: ')
point_value_label_2 = Label(question_frame, bg='lightyellow', textvariable=points)
question_number_label = Label(question_frame, bg='lightyellow', textvariable=question_number)
question_label = Label(question_frame, bg='lightyellow', textvariable=text)
selection_frame = Frame(quiz_frame, bg='lightyellow')
answer_frame = Frame(quiz_frame, bg='lightyellow')
instructions_for_quiz_label = Label(answer_frame, bg='lightyellow', text='Your answer (A, B, C, or D):')
answer_entry = Entry(answer_frame, bg='white', textvariable=user_answer)
feedback_image = Label(quiz_frame, relief=SUNKEN)

home()
window.mainloop()
