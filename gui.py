import tkinter as tk
from tkinter import messagebox
from main import WebAutomation


class App:
    def __init__(self, root):
        self.root=root
        self.root.title("Web Automation GUI")

        #login frame
        self.login_frame=tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, sticky='w')
        self.entry_username=tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, sticky='ew')

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, sticky='w')
        self.entry_password=tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, sticky='ew')

    
        #form submission
        self.form_frame=tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, text="Full Name").grid(row=0, column=0, sticky='w')
        self.entry_fullname=tk.Entry(self.form_frame)
        self.entry_fullname.grid(row=0, column=1, sticky='ew')

        tk.Label(self.form_frame, text="Email").grid(row=1, column=0, sticky='w')
        self.entry_email=tk.Entry(self.form_frame)
        self.entry_email.grid(row=1, column=1, sticky='ew')

        tk.Label(self.form_frame, text="Current address").grid(row=2, column=0, sticky='w')
        self.entry_currentaddress=tk.Entry(self.form_frame)
        self.entry_currentaddress.grid(row=2, column=1, sticky='ew')

        tk.Label(self.form_frame, text="Permanent address").grid(row=3, column=0, sticky='w')
        self.entry_permanentaddress=tk.Entry(self.form_frame)
        self.entry_permanentaddress.grid(row=3, column=1, sticky='ew')

        #buttons
        self.button_frame=tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)

        tk.Button(self.button_frame, text= "Submit", command= self.submit_button).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text= "Close Browser", command= self.close_browser).grid(row=0, column=1, padx=5)

    def submit_button(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        full_name = self.entry_fullname.get()
        email = self.entry_email.get()
        current_address = self.entry_currentaddress.get()
        permanent_address = self.entry_permanentaddress.get()

        self.wa = WebAutomation()
        self.wa.login(username, password)
        self.wa.fill_form(full_name, email, current_address, permanent_address)


    def close_browser(self):
        self.wa.close()
        messagebox.showinfo("Browser close", "Submitted Successfully.")

  
root=tk.Tk()
app=App(root)
root.mainloop()