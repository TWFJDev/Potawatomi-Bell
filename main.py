from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3

bell_closet_tracker = Tk()
bell_closet_tracker.title("Bell Closet")

def createDBIfNotExist():
    conn = sqlite3.connect('current_bell_items.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS items_in(
        initials_clock_number TEXT,
        guest_name TEXT,
        number_of_items TEXT,
        tag_number TEXT,
        location TEXT,
        time_in TEXT,
        time_out TEXT,
        comments TEXT
    )""")

    conn.commit()
    conn.close()

# Look through database when program starts
def querydb():
    global items
    conn = sqlite3.connect('current_bell_items.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM items_in")
    items = c.fetchall()

    # Add data to screen
    for items in items:
        if int(str(items[0])) % 2 == 0:
            treeTable.insert(parent = '', index = 'end', iid = items[0], text = '', values = (items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8]), tags = ('evenrow',))
        else:
            treeTable.insert(parent = '', index = 'end', iid = items[0], text = '', values = (items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8]), tags = ('oddrow',))

    conn.commit()
    conn.close()

def clearEntryBoxes():
    initialsEntry.delete(0, END)
    guestNameEntry.delete(0, END)
    numItemsEntry.delete(0, END)
    tagNumEntry.delete(0, END)
    locationEntry.delete(0, END)
    timeInEntry.delete(0, END)
    timeOutEntry.delete(0, END)
    commentsEntry.delete(0, END)

def selectAnItem(e):
    clearEntryBoxes()

    selected = treeTable.focus()

    values = treeTable.item(selected, 'values')

    initialsEntry.insert(0, values[1])
    guestNameEntry.insert(0, values[2])
    numItemsEntry.insert(0, values[3])
    tagNumEntry.insert(0, values[4])
    locationEntry.insert(0, values[5])
    timeInEntry.insert(0, values[6])
    timeOutEntry.insert(0, values[7])
    commentsEntry.insert(0, values[8])

def addItems():
    conn = sqlite3.connect('current_bell_items.db')
    c = conn.cursor()

    init_clock_num = initialsEntry.get()
    guest = guestNameEntry.get()
    item_quantity = numItemsEntry.get()
    tag = tagNumEntry.get()
    space = locationEntry.get()
    time_in_bell = timeInEntry.get()
    time_out_bell = timeOutEntry.get()

    if init_clock_num == '':
        messagebox.showerror("Bell Closet", "Please fill out the 'Initials/Clock #' box!")

    elif guest == '':
        messagebox.showerror("Bell Closet", "Please fill out 'Guest Name' box!")

    elif item_quantity == '':
        messagebox.showerror("Bell Closet", "Please fill out the '# of Items' box!")

    elif tag == '':
        messagebox.showerror("Bell Closet", "Please fill out the 'Tag #' box!")

    elif space == '':
        messagebox.showerror("Bell Closet", "Please fill out the 'Location' box!")

    elif time_in_bell == '':
        messagebox.showerror("Bell Closet", "Please fill out the 'Time In' box!")

    elif time_out_bell == '':
        messagebox.showerror("Bell Closet", "Please fill out the 'Time Out' box!")

    else:
        c.execute("INSERT INTO items_in VALUES(:initials_clock_number, :guest_name, :number_of_items, :tag_number, :location, :time_in, :time_out, :comments)", {
            'initials_clock_number' : initialsEntry.get(), 
            'guest_name' : guestNameEntry.get(), 
            'number_of_items' : numItemsEntry.get(),
            'tag_number' : tagNumEntry.get(),
            'location' : locationEntry.get(),
            'time_in' : timeInEntry.get(),
            'time_out' : timeOutEntry.get(),
            'comments' : commentsEntry.get()
        })

    conn.commit()
    conn.close()

    clearEntryBoxes()

    treeTable.delete(*treeTable.get_children())

    querydb()

# def updateACard():

#     cardName = cardNameEntry.get()
#     type1 = typeEntry.get()
#     cardNumber = cardNumberEntry.get()
#     manaType1 = manaType1Entry.get()
#     manaType2 = manaType2Entry.get()
#     manaCost = manaCost2Entry.get()

#     if cardName == '':
#         messagebox.showerror("Magic Card Sorter", "Please fill out the 'card name' box!")

#     elif type1 == '':
#         messagebox.showerror("Magic Card Sorter", "Please fill out 'type 1' box!")

#     elif cardNumber == '':
#         messagebox.showerror("Magic Card Sorter", "Please fill out the 'card number' box!")

#     elif manaType1 == '':
#         messagebox.showerror("Magic Card Sorter", "Please fill out the 'mana type 1' box!")

#     elif manaType2 == '':
#         messagebox.showerror("Magic Card Sorter", "Please fill out the 'mana type 2' box!")

#     elif manaCost == '':
#         messagebox.showerror("Magic Card Sorter", "Please fill out the 'mana cost' box!")

#     else:
  
#         selected = treeTable.focus()
#         treeTable.item(selected, text = "", values = (
#             itemNumberEntry.get(), 
#             cardNameEntry.get(), 
#             typeEntry.get(), 
#             subTypeEntry.get(),
#             type3Entry.get(),
#             type4Entry.get(),
#             type5Entry.get(),
#             type6Entry.get(),
#             type7Entry.get(), 
#             manaType1Entry.get(),
#             manaType2Entry.get(), 
#             manaCost2Entry.get(), 
#             powerToughnessEntry.get(), 
#             cardNumberEntry.get()
#             ))
    
#         conn = sqlite3.connect('magicCards.db')
#         c = conn.cursor()
    
#         c.execute("""UPDATE cards SET
#             card_name = :card_name,
#             type_1 = :type_1,
#             type_2 = :type_2,
#             type_3 = :type_3,
#             type_4 = :type_4,
#             type_5 = :type_5,
#             type_6 = :type_6,
#             type_7 = :type_7,
#             mana_type_1 = :mana_type_1,
#             mana_type_2 = :mana_type_2,
#             mana_cost_2 = :mana_cost_1,
#             power_toughness = :power_toughness,
#             card_number = :card_number 
    
