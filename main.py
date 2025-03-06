import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox
from tkcalendar import Calendar


win = tk.Tk()
win.geometry("1350x700+0+0")
win.resizable(True,True)
win.title("Student Management")
title = tk.Label(win,text="Student Management System",font=("Arial",25,"bold"),border=12,relief=tk.RIDGE,bg="lightblue",foreground="red")
title.pack(side=tk.TOP,fill=tk.X)


def create_gradient(canvas, width, height, color1, color2):
    # Create gradient rectangle
    for y in range(height):
        # Interpolate colors
        r = int(color1[0] * (height - y) / height + color2[0] * y / height)
        g = int(color1[1] * (height - y) / height + color2[1] * y / height)
        b = int(color1[2] * (height - y) / height + color2[2] * y / height)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, y, width, y, fill=color, width=1)
        

def on_resize(event):
    # Update gradient on window resize
    canvas.config(width=event.width, height=event.height)
    create_gradient(canvas, event.width, event.height, color1, color2)
# Create canva
canvas = tk.Canvas(win, width=1500, height=900)
canvas.pack(fill=tk.BOTH, expand=True)

# Define gradient colors
color1 = (255, 255, 255)  # white
color2 = (0, 255, 255)       # blue

# Create gradient
create_gradient(canvas, 1350, 700, color1, color2)




detail_frame =tk.LabelFrame(win,text="Enter Details",font=("Arial",19),bd=10,relief=tk.GROOVE,bg="lightblue") #Label_Frame
detail_frame.place(x=20,y=90,width=420,height=572)

##DATAFRAME
data_frame = tk.Frame(win,bd=10,relief=tk.GROOVE,bg="lightblue") #Data_Frame
data_frame.place(x=470,y=90,width=852,height=571)
##DAtaframe_Created

#====Variables====#

rollno = tk.StringVar()
name =tk.StringVar()
gender = tk.StringVar()
selected_datedob =tk.StringVar()
class_var =tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
father_name =tk.StringVar()
address = tk.StringVar()

search_by = tk.StringVar()
search_txt=tk.StringVar()
##==================================================ENTRY==================================================##

rollno_lb1 =tk.Label(detail_frame,text="Roll No",font=("Bahnschrift",17),bg="lightblue")
rollno_lb1.grid(row=0,column=0,padx=2,pady=2)
rollno_entry = tk.Entry(detail_frame,bd=7,font=("Arail",15),textvariable=rollno)
rollno_entry.grid(row=0,column=2,padx=2,pady=2)

name_lb2 =tk.Label(detail_frame,text="Name",font=("Bahnschrift",17),bg="lightblue")
name_lb2.grid(row=1,column=0,padx=2,pady=2)
name_entry = tk.Entry(detail_frame,bd=7,font=("Arail",15),textvariable=name)
name_entry.grid(row=1,column=2,padx=2,pady=2)

gender_lb3 =tk.Label(detail_frame,text="Gender",font=("Bahnschrift",17),bg="lightblue")
gender_lb3.grid(row=2,column=0,padx=2,pady=2)
gender_entry = ttk.Combobox(detail_frame,font=("Arail",15),state="readonly",textvariable=gender)
gender_entry["values"]=("Male","Female","Other")
gender_entry.grid(row=2,column=2,padx=2,pady=2)


DOB_lb4 =tk.Label(detail_frame,text="DOB",font=("Bahnschrift",17),bg="lightblue")
DOB_lb4.grid(row=3,column=0,padx=2,pady=2)

def display_calendar():
    def select_date():
        selected_datedob.set(cal.get_date())
        top.destroy()

    top = tk.Toplevel(detail_frame)
    cal = Calendar(top, select_mode="day", date_pattern="dd-mm-y")
    cal.pack(padx=10, pady=10)
    select_button = tk.Button(top, text="Select", command=select_date)
    select_button.pack(pady=10)


selected_datedob = tk.StringVar()
DOB_entry = tk.Entry(detail_frame,bd=7,font=("Arail",15), textvariable=selected_datedob)
DOB_entry.grid(row=3,column=2,padx=2,pady=2)

calendar_button = tk.Button(detail_frame, text="Select Date", command=display_calendar)
calendar_button.grid(row=3,column=2,padx=1,pady=2)
calendar_button.place(x=315,y=132)



