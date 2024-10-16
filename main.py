import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="mysql123", 
        database="PetManagement"
    )


from tkinter import messagebox, Frame, Label, Entry, Button, StringVar, Radiobutton, Toplevel, Tk, END

is_admin = False
admin_username = "admin"  # Sample admin username
admin_password = "admin"  # Sample admin password

def login_window():
    global is_admin

    def on_login():
        global is_admin
        if user_type.get() == "Admin":
            # For admin login
            if username.get() == admin_username and password.get() == admin_password:
                is_admin = True
                root.destroy()  # Close login window
                pet_management_gui()
            else:
                messagebox.showerror("Login Error", "Invalid Admin Credentials")
        else:
            # For customer, directly open the main application
            is_admin = False
            root.destroy()  # Close login window
            pet_management_gui()

    root = Tk()
    root.title("Login")

    # Set the background color
    root.configure(bg='white')

    Label(root, text="Select User Type:", bg='white').grid(row=0, column=0, pady=10, padx=10, sticky=W)
    
    user_type = StringVar(value="Customer")
    Radiobutton(root, text="Admin", variable=user_type, value="Admin", bg='white').grid(row=0, column=1)
    Radiobutton(root, text="Customer", variable=user_type, value="Customer", bg='white').grid(row=0, column=2)

    Label(root, text="Username:", bg='white').grid(row=1, column=0, pady=10, padx=10, sticky=W)
    username = Entry(root)
    username.grid(row=1, column=1)

    Label(root, text="Password:", bg='white').grid(row=2, column=0, pady=10, padx=10, sticky=W)
    password = Entry(root, show='*')
    password.grid(row=2, column=1)

    Button(root, text="Login", command=on_login).grid(row=3, columnspan=3, pady=10)

    root.mainloop()
    

# Add new pet
def add_pet():
    conn = connect_db()
    cursor = conn.cursor()

    sql = "INSERT INTO pets (name, species, age, breed, shelter_id) VALUES (%s, %s, %s, %s, %s)"
    val = (pet_name.get(), pet_species.get(), pet_age.get(), pet_breed.get(), pet_shelter_id.get())
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Success", "Pet added successfully!")
    
    conn.close()

# View pets
def view_pets():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pets")
    records = cursor.fetchall()

    view_window = Toplevel()
    view_window.title("View Pets")

    tree = ttk.Treeview(view_window)
    tree.pack()

    # Get column names
    cursor.execute("DESCRIBE pets")
    columns = [col[0] for col in cursor.fetchall()]

    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for row in records:
        tree.insert('', 'end', values=row)

    conn.close()

# Add new adopter
def add_adopter():
    conn = connect_db()
    cursor = conn.cursor()

    sql = "INSERT INTO adopter (name, contact_info, address) VALUES (%s, %s, %s)"
    val = (adopter_name.get(), adopter_contact.get(), adopter_address.get())
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Success", "Adopter added successfully!")

    conn.close()

# View adopters
def view_adopters():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM adopter")  # Ensure this table name matches your schema
    records = cursor.fetchall()

    view_window = Toplevel()
    view_window.title("View Adopters")

    tree = ttk.Treeview(view_window)
    tree.pack()

    # Get column names
    cursor.execute("DESCRIBE adopter")  # Ensure this table name matches your schema
    columns = [col[0] for col in cursor.fetchall()]

    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for row in records:
        tree.insert('', 'end', values=row)

    conn.close()