#             WHERE oid = :oid""", {
#                'card_name' : cardNameEntry.get(), 
#                'type_1' : typeEntry.get(), 
#                'type_2' : subTypeEntry.get(),
#                'type_3' : type3Entry.get(),
#                'type_4' : type4Entry.get(),
#                'type_5' : type5Entry.get(),
#                'type_6' : type6Entry.get(),
#                'type_7' : type7Entry.get(), 
#                'mana_type_1' : manaType1Entry.get(),
#                'mana_type_2' : manaType2Entry.get(), 
#                'mana_cost_1' : manaCost2Entry.get(), 
#                'power_toughness' : powerToughnessEntry.get(), 
#                'card_number' : cardNumberEntry.get(),
#                'oid' : card[0]
#             })

#         conn.commit()
#         conn.close()

#     clearEntryBoxes()

def removeAItem():
    x = treeTable.selection()[0]
    treeTable.delete(x)

    conn = sqlite3.connect('current_bell_items.db')
    c = conn.cursor()

    c.execute("DELETE FROM items_in WHERE oid = " + str(items[0]))

    conn.commit()
    conn.close()

    messagebox.showinfo("Bell Closet", "Info has been deleted")

    clearEntryBoxes()

# Create Treeview frame
treeFrame = Frame(bell_closet_tracker)
treeFrame.pack(padx = 10, pady = 10)

# Scrollbar
treeScrolly = Scrollbar(treeFrame)
treeScrolly.pack(side = RIGHT, fill = Y)

treeScrollx=Scrollbar(treeFrame, orient = 'horizontal')
treeScrollx.pack(side = BOTTOM, fill = 'x')

# Create Treeview
treeTable = ttk.Treeview(treeFrame, yscrollcommand = treeScrolly.set, xscrollcommand = treeScrollx.set, selectmode = "extended")
treeTable.pack()

# Scrollbar config
treeScrolly.config(command = treeTable.yview)
treeScrollx.config(command = treeTable.xview)

# Define columns
treeTable['columns'] = ("Item Info", "Initials/Clock #", "Guest Name", "# of Items", "Tag #", "Location", "Time In", "Time Out", "Comments")

# Format Columns
treeTable.column("#0", width = 0, stretch = NO)
treeTable.column("Item Info", anchor = CENTER, width = 110, minwidth = 110)
treeTable.column("Initials/Clock #", anchor = CENTER, width = 120, minwidth = 120)
treeTable.column("Guest Name", anchor = CENTER, width = 110, minwidth = 110, stretch = YES)
treeTable.column("# of Items", anchor = CENTER, width = 100, minwidth = 100)
treeTable.column("Tag #", anchor = CENTER, width = 80, minwidth = 80)
treeTable.column("Location", anchor = CENTER, width = 100, minwidth = 100)
treeTable.column("Time In", anchor = CENTER, width = 85, minwidth = 85)
treeTable.column("Time Out", anchor = CENTER, width = 100, minwidth = 100)
treeTable.column("Comments", anchor = CENTER, width = 100, minwidth = 100, stretch = YES)