class_lb5 =tk.Label(detail_frame,text="Class",font=("Bahnschrift",17),bg="lightblue")
class_lb5.grid(row=4,column=0,padx=2,pady=2)
class_entry = tk.Entry(detail_frame,bd=7,font=("Arail",15),textvariable=class_var)
class_entry.grid(row=4,column=2,padx=2,pady=2)

section_lb6 =tk.Label(detail_frame,text="Section",font=("Bahnschrift",17),bg="lightblue")
section_lb6.grid(row=5,column=0,padx=2,pady=2)
section_entry = tk.Entry(detail_frame,bd=7,font=("Arail",15),textvariable=section)
section_entry.grid(row=5,column=2,padx=2,pady=2)

contact_lb7 =tk.Label(detail_frame,text="Contact",font=("Bahnschrift",17),bg="lightblue")
contact_lb7.grid(row=6,column=0,padx=2,pady=2)
contact_entry = tk.Entry(detail_frame,bd=7,font=("Arail",15),textvariable=contact)
contact_entry.grid(row=6,column=2,padx=2,pady=2)

FatherN_lb8 =tk.Label(detail_frame,text="Father Name",font=("Bahnschrift",17),bg="lightblue")
FatherN_lb8.grid(row=7,column=0,padx=2,pady=2)
FatherN_entry = tk.Entry(detail_frame,bd=7,font=("Arail",15),textvariable=father_name)
FatherN_entry.grid(row=7,column=2,padx=2,pady=2)

address_lb9 =tk.Label(detail_frame,text="Address",font=("Bahnschrift",17),bg="lightblue")
address_lb9.grid(row=8,column=0,padx=2,pady=2)
address_entry = tk.Entry(detail_frame,bd=7,font=("Arail",15),textvariable=address)
address_entry.grid(row=8,column=2,padx=2,pady=2)


##================================================================================##

#=============Functions===================#

def fetch_data():
    conn= pymysql.connect(host="localhost",user="root",password="",database="sms1")
    cur = conn.cursor()
    cur.execute("SELECT * FROM studentdata")
    rows =cur.fetchall()
    if len(rows)!=0:
        std_table.delete(*std_table.get_children())
        for row in rows:
            std_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()

