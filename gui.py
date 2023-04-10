import tkinter as tk

class App(tk.Tk):
    def __init__(self, content=[num for num in range(0,100)]):
        super().__init__()
        self.content = content
        self.title("Python Examples!")
        self.geometry('400x300')
        self.resizable(0,0)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)

        self.__create_widgets(content)
        del self.content
    
    def __create_widgets(self, content):
        welcome_message = tk.Frame(self)
        scroll_frame = tk.Frame(self)
        button_frame = tk.Frame(self)

        LabelFrame(welcome_message).grid(column=0, row=0, sticky=tk.NE) # Welcome Message
        ListBoxFrame(scroll_frame, content).grid(column=0, row=1) # List Box and Scroll Bar
        ButtonFrame(button_frame).grid(column=3, row=1, sticky=tk.E)
        # welcome_message.grid(column=2, row=0, sticky=tk.NSEW) # Display the frame for the welcome message
        # scroll_frame.grid(column=0, row=1) # Display the frame for the scroll bar
        for child in self.winfo_children():
            child.grid(padx=5, pady=5) # Give everything a small bit of padding

class LabelFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.__create_widgets()
    
    def __create_widgets(self):
        self.main_label = tk.Label(self, text="Welcome! Please select an option.", width=30).grid(column=1, row=0, sticky=tk.N)

class ButtonFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.__create_widgets()

    def __create_widgets(self):
        tk.Button(self, text="Open", width=5, command=lambda: print("Clicked me!")).grid(column=2, row=0, sticky=tk.E)

class ListBoxFrame(tk.Frame):
    def __init__(self, container, content):
        super().__init__(container)
        self.content = tk.Variable(value=content)

        self.__create_widgets(container)
    
    def __create_widgets(self, container):
        self.sb = tk.Scrollbar(container, orient=tk.VERTICAL) # sb = Scroll Bar
        self.lb = tk.Listbox(container, height=10, width=15, listvariable=self.content, yscrollcommand=self.sb.set).grid(row=0, column=0) # lb = List Box

        self.sb.grid(row=0, column=1, sticky=tk.NS)

        for child in self.winfo_children():
            child.grid(padx=0, pady=5)


app = App()
app.mainloop()