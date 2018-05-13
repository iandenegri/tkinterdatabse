'''
GUI for a program that stores Title,Author,Year,ISBN
User can interact with stored data.
'''
from bookdata import Database
from tkinter import *

database=Database('books.db')

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        entry1.delete(0,END)
        entry1.insert(END,selected_tuple[1])
        entry2.delete(0,END)
        entry2.insert(END,selected_tuple[2])
        entry3.delete(0,END)
        entry3.insert(END,selected_tuple[3])
        entry4.delete(0,END)
        entry4.insert(END,selected_tuple[4])
    except IndexError:
        pass

#functions to use on buttons

def view_function():
    list1.delete(0,END)
    for row in database.view_data():
        list1.insert(END,row)

def search_func():
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_func():
    database.insert_data(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_func():
    database.delete_data(selected_tuple[0])
    list1.delete(0,END)
    for row in database.view_data():
        list1.insert(END,row)

def update_func():
    database.update_data(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    for row in database.view_data():
        list1.insert(END,row)


window=Tk()

window.wm_title("Ian's Jank Bookstore")

# Label widgets for the entries

label1 = Label(window,text='Title')
label1.grid(row=0,column=0)

label2 = Label(window,text='Author')
label2.grid(row=0,column=2)

label3 = Label(window,text='Year')
label3.grid(row=1,column=0)

label4 = Label(window,text='ISBN')
label4.grid(row=1,column=2)

# Add entry widgets

title_text = StringVar()
entry1 = Entry(window,textvariable=title_text)
entry1.grid(row=0,column=1)

author_text = StringVar()
entry2 = Entry(window,textvariable=author_text)
entry2.grid(row=0,column=3)

year_text = StringVar()
entry3 = Entry(window,textvariable=year_text)
entry3.grid(row=1,column=1)

isbn_text = StringVar()
entry4 = Entry(window,textvariable=isbn_text)
entry4.grid(row=1,column=3)

# List box
list1 = Listbox(window,height=7,width=50)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

#Scrollbar
scroll1=Scrollbar(window)
scroll1.grid(row=2,column=2,rowspan=6)

#attach scrollbar to list
list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

#Buttons
but1=Button(window,text='View All',width=16,command=view_function)
but1.grid(row=2,column=3)

but2=Button(window,text='Search Entries',width=16,command=search_func)
but2.grid(row=3,column=3)

but3=Button(window,text='Add Entry',width=16,command=add_func)
but3.grid(row=4,column=3)

but4=Button(window,text='Update Entry',width=16,command=update_func)
but4.grid(row=5,column=3)

but5=Button(window,text='Delete Entry',width=16,command=delete_func)
but5.grid(row=6,column=3)

but5=Button(window,text='Close Program',width=16,command=window.destroy)
but5.grid(row=7,column=3)

window.mainloop()