def add_fun():
    if rollno.get()=="" or name.get()=="" or class_var.get()=="" or gender.get()=="":
        messagebox.showerror("Error!","Please fill all the fields")
    else:
        conn= pymysql.connect(host="localhost",user="root",password="",database="sms1")
        cur = conn.cursor()
        cur.execute("INSERT INTO studentdata VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),gender.get(),selected_datedob.get(),class_var.get(),section.get(),contact.get(),father_name.get(),address.get()))
        conn.commit()
        conn.close()
        fetch_data() #---> this will fetch data after adding [Means update]

def get_cursor(event):
    cursor_row =std_table.focus()
    content = std_table.item(cursor_row)
    row = content["values"]
    rollno.set(row[0])
    name.set(row[1])
    gender.set(row[2])
    selected_datedob.set(row[3])
    class_var.set(row[4])
    section.set(row[5])
    contact.set(row[6])
    father_name.set(row[7])
    address.set(row[8])

def clear():
    rollno.set("")
    name.set("")
    gender.set("")
    selected_datedob.set("")
    class_var.set("")
    section.set("")
    contact.set("")
    father_name.set("")
    address.set("")

def update_fun():
        conn= pymysql.connect(host="localhost",user="root",password="",database="sms1")
        cur = conn.cursor()
        cur.execute("update studentdata set name=%s,gender=%s,selected_datedob=%s,class=%s,section=%s,contact=%s,father_name=%s,address=%s where rollno=%s",(name.get(),gender.get(),selected_datedob.get(),class_var.get(),section.get(),contact.get(),father_name.get(),address.get(),rollno.get()))
        conn.commit()
       
        fetch_data()
        conn.close()
        clear()

def delete_fun():
        conn= pymysql.connect(host="localhost",user="root",password="",database="sms1")
        cur = conn.cursor()
        cur.execute("DELETE from studentdata where rollno=%s",rollno.get())
        conn.commit()
        conn.close()
        fetch_data()
        clear()
        
def search_data():
    conn= pymysql.connect(host="localhost",user="root",password="",database="sms1")
    cur = conn.cursor()
    query = f"SELECT * FROM studentdata WHERE {search_by.get()} LIKE '%{search_txt.get()}%'"
    cur.execute(query)
    #cur.execute("SELECT * FROM studentdata where"+str(search_by.get())+" LIKE '%"+str(search_txt.get())+"%'")
    rows =cur.fetchall()
    if len(rows)!=0:
        std_table.delete(*std_table.get_children())
        for row in rows:
            std_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()

def show_all():
    fetch_data()

    


#================================#

###*************************************BUTTON**************************************###
btn_frame =tk.Frame(detail_frame,bd=6,relief=tk.GROOVE,bg="lightblue")
btn_frame.place(x=20,y=400,width=360,height=110)

add_btn = tk.Button(btn_frame,text="Add",bg="lightgrey",foreground="red",bd=5,font=("Arail",13),width=15, command=add_fun)
add_btn.grid(row=0,column=0,padx=8,pady=2)

update_btn = tk.Button(btn_frame,text="Update",bg="lightgrey",foreground="red",bd=5,font=("Arail",13),width=15,command=update_fun)
update_btn.grid(row=0,column=1,padx=11,pady=2)

delete_btn = tk.Button(btn_frame,text="Delete",foreground="red",bg="lightgrey",bd=5,font=("Arail",13),width=15,command=delete_fun)
delete_btn.grid(row=1,column=0,padx=11,pady=2)
delete_btn.place(x=7,y=50,width=152,height=39)

clear_btn = tk.Button(btn_frame,text="Clear",foreground="red",bg="lightgrey",bd=5,font=("Arail",13),width=15,command=clear)
clear_btn.grid(row=1,column=1,padx=11,pady=2)
clear_btn.place(x=177,y=50,width=152,height=39)

###*ButtenEnd*******************************************************************************####

#@@@@@====SEARCH====@@@@@@@@

search_frame=tk.Frame(data_frame,bd=9,relief=tk.GROOVE,bg="white")
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl = tk.Label(search_frame,text="Search",bg="white",font=("Arail",14))
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_en = ttk.Combobox(search_frame,font=("Arial",12),state="readonly",textvariable=search_by)
search_en["values"]=('Name','Rollno','Contact','Class','FatherName')
search_en.grid(row=0,column=1,padx=12,pady=2)

search_txt=tk.Entry(search_frame,bd=7,font=("Arail",15),width=13,textvariable=search_txt)
search_txt.grid(row=0,column=2,padx=12,pady=2)


search_btn =tk.Button(search_frame,text="Search",font=("Arial",13),bd=6,bg="lightgray",width=10,command=search_data)
search_btn.grid(row=0,column=3,padx=7,pady=2)

showAll_btn =tk.Button(search_frame,text="Show All",font=("Arial",13),bd=6,bg="lightgray",width=10,command=show_all)
showAll_btn.grid(row=0,column=4,padx=7,pady=2)

#@@@@==========@@@@@#

###$$$$=====DATABASE FRAME======$$$$###

main_frame = tk.Frame(data_frame,bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)


y_scroll =tk.Scrollbar(main_frame,orient=tk.VERTICAL,)
x_scroll =tk.Scrollbar(main_frame,orient=tk.HORIZONTAL,)

std_table = ttk.Treeview(main_frame,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
std_table["columns"]=('Roll No','Name','Gender','D.O.B','Class','Section','Contact','FatherName','Address')

y_scroll.config(command=std_table.yview)
x_scroll.config(command=std_table.xview)
y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

std_table.heading("Roll No",text="Roll No")
std_table.heading("Name",text="Name")
std_table.heading("Gender",text="Gender")
std_table.heading("D.O.B",text="D.O.B")
std_table.heading("Class",text="Class")
std_table.heading("Section",text="Section")
std_table.heading("Contact",text="Contact")
std_table.heading("FatherName",text="FatherName")
std_table.heading("Address",text="Address")



std_table['show']='headings'

std_table.column("Roll No",width=100)
std_table.column("Name",width=100)
std_table.column("Gender",width=100)
std_table.column("D.O.B",width=100)
std_table.column("Class",width=100)
std_table.column("Section",width=100)
std_table.column("Contact",width=100)
std_table.column("FatherName",width=100)
std_table.column("Address",width=100)



std_table.pack(fill=tk.BOTH,expand=True)

fetch_data()
std_table.bind("<ButtonRelease-1>",get_cursor)
win.bind("<Configure>", on_resize)
                      

win.mainloop()