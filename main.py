from tkinter import *
from tkinter import filedialog, messagebox, LabelFrame, Text, Checkbutton, BooleanVar
from clearing import DataCleaner


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("480x720")
        self.root.title("Email Management")
        self.root.iconbitmap('_internal/logo.ico')

        # Add widgets to the LabelFrame
        self.filepath = None
        self.create_widgets()

    def show_menu(self, event):
        # Position the menu right below the menubutton
        x = self.theme_selectbox.winfo_rootx()
        y = self.theme_selectbox.winfo_rooty() + self.theme_selectbox.winfo_height()
        self.custom_menu.post(x, y)

    def destroy_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_widgets(self):

        self.destroy_widgets()

        # Create the LabelFrame
        self.labelframe = LabelFrame(self.root, borderwidth=5, relief="flat", padx=5, pady=5)
        self.labelframe.pack(fill="both", expand=True, padx=10, pady=10)

        # Theme select box
        self.theme_var = StringVar(value="Dark")

        # Create a custom Menu for the OptionMenu
        self.custom_menu = Menu(self.root, tearoff=0)

        # Add options to the custom Menu
        self.custom_menu.add_radiobutton(label="Dark", variable=self.theme_var, value="Dark", command=self.configure_appearance)
        self.custom_menu.add_radiobutton(label="Light", variable=self.theme_var, value="Light", command=self.configure_appearance)

        # Create the Menubutton
        self.theme_selectbox = Menubutton(
            self.root,
            textvariable=self.theme_var,
            indicatoron=False
        )
        self.theme_selectbox["menu"] = self.custom_menu
        self.theme_selectbox.place(anchor="nw")
        self.theme_selectbox.bind('<Button-1>', self.show_menu)

        # Logo?
        self.logo = PhotoImage(file="_internal/logo.png")
        self.logo = self.logo.subsample(20, 20)
        self.logo_label = Label(self.labelframe, image=self.logo)
        self.logo_label.pack()
        # Instructions
        self.step1 = Label(self.labelframe, text="Step 1\nChose the .csv file to clean.")
        self.step1.pack(pady=(50, 10))

        self.step2 = Label(self.labelframe, text="Step 2\nIf you need, add emails to exclude from the list.")
        self.step2.pack(pady=10)

        self.step3 = Label(self.labelframe, text="Step 3\nClean emails.")
        self.step3.pack(pady=10)

        # Boolean & checkbutton to see if you want to split by 200;
        self.split_by_200 = BooleanVar()
        self.split_checkbox = Checkbutton(
            self.labelframe,
            text="Split by 200",
            variable=self.split_by_200,
        )
        self.split_checkbox.pack(pady=10)

        # Button to choose file
        self.choose_file_button = Button(self.labelframe, text="Choose File", command=self.choose_file)
        self.choose_file_button.pack(pady=(50, 10))

        # Button to exclude emails
        self.exclude_emails_button = Button(self.labelframe, text="Exclude Emails", command=self.open_exclude_window)
        self.exclude_emails_button.pack(pady=10)

        # Button to clean emails
        self.clean_emails_button = Button(self.labelframe, text="Clean Emails", command=self.clean_emails)
        self.clean_emails_button.pack(pady=10)

        self.configure_appearance()

    def configure_appearance(self):

        background_dark = '#444'
        background_button_dark = '#333'
        active_background_dark = '#555'
        active_foreground_dark = '#bbb'
        foreground_dark = '#bbb'
        background_email_dark = '#666'
        foreground_email_dark = '#ccc'
        
        background_light = '#fff'
        background_button_light = '#eee'
        active_background_light = '#ddd'
        active_foreground_light = '#444'
        foreground_light = '#555'
        background_email_light = '#eee'
        foreground_email_light = '#555'

        self.font = 'Helvetica 14'
        self.email_font = 'Helvetica 12'
        self.background = background_dark if self.theme_var.get() == 'Dark' else background_light
        self.background_button = background_button_dark if self.theme_var.get() == 'Dark' else background_button_light
        self.active_background = active_background_dark if self.theme_var.get() == 'Dark' else active_background_light
        self.active_foreground = active_foreground_dark if self.theme_var.get() == 'Dark' else active_foreground_light
        self.foreground = foreground_dark if self.theme_var.get() == 'Dark' else foreground_light
        self.background_email = background_email_dark if self.theme_var.get() == 'Dark' else background_email_light
        self.foreground_email = foreground_email_dark if self.theme_var.get() == 'Dark' else foreground_email_light

        self.labelframe.configure(background=self.background)
        self.root.configure(background=self.background)

        self.custom_menu.configure(bg=self.background, fg=self.foreground, activebackground=self.active_background, activeforeground=self.foreground)

        self.theme_selectbox.configure(
            borderwidth=0,
            relief="flat",
            bg=self.background,
            fg=self.foreground,
            font="Helvetica 8",
            activebackground=self.active_background,
            activeforeground=self.foreground
        )

        self.logo_label.configure(background=self.background)

        self.step1.configure(background=self.background, foreground=self.foreground, font=self.font)

        self.step2.configure(background=self.background, foreground=self.foreground, font=self.font)

        self.step3.configure(background=self.background, foreground=self.foreground, font=self.font)

        self.split_checkbox.configure(
            bg=self.background,
            fg=self.foreground,
            font=self.font,
            selectcolor=self.background,
            activebackground=self.background,
            activeforeground=self.active_foreground,
            cursor='hand2',
        )

        self.choose_file_button.configure(
            background=self.background_button,
            foreground=self.foreground,
            font=self.font,
            width="100",
            activebackground=self.active_background,
            activeforeground=self.foreground,
            borderwidth=0,
            cursor='hand2',
        )

        self.exclude_emails_button.configure(
            background=self.background_button,
            foreground=self.foreground,
            font=self.font,
            width="100",
            activebackground=self.active_background,
            activeforeground=self.foreground,
            borderwidth=0,
            cursor='hand2',
        )

        self.clean_emails_button.configure(
            background=self.background_button,
            foreground=self.foreground,
            font=self.font,
            width="100",
            activebackground=self.active_background,
            activeforeground=self.foreground,
            borderwidth=0,
            cursor='hand2',
        )

    def choose_file(self):
        self.filepath = filedialog.askopenfilename()

    def open_exclude_window(self):
        # Create a new window for excluding emails
        self.exclude_window = Toplevel(self.root)
        self.exclude_window.title("Exclude Emails")
        self.exclude_window.iconbitmap('_internal/logo.ico')
        self.exclude_window.geometry("800x500")
        self.exclude_window.configure(background=self.background)

        text = ("Enter emails to be excluded from the list on new line ex:\n"
                "email1@mail.com\n"
                "email2@mail.com\n")
        self.label = Label(self.exclude_window, text=text, wraplength=600)
        self.label.configure(background=self.background, foreground=self.foreground, font=self.email_font)
        self.label.pack(pady=10)

        # Create a text widget for entering emails
        self.email_text = Text(self.exclude_window, width=60, height=15)
        self.email_text.configure(background=self.background_email, foreground=self.foreground_email, font=self.email_font, borderwidth=0)
        self.email_text.pack(pady=10)

        # Button to save emails to ignore_emails.txt
        self.save_button = Button(self.exclude_window, text="Exclude Emails", command=self.save_emails)
        self.save_button.configure(
            background=self.background_button,
            foreground=self.foreground,
            font=self.font,
            width="60",
            activebackground=self.active_background,
            activeforeground=self.foreground,
            borderwidth=0,
        )
        self.save_button.pack(pady=10)

    def save_emails(self):
        emails = self.email_text.get("1.0", END)
        with open("_internal/ignore_emails.txt", "a") as file:
            file.write(emails)
        self.exclude_window.destroy()
        messagebox.showinfo("Success", "Emails will be ignored!")

    def clean_emails(self):
        if self.filepath:
            data_cleaner = DataCleaner(self.filepath, self.split_by_200.get())
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

