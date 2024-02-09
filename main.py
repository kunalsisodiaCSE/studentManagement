from tkinter import *
from tkinter import ttk
from pymongo import *
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x690+1+1')
        self.root.title('School Record')
        self.root.configure(background='#C3ACD0')
        self.root.resizable(False,False)
        title = Label(self.root,
              text = 'Student Registration',
              bg = '#2981A0',
              font = ('poppins',14,'bold'),
              fg="white"
                      )
        title.pack(fill=X)
        
        # Frame Management
        Frame_management = Frame(self.root, bg='#C1F0E9')
        Frame_management.place(x=1137,y=30,width=210,height=400)
        
        # Variables
        self.id = StringVar()
        self.Name = StringVar()
        self.Email = StringVar()
        self.Phone = StringVar()
        self.certificates = StringVar()
        self.gender = StringVar()
        self.Address = StringVar()
        self.delete = StringVar()
        self.search = StringVar()
        self.search_var = StringVar()
        
        # ID
        Id_label = Label(Frame_management, text= "ID (int)", bg="#C1F0E9")
        Id_label.pack()
        Entry_id = Entry(Frame_management, bd='2', textvariable= self.id, justify='center')
        Entry_id.pack()
        
        # Name
        Name_label = Label(Frame_management, text="Student Name", bg="#C1F0E9")
        Name_label.pack()
        Entry_Name = Entry(Frame_management, bd='2', textvariable= self.Name, justify='center')
        Entry_Name.pack()
        
        # Email
        Email_label = Label(Frame_management, text="Student Email", bg="#C1F0E9")
        Email_label.pack()
        Entry_Email = Entry(Frame_management, bd='2', textvariable= self.Email, justify='center')
        Entry_Email.pack()
        
        # Phone
        Phone_label = Label(Frame_management, text="Student Phone", bg="#C1F0E9")
        Phone_label.pack()
        Entry_Phone = Entry(Frame_management, bd='2', textvariable= self.Phone, justify='center')
        Entry_Phone.pack()
        
        # Certificates
        certificates_label = Label(Frame_management, text="Student Certificates", bg="#C1F0E9")
        certificates_label.pack()
        Entry_certificates = Entry(Frame_management, bd='2', textvariable= self.certificates, justify='center')
        Entry_certificates.pack()
        
        # Gender
        Gender_label = Label(Frame_management, text="Student Gender", bg="#C1F0E9")
        Gender_label.pack()
        Entry_Gender = ttk.Combobox(Frame_management, textvariable= self.gender)
        Entry_Gender['value'] = ('Male', 'Female')
        Entry_Gender.pack()
        
        # Address
        Address_label = Label(Frame_management, text="Student Address", bg="#C1F0E9")
        Address_label.pack()
        Entry_Address = Entry(Frame_management, bd='2', textvariable= self.Address, justify='center')
        Entry_Address.pack()
        
        # Delete
        Delete_label = Label(Frame_management, fg='red', text="Delete Student (ID)", bg="#C1F0E9")
        Delete_label.pack()
        Entry_Delete = Entry(Frame_management, bd='2', textvariable= self.delete, justify='center')
        Entry_Delete.pack()
        
        # Control Panel
        Frame_buttons = Frame(self.root, bg='#25B8A2')
        Frame_buttons.place(x=1137, y=437, width=210, height=253)
        
        # Control Panel Label
        Control_Panel_label = Label(Frame_buttons, fg='black', text="Control Panel", bg="#2981A0")
        Control_Panel_label.pack(fill=X)
        
        # Buttons
        add_btn= Button(Frame_buttons, text="Add", bg="#6CE50D", fg="black", command=self.Add_Student)
        add_btn.place(x=33,y=33,width=150,height=33)

        delete_btn = Button(Frame_buttons, text="Delete", bg="#D32E06", fg="black", command=self.Delete)
        delete_btn.place(x=33,y=70,width=150,height=33)

        update_btn = Button(Frame_buttons, text="Update", bg="#6CE50D", fg="black", command=self.Update)
        update_btn.place(x=33,y=107,width=150,height=33)

        clear_btn = Button(Frame_buttons, text="Clear", bg="#6CE50D", fg="black", command=self.Clear)
        clear_btn.place(x=33,y=144,width=150,height=33)

        about_btn = Button(Frame_buttons, text="About us", bg="#6CE50D", fg="black", command=self.About)
        about_btn.place(x=33,y=181,width=150,height=33)

        exit_btn = Button(Frame_buttons, text="Exit", bg="#D32E06", fg="black", command=root.quit)
        exit_btn.place(x=33,y=218,width=150,height=33)

        # Frame Search
        Frame_search = Frame(self.root, bg='white')
        Frame_search.place(x=1, y=30, width=1134, height=30)
        
        # Search
        Search_Label = ttk.Combobox(Frame_search, textvariable=self.search_var, justify='center')
        Search_Label['value'] = ('_id', 'Name', 'Gender', 'Phone')
        Search_Label.place(x=880, y=12)

        Entry_Search = Entry(Frame_search, bd='2', textvariable=self.search, justify='center')
        Entry_Search.place(x=730, y=12)

        Search_btn = Button(Frame_search, text="Search", bg="#5142E4", fg="white", command=self.Search)
        Search_btn.place(x=620, y=2, width=100, height=30)

        # Frame Data
        Frame_data = Frame(self.root, bg='#2981A0')
        Frame_data.place(x=1, y=60, width=1134, height=630)

        Scroll_X = Scrollbar(Frame_data, orient=HORIZONTAL)
        Scroll_Y = Scrollbar(Frame_data, orient=VERTICAL)

        self.student_table = ttk.Treeview(Frame_data,
                                          columns = ('ID', 'Name', 'Email', 'Phone', 'Certificates', 'Gender', 'Address'),
                                          xscrollcommand = Scroll_X.set,
                                          yscrollcommand = Scroll_Y.set
                                          )
        self.student_table.place(x=18,y=1,width=1130,height=600)
        Scroll_X.pack(side=BOTTOM, fill=X)
        Scroll_Y.pack(side=LEFT, fill=Y)

        self.student_table['show'] = 'headings'
        self.student_table.heading('ID', text="ID")
        self.student_table.heading('Name', text="Name")
        self.student_table.heading('Email', text="Email")
        self.student_table.heading('Phone', text="Phone")
        self.student_table.heading('Certificates', text="Certificates")
        self.student_table.heading('Gender', text="Gender")
        self.student_table.heading('Address', text="Address")

        self.student_table.column('ID', width=17)
        self.student_table.column('Name', width=100)
        self.student_table.column('Email', width=70)
        self.student_table.column('Phone', width=65)
        self.student_table.column('Certificates', width=65)
        self.student_table.column('Gender', width=30)
        self.student_table.column('Address', width=125)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_all()
        
    def Add_Student(self):
        cnx = MongoClient(host='localhost', port=27017)
        db = cnx.SchoolManagement
        Student_Coll = db.Students
        Student = {"_id" : self.id.get(),
                   "Name": self.Name.get(),
                   "Email": self.Email.get(),
                   "Phone": self.Phone.get(),
                   "Certificates" : self.certificates.get(),
                   "Gender" : self.gender.get(),
                   "Address" : self.Address.get()
                   }
        Student_Coll.insert_one(Student)
        self.fetch_all()
        self.Clear()

    def fetch_all(self):
        cnx = MongoClient(host='localhost', port=27017)
        db = cnx.SchoolManagement

        collection = db['Students']
        rows = list(collection.find())

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=list(row.values()))

    def Delete(self):
        cnx = MongoClient(host='localhost', port=27017)
        db = cnx.SchoolManagement
        collection = db['Students']

        collection.delete_one({'_id' : self.delete.get()})
        self.fetch_all()

    def Clear(self):
        self.id.set('')
        self.Name.set('')
        self.Email.set('')
        self.Phone.set('')
        self.certificates.set('')
        self.gender.set('')
        self.Address.set('')
        self.delete.set('')

    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.id.set(row[0])
        self.Name.set(row[1])
        self.Email.set(row[2])
        self.Phone.set(row[3])
        self.certificates.set(row[4])
        self.gender.set(row[5])
        self.Address.set(row[6])

    def Update(self):
        cnx = MongoClient(host='localhost', port=27017)
        db = cnx.SchoolManagement
        Student_Coll = db.Students
        Student = {
                   "Name": self.Name.get(),
                   "Email": self.Email.get(),
                   "Phone": self.Phone.get(),
                   "Certificates": self.certificates.get(),
                   "Gender": self.gender.get(),
                   "Address": self.Address.get()
                   }
        Student_Coll.update_one({"_id": self.id.get()}, {"$set" : Student})
        self.fetch_all()
        self.Clear()

    def Search(self):
        cnx = MongoClient(host='localhost', port=27017)
        db = cnx.SchoolManagement

        collection = db['Students']
        rows = list(collection.find({str(self.search_var.get()) : str(self.search.get())}))

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=list(row.values()))

    def About(self):
        messagebox.showinfo('Kunal Sisodia', 'Contact: 70xxxxx220 Email: kunalsisodia98@gmail.com')

root = Tk()
object = Student(root)
root.mainloop()
