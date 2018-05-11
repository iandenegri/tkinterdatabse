'''
GUI for a program that stores Title,Author,Year,ISBN
User can interact with stored data.
'''
import bookdata
from tkinter import *

#functions to use on buttons

def view_function():
    list1.delete(0,END)
    for row in bookdata.view_data():
        list1.insert(END,row)





window=Tk()

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

but3=Button(window,text='Add Entry',width=16)
but3.grid(row=4,column=3)

but4=Button(window,text='Update Entry',width=16)
but4.grid(row=5,column=3)

but5=Button(window,text='Delete Entry',width=16)
but5.grid(row=6,column=3)

but5=Button(window,text='Close Program',width=16)
but5.grid(row=7,column=3)

window.mainloop()
