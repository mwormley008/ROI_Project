from tkinter import *
from tkinter import ttk

# root.geometry("1500x1500")
# root.title("My First GUI")



# root.mainloop()

class MyGUI:

    def __init__(self):
        """ Defines the UI """

        self.root = Tk()

        self.root.geometry("1200x1200")
        self.root.title("ROI Calculator")

        self.label = Label(self.root, text="ROI Calculator", font=('Ariel', 18,'underline'))
        self.label.pack()

        # content = Frame(self.root)
        # frame = Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
        # content.grid(column=0, row=0, sticky=(N, S, E, W))
        # frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        
        self.guiframe = Frame(self.root, padx=5, pady=5)
        self.guiframe.columnconfigure(0, weight = 1, pad=5)
        self.guiframe.columnconfigure(1, weight = 1, pad=5)
        self.guiframe.pack(fill='x')
        # Income
        self.labelh1 = Label(self.guiframe, text="Monthly Income", font=('Ariel', 18, 'underline'))
        self.labelh1.grid(row=0, column=0, sticky=W+E)

        self.label1 = Label(self.guiframe, text="Rental Income", font=('Ariel', 18))
        self.label1.grid(row=1, column=0, sticky=W+E)
        self.entry1 = Entry(self.guiframe, font =('Arial', 10))
        self.entry1.grid(row=2, column=0, sticky=W+E)
        # Expenses
        self.labelh2 = Label(self.guiframe, text="Expenses", font=('Ariel', 18, 'underline'))
        self.labelh2.grid(row=3, column=0, sticky=W+E)
        
        self.label2 = Label(self.guiframe, text="Tax", font=('Ariel', 18))
        self.label2.grid(row=4, column=0, sticky=W+E)
        self.entry2 = Entry(self.guiframe, font =('Arial', 10))
        self.entry2.grid(row=5, column=0, sticky=W+E)

        self.label3 = Label(self.guiframe, text="Insurance", font=('Ariel', 18))
        self.label3.grid(row=6, column=0, sticky=W+E)
        self.entry3 = Entry(self.guiframe, font =('Arial', 10))
        self.entry3.grid(row=7, column=0, sticky=W+E)

        self.label4 = Label(self.guiframe, text="Utilities", font=('Ariel', 18))
        self.label4.grid(row=8, column=0, sticky=W+E)
        self.entry4 = Entry(self.guiframe, font =('Arial', 10))
        self.entry4.grid(row=9, column=0, sticky=W+E)

        self.label5 = Label(self.guiframe, text="HOA Fees", font=('Ariel', 18))
        self.label5.grid(row=10, column=0, sticky=W+E)
        self.entry5 = Entry(self.guiframe, font =('Arial', 10))
        self.entry5.grid(row=11, column=0, sticky=W+E)

        # Monthly Cash FLow
        self.label6 = Label(self.guiframe, text="Monthly Cash Flow", font=('Ariel', 18, 'underline'))
        self.label6.grid(row=0, column=1, sticky=W+E)
        self.label7 = Label(self.guiframe, text="", font=('Ariel', 18, 'underline'))
        self.label7.grid(row=1, column=1, sticky=W+E)

        # Cash on Cash ROI
        



        


        self.button = Button(self.root, text="Calculate ROI", font=('Arial',18), command=self.get_data)
        self.button.pack(padx=20, pady=20)
        self.root.mainloop()

    def show_message(self):
        print("Hello World")

    def button_equal(self):
        pass

    def get_data(self):
        #This part gets the information from each cell
        if self.entry1.get() == "":
            rental_income = 0
        else:
            rental_income = int(self.entry1.get())
        
        tax_e = self.entry2.get()

        insurance_e = self.entry3.get()
        util_e = self.entry4.get()
        hoa_e = self.entry5.get()

        list_of_expenses = [tax_e, insurance_e, util_e, hoa_e]
        num_list_of_expenses = []

        for x in list_of_expenses:
            if x == "":
                num_list_of_expenses.append(0)                
            else:
                num_list_of_expenses.append(int(x))
        
        expenses = sum(num_list_of_expenses)
        monthly_cash_flow = rental_income - expenses
        self.label7.config(text= monthly_cash_flow, font= ('Helvetica 13'))

MyGUI()