# Add new daycare entry
def add_daycare_entry():
    if not all([daycare_facility_name.get(), daycare_pet_name.get(), daycare_owner_name.get(), daycare_contact.get(), daycare_check_in.get(), daycare_check_out.get(), daycare_shelter_id.get(), daycare_capacity.get(), daycare_availability.get()]):
        messagebox.showwarning("Input Error", "All fields must be filled!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    sql = "INSERT INTO daycare (shelter_id, facility_name, capacity, pet_name, owner_name, contact_number, check_in_date, check_out_date, availability) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (daycare_shelter_id.get(), daycare_facility_name.get(), daycare_capacity.get(), daycare_pet_name.get(), daycare_owner_name.get(), daycare_contact.get(), daycare_check_in.get(), daycare_check_out.get(), daycare_availability.get())
    
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Success", "Daycare entry added successfully!")
    
    conn.close()


# View daycare records
def view_daycare_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM daycare")
    records = cursor.fetchall()

    view_window = Toplevel()
    view_window.title("View Daycare Data")

    tree = ttk.Treeview(view_window)
    tree.pack()

    # Get column names
    cursor.execute("DESCRIBE daycare")
    columns = [col[0] for col in cursor.fetchall()]

    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for row in records:
        tree.insert('', 'end', values=row)

    conn.close()


# Add new shelter
def add_shelter():
    conn = connect_db()
    cursor = conn.cursor()

    sql = "INSERT INTO shelters (name, location, capacity) VALUES (%s, %s, %s)"
    val = (shelter_name.get(), shelter_location.get(), shelter_capacity.get())
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Success", "Shelter added successfully!")

    conn.close()

# View shelters
def view_shelters():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shelters")
    records = cursor.fetchall()

    view_window = Toplevel()
    view_window.title("View Shelters")

    tree = ttk.Treeview(view_window)
    tree.pack()

    # Get column names
    cursor.execute("DESCRIBE shelters")
    columns = [col[0] for col in cursor.fetchall()]

    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for row in records:
        tree.insert('', 'end', values=row)

    conn.close()

# Add new adoption entry
def add_adoption():
    conn = connect_db()
    cursor = conn.cursor()

    sql = "INSERT INTO adoption (pet_id, adopter_id, adoption_date) VALUES (%s, %s, %s)"
    val = (adoption_pet_id.get(), adoption_adopter_id.get(), adoption_date.get())
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Success", "Adoption added successfully!")

    conn.close()

# View adoption records
def view_adoptions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM adoption")
    records = cursor.fetchall()

    view_window = Toplevel()
    view_window.title("View Adoptions")

    tree = ttk.Treeview(view_window)
    tree.pack()

    # Get column names
    cursor.execute("DESCRIBE adoption")
    columns = [col[0] for col in cursor.fetchall()]

    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for row in records:
        tree.insert('', 'end', values=row)

    conn.close()

# GUI for pet management system

def pet_management_gui():
    global pet_name, pet_species, pet_age, pet_breed, pet_shelter_id
    global adopter_name, adopter_contact, adopter_address
    global daycare_shelter_id, daycare_facility_name, daycare_capacity, daycare_availability, daycare_pet_name, daycare_owner_name, daycare_contact, daycare_check_in, daycare_check_out 
    global shelter_name, shelter_location, shelter_capacity
    global adoption_pet_id, adoption_adopter_id, adoption_date

    root = Tk()
    root.title("Pet Management System")
    root.geometry("600x600")  # Set a fixed size for better layout
    root.configure(bg="white")  # Set background color to white

    # Create tab control
    tab_control = ttk.Notebook(root)

    # Create a common style for labels and entries
    style = ttk.Style()
    style.configure("TLabel", background="lightgrey", font=("Arial", 10))
    style.configure("TEntry", font=("Arial", 10), fieldbackground="lightgrey")

    # Create Pet Tab
    pet_tab = Frame(tab_control, bg="white")
    tab_control.add(pet_tab, text='Pets')

    # Pet Tab Entries
    Label(pet_tab, text="Pet Name", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
    pet_name = Entry(pet_tab, bg="lightgrey")
    pet_name.grid(row=0, column=1, padx=10, pady=5)

    Label(pet_tab, text="Species", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
    pet_species = Entry(pet_tab, bg="lightgrey")
    pet_species.grid(row=1, column=1, padx=10, pady=5)

    Label(pet_tab, text="Age", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
    pet_age = Entry(pet_tab, bg="lightgrey")
    pet_age.grid(row=2, column=1, padx=10, pady=5)

    Label(pet_tab, text="Breed", bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
    pet_breed = Entry(pet_tab, bg="lightgrey")
    pet_breed.grid(row=3, column=1, padx=10, pady=5)

    Label(pet_tab, text="Shelter ID", bg="white").grid(row=4, column=0, padx=10, pady=5, sticky=W)
    pet_shelter_id = Entry(pet_tab, bg="lightgrey")
    pet_shelter_id.grid(row=4, column=1, padx=10, pady=5)
    
    if is_admin:
        Button(pet_tab, text="Add Pet", command=add_pet, bg="#4CAF50", fg="white").grid(row=5, columnspan=2, pady=10)
        Button(pet_tab, text="View Pets", command=view_pets, bg="#2196F3", fg="white").grid(row=6, columnspan=2)
    
    else:
        Button(pet_tab, text="View Pets", command=view_pets, bg="#2196F3", fg="white").grid(row=6, columnspan=2)
    

    # Create Adopter Tab
    adopter_tab = Frame(tab_control, bg="white")
    tab_control.add(adopter_tab, text='Adopters')

    # Adopter Tab Entries

    if is_admin:
        Label(adopter_tab, text="Owner Name", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        adopter_name = Entry(adopter_tab, bg="lightgrey")
        adopter_name.grid(row=0, column=1, padx=10, pady=5)

        Label(adopter_tab, text="Contact Number", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        adopter_contact = Entry(adopter_tab, bg="lightgrey")
        adopter_contact.grid(row=1, column=1, padx=10, pady=5)

        Label(adopter_tab, text="Address", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        adopter_address = Entry(adopter_tab, bg="lightgrey")
        adopter_address.grid(row=2, column=1, padx=10, pady=5)

        Button(adopter_tab, text="Add Adopter", command=add_adopter, bg="#4CAF50", fg="white").grid(row=3, columnspan=2, pady=10)
        Button(adopter_tab, text="View Adopters", command=view_adopters, bg="#2196F3", fg="white").grid(row=4, columnspan=2)
    else:
        Button(adopter_tab, text="View Adopters", command=view_adopters, bg="#2196F3", fg="white").grid(row=4, columnspan=2)
    

    # Create Daycare Tab
    daycare_tab = Frame(tab_control, bg="white")
    tab_control.add(daycare_tab, text='Daycare')

    # Daycare Tab Entries
    if is_admin:
        Label(daycare_tab, text="Shelter ID", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        daycare_shelter_id = Entry(daycare_tab, bg="lightgrey")
        daycare_shelter_id.grid(row=0, column=1, padx=10, pady=5)

        Label(daycare_tab, text="Facility Name", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        daycare_facility_name = Entry(daycare_tab, bg="lightgrey")
        daycare_facility_name.grid(row=1, column=1, padx=10, pady=5)

        Label(daycare_tab, text="Capacity", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        daycare_capacity = Entry(daycare_tab, bg="lightgrey")
        daycare_capacity.grid(row=2, column=1, padx=10, pady=5)

        Label(daycare_tab, text="Availability (1/0)", bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        daycare_availability = Entry(daycare_tab, bg="lightgrey")
        daycare_availability.grid(row=3, column=1, padx=10, pady=5)

        Label(daycare_tab, text="Pet Name", bg="white").grid(row=4, column=0, padx=10, pady=5, sticky=W)
        daycare_pet_name = Entry(daycare_tab, bg="lightgrey")
        daycare_pet_name.grid(row=4, column=1, padx=10, pady=5)

        Label(daycare_tab, text="Owner Name", bg="white").grid(row=5, column=0, padx=10, pady=5, sticky=W)
        daycare_owner_name = Entry(daycare_tab, bg="lightgrey")
        daycare_owner_name.grid(row=5, column=1, padx=10, pady=5)

        Label(daycare_tab, text="Contact Number", bg="white").grid(row=6, column=0, padx=10, pady=5, sticky=W)
        daycare_contact = Entry(daycare_tab, bg="lightgrey")
        daycare_contact.grid(row=6, column=1, padx=10, pady=5)

        Label(daycare_tab, text="Check-in Date", bg="white").grid(row=7, column=0, padx=10, pady=5, sticky=W)
        daycare_check_in = Entry(daycare_tab, bg="lightgrey")
        daycare_check_in.grid(row=7, column=1, padx=10, pady=5)

        Label(daycare_tab, text="Check-out Date", bg="white").grid(row=8, column=0, padx=10, pady=5, sticky=W)
        daycare_check_out = Entry(daycare_tab, bg="lightgrey")
        daycare_check_out.grid(row=8, column=1, padx=10, pady=5)

        Button(daycare_tab, text="Add Daycare Entry", command=add_daycare_entry, bg="#4CAF50", fg="white").grid(row=9, columnspan=2, pady=10)
        Button(daycare_tab, text="View Daycare Data", command=view_daycare_data, bg="#2196F3", fg="white").grid(row=10, columnspan=2)
    

    # Create Shelter Tab
    shelter_tab = Frame(tab_control, bg="white")
    tab_control.add(shelter_tab, text='Shelters')

    # Shelter Tab Entries
    if is_admin:
        Label(shelter_tab, text="Shelter Name", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        shelter_name = Entry(shelter_tab, bg="lightgrey")
        shelter_name.grid(row=0, column=1, padx=10, pady=5)

        Label(shelter_tab, text="Location", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        shelter_location = Entry(shelter_tab, bg="lightgrey")
        shelter_location.grid(row=1, column=1, padx=10, pady=5)

        Label(shelter_tab, text="Capacity", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        shelter_capacity = Entry(shelter_tab, bg="lightgrey")
        shelter_capacity.grid(row=2, column=1, padx=10, pady=5)

        Button(shelter_tab, text="Add Shelter", command=add_shelter, bg="#4CAF50", fg="white").grid(row=3, columnspan=2, pady=10)
        Button(shelter_tab, text="View Shelters", command=view_shelters, bg="#2196F3", fg="white").grid(row=4, columnspan=2)
    else:
        Button(shelter_tab, text="View Shelters", command=view_shelters, bg="#2196F3", fg="white").grid(row=4, columnspan=2)
    

    # Create Adoption Tab
    adoption_tab = Frame(tab_control, bg="white")
    tab_control.add(adoption_tab, text='Adoptions')

    # Adoption Tab Entries
    if is_admin:
        Label(adoption_tab, text="Pet ID", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        adoption_pet_id = Entry(adoption_tab, bg="lightgrey")
        adoption_pet_id.grid(row=0, column=1, padx=10, pady=5)

        Label(adoption_tab, text="Adopter ID", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        adoption_adopter_id = Entry(adoption_tab, bg="lightgrey")
        adoption_adopter_id.grid(row=1, column=1, padx=10, pady=5)

        Label(adoption_tab, text="Adoption Date", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        adoption_date = Entry(adoption_tab, bg="lightgrey")
        adoption_date.grid(row=2, column=1, padx=10, pady=5)

        Button(adoption_tab, text="Add Adoption", command=add_adoption, bg="#4CAF50", fg="white").grid(row=3, columnspan=2, pady=10)
        Button(adoption_tab, text="View Adoptions", command=view_adoptions, bg="#2196F3", fg="white").grid(row=4, columnspan=2)
    

    # Pack tabs
    tab_control.pack(expand=1, fill='both')

    # Main loop
    root.mainloop()

if __name__ == "__main__":
    root = Tk()  # Create the root window
    root.withdraw()  # Hide the root window
    login_window()  # Show the login window
    root.mainloop()  # Start the main loop