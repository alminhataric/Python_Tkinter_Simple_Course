from tkinter import *
from PIL import ImageTk, Image
import _sqlite3

#Full course on youtube Tkinter Course - Create Graphic User Interfaces in Python Tutorial

root = Tk()
root.title("Welcome to Python")
root.geometry("300x400")

#Database

#Create a database or connect to one
conn = _sqlite3.connect("address_book.db")

c = conn.cursor()

'''
#Create table
c.execute(""" CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)""")
'''

#Create function to update record
def update():
    conn = _sqlite3.connect("address_book.db")
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET     
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
        {
            'first': f_name_update.get(),
            'last': l_name_update.get(),
            'address': address_update.get(),
            'city': city_update.get(),
            'state': state_update.get(),
            'zipcode': zipcode_update.get(),

            'oid': record_id
        })
    conn.commit()
    conn.close()
    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Update a record")
    editor.geometry("300x250")

    conn = _sqlite3.connect("address_book.db")
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    #Create Global Variables for text box names

    global f_name_update
    global l_name_update
    global address_update
    global city_update
    global state_update
    global zipcode_update

    # Creating Text Boxes
    f_name_update = Entry(editor, width=30)
    f_name_update.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_update = Entry(editor, width=30)
    l_name_update.grid(row=1, column=1)
    address_update = Entry(editor, width=30)
    address_update.grid(row=2, column=1)
    city_update = Entry(editor, width=30)
    city_update.grid(row=3, column=1)
    state_update = Entry(editor, width=30)
    state_update.grid(row=4, column=1)
    zipcode_update = Entry(editor, width=30)
    zipcode_update.grid(row=5, column=1)

    # Create Text Box Label
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Loop thru results
    for record in records:
        f_name_update.insert(0, record[0])
        l_name_update.insert(0, record[1])
        address_update.insert(0, record[2])
        city_update.insert(0, record[3])
        state_update.insert(0, record[4])
        zipcode_update.insert(0, record[5])


    # Create an Save Button To Save Updated Record
    edit_btn = Button(editor, text="Save Changes", command=update)
    edit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=50)


#Create function to delete record
def delete():
    conn = _sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())
    delete_box.delete(0, END)

    conn.commit()
    conn.close()

#Create Submit Function

def submit():
    conn = _sqlite3.connect("address_book.db")
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode )",
              {
                  'f_name':f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    conn.commit()
    conn.close()

    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#Create Query Function
def query():
    conn = _sqlite3.connect("address_book.db")
    c = conn.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    #Loop Thru Results

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +    str(record[6]) + "\n"

    query_label = Label(root, text = print_records)
    query_label.grid(row=12,column=0,columnspan=2)

    conn.commit()
    conn.close()

#Creating Text Boxes

f_name = Entry(root, width=30)
f_name.grid(row=0,column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1)
address = Entry(root, width=30)
address.grid(row=2,column=1)
city = Entry(root, width=30)
city.grid(row=3,column=1)
state = Entry(root, width=30)
state.grid(row=4,column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5,column=1)

delete_box = Entry(root,width=30)
delete_box.grid(row=9, column=1, pady=5)

#Create Text Box Label
f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0, pady=(10, 0))
l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label = Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label = Label(root,text="City")
city_label.grid(row=3,column=0)
state_label = Label(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label = Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

#Create Submit Button

submit_btn = Button(root, text="Add Records To Database", command=submit)
submit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=20)

#Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=1, columnspan=2, pady=10,  padx=10, ipadx=50)


#Create A Delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

#Create an Update Button
edit_btn = Button(root, text="Update Record", command=edit)
edit_btn.grid(row=11, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

#Commit Changes
conn.commit()

#Close Connection
conn.close()

root.mainloop()