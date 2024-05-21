from tkinter import *
from tkinter import filedialog, messagebox, LabelFrame, Text
from clearing import DataCleaner


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Email Management")
        self.root.iconbitmap('_internal/logo.ico')

        # Create the LabelFrame
        self.labelframe = LabelFrame(self.root, borderwidth=5, relief="flat", padx=5, pady=5)
        self.labelframe.pack(fill="both", expand=True, padx=10, pady=10)
        self.labelframe.configure(background="#444")

        # Add widgets to the LabelFrame
        self.filepath = None
        self.create_widgets()

        self.root.configure(background="#444")

    def create_widgets(self):
        # Logo?
        self.logo = PhotoImage(file="_internal/logo.png")
        self.logo = self.logo.subsample(20, 20)
        self.logo_label = Label(self.labelframe, image=self.logo)
        self.logo_label.configure(background="#444")
        self.logo_label.pack()
        # Instructions
        self.step1 = Label(self.labelframe, text="Step 1\nChose the .csv file to clean.")
        self.step1.configure(background="#444", foreground="#bbb", font="Helvetica 16")
        self.step1.pack(pady=10)

        self.step2 = Label(self.labelframe, text="Step 2\nIf you need, add emails to exclude from the list.")
        self.step2.configure(background="#444", foreground="#bbb", font="Helvetica 16")
        self.step2.pack(pady=10)

        self.step3 = Label(self.labelframe, text="Step 3\nClean emails.")
        self.step3.configure(background="#444", foreground="#bbb", font="Helvetica 16")
        self.step3.pack(pady=10)

        # Button to choose file
        self.choose_file_button = Button(self.labelframe, text="Choose File", command=self.choose_file)
        self.choose_file_button.configure(
            background="#333",
            foreground="#bbb",
            font="Helvetica 16",
            width="100",
            activebackground="#555",
            activeforeground="#bbb",
            borderwidth=0,
        )
        self.choose_file_button.pack(pady=10)

        # Button to exclude emails
        self.exclude_emails_button = Button(self.labelframe, text="Exclude Emails", command=self.open_exclude_window)
        self.exclude_emails_button.configure(
            background="#333",
            foreground="#bbb",
            font="Helvetica 16",
            width="100",
            activebackground="#555",
            activeforeground="#bbb",
            borderwidth=0,
        )
        self.exclude_emails_button.pack(pady=10)

        # Button to clean emails
        self.clean_emails_button = Button(self.labelframe, text="Clean Emails", command=self.clean_emails)
        self.clean_emails_button.configure(
            background="#333",
            foreground="#bbb",
            font="Helvetica 16",
            width="100",
            activebackground="#555",
            activeforeground="#bbb",
            borderwidth=0,
        )
        self.clean_emails_button.pack(pady=10)

    def choose_file(self):
        self.filepath = filedialog.askopenfilename()

    def open_exclude_window(self):
        # Create a new window for excluding emails
        self.exclude_window = Toplevel(self.root)
        self.exclude_window.title("Exclude Emails")
        self.exclude_window.iconbitmap('_internal/logo.ico')
        self.exclude_window.geometry("800x500")
        self.exclude_window.configure(background="#444")

        text = ("Enter emails to be excluded from the list on new line ex:\n"
                "email1@mail.com\n"
                "email2@mail.com\n")
        self.label = Label(self.exclude_window, text=text, wraplength=600)
        self.label.configure(background="#444", foreground="#aaa", font="Helvetica 15")
        self.label.pack(pady=10)

        # Create a text widget for entering emails
        self.email_text = Text(self.exclude_window, width=60, height=15)
        self.email_text.configure(background="#555", foreground="#ccc", font="Helvetica 12", borderwidth=0)
        self.email_text.pack(pady=10)

        # Button to save emails to ignore_emails.txt
        self.save_button = Button(self.exclude_window, text="Exclude Emails", command=self.save_emails)
        self.save_button.configure(
            background="#333",
            foreground="#bbb",
            font="Helvetica 16",
            width="60",
            activebackground="#555",
            activeforeground="#bbb",
            borderwidth=0,
        )
        self.save_button.pack(pady=10)

    def save_emails(self):
        emails = self.email_text.get("1.0", END)
        with open("_internal/ignore_emails.txt", "w") as file:
            file.write(emails)
        self.exclude_window.destroy()
        messagebox.showinfo("Success", "Emails will be ignored!")

    def clean_emails(self):
        if self.filepath:
            data_cleaner = DataCleaner(self.filepath)
            result = data_cleaner.clean_data()
            # Here you would add your logic to clean the emails based on ignore_emails list.
            if result:
                messagebox.showinfo("Success", "Emails are cleaned!")
        else:
            messagebox.showwarning("No File", "Please choose a file first.")

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    root = Tk()
    app = MainWindow(root)
    app.run()