# Create Headings
treeTable.heading("#0", text = "", anchor = CENTER)
treeTable.heading("Item Info", text = "Item Info #", anchor = CENTER)
treeTable.heading("Initials/Clock #", text = "Initials/Clock #", anchor = CENTER)
treeTable.heading("Guest Name", text = "Guest Name", anchor = CENTER)
treeTable.heading("# of Items", text = "# of Items", anchor = CENTER)
treeTable.heading("Tag #", text = "Tag #", anchor = CENTER)
treeTable.heading("Location", text = "Location", anchor = CENTER)
treeTable.heading("Time In", text = "Time In", anchor = CENTER)
treeTable.heading("Time Out", text = "Time Out", anchor = CENTER)
treeTable.heading("Comments", text = "Comments", anchor = CENTER)

# Add item data frame
itemDataFrame = LabelFrame(bell_closet_tracker, text = "Item Info:")
itemDataFrame.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

initialsLabel = Label(itemDataFrame, text = "Initials/Clock #:")
initialsLabel.grid(row = 0, column = 0, padx = 10, pady = 10)

initialsEntry = Entry(itemDataFrame, border = 2)
initialsEntry.grid(row = 0, column = 1, padx = 10, pady = 10)

guestNameLabel = Label(itemDataFrame, text = "Guest Name:")
guestNameLabel.grid(row = 0, column = 2, padx = 10, pady = 10)

guestNameEntry = Entry(itemDataFrame, border = 2)
guestNameEntry.grid(row = 0, column = 3, padx = 10, pady = 10)

numItemsLabel = Label(itemDataFrame, text = "# of Items:")
numItemsLabel.grid(row = 0, column = 4, padx = 10, pady = 10)

numItemsEntry = Entry(itemDataFrame, border = 2)
numItemsEntry.grid(row = 0, column = 5, padx = 10, pady = 10)

tagNumLabel = Label(itemDataFrame, text = "Tag #:")
tagNumLabel.grid(row = 0, column = 6, padx = 10, pady = 10)

tagNumEntry = Entry(itemDataFrame, border = 2)
tagNumEntry.grid(row = 0, column = 7, padx = 10, pady = 10)

locationLabel = Label(itemDataFrame, text = "Location:")
locationLabel.grid(row = 1, column = 0, padx = 10, pady = 10)

locationEntry = Entry(itemDataFrame, border = 2)
locationEntry.grid(row = 1, column = 1, padx = 10, pady = 10)

timeInLabel = Label(itemDataFrame, text = "Time In:")
timeInLabel.grid(row = 1, column = 2, padx = 10, pady = 10)

timeInEntry = Entry(itemDataFrame, border = 2)
timeInEntry.grid(row = 1, column = 3, padx = 10, pady = 10)

timeOutLabel = Label(itemDataFrame, text = "Time Out:")
timeOutLabel.grid(row = 1, column = 4, padx = 10, pady = 10)

timeOutEntry = Entry(itemDataFrame, border = 2)
timeOutEntry.grid(row = 1, column = 5, padx = 10, pady = 10)

commentsLabel = Label(itemDataFrame, text = "Comments:")
commentsLabel.grid(row = 1, column = 6, padx = 10, pady = 10)

commentsEntry = Entry(itemDataFrame, border = 2)
commentsEntry.grid(row = 1, column = 7, padx = 10, pady = 10)

addAnItem = Button(itemDataFrame, text = "Add Items", command = addItems)
addAnItem.grid(row = 2, column = 2, padx = 10, pady = 10)

updateAnItem = Button(itemDataFrame, text = "Update Info")
updateAnItem.grid(row = 2, column = 3, padx = 10, pady = 10)

removeAnItem = Button(itemDataFrame, text = "Remove Item", command = removeAItem)
removeAnItem.grid(row = 2, column = 4, padx = 10, pady = 10)

clearEntry = Button(itemDataFrame, text = "Clear Entries", command = clearEntryBoxes)
clearEntry.grid(row = 2, column = 5, padx = 10, pady = 10)

treeTable.bind("<ButtonRelease-1>", selectAnItem)

createDBIfNotExist()

querydb()

bell_closet_tracker.mainloop()