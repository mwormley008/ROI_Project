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

        self.label6 = Label(self.guiframe, text="Lawn/Snow Care", font=('Ariel', 18))
        self.label6.grid(row=12, column=0, sticky=W+E)
        self.entry6 = Entry(self.guiframe, font =('Arial', 10))
        self.entry6.grid(row=13, column=0, sticky=W+E)

        self.label7 = Label(self.guiframe, text="Vacancy", font=('Ariel', 18))
        self.label7.grid(row=14, column=0, sticky=W+E)
        self.entry7 = Entry(self.guiframe, font =('Arial', 10))
        self.entry7.grid(row=15, column=0, sticky=W+E)

        self.label8 = Label(self.guiframe, text="Repairs", font=('Ariel', 18))
        self.label8.grid(row=16, column=0, sticky=W+E)
        self.entry8 = Entry(self.guiframe, font =('Arial', 10))
        self.entry8.grid(row=17, column=0, sticky=W+E)

        self.label9 = Label(self.guiframe, text="CapEx", font=('Ariel', 18))
        self.label9.grid(row=18, column=0, sticky=W+E)
        self.entry9 = Entry(self.guiframe, font =('Arial', 10))
        self.entry9.grid(row=19, column=0, sticky=W+E)

        self.label10 = Label(self.guiframe, text="Property Management", font=('Ariel', 18))
        self.label10.grid(row=20, column=0, sticky=W+E)
        self.entry10 = Entry(self.guiframe, font =('Arial', 10))
        self.entry10.grid(row=21, column=0, sticky=W+E)

        self.label11 = Label(self.guiframe, text="Mortgage", font=('Ariel', 18))
        self.label11.grid(row=22, column=0, sticky=W+E)
        self.entry11 = Entry(self.guiframe, font =('Arial', 10))
        self.entry11.grid(row=23, column=0, sticky=W+E)

        # Monthly Cash FLow
        self.labelcf = Label(self.guiframe, text="Monthly Cash Flow", font=('Ariel', 18, 'underline'))
        self.labelcf.grid(row=0, column=1, sticky=W+E)
        self.labelmc = Label(self.guiframe, text="", font=('Ariel', 18, 'underline'), background='grey')
        self.labelmc.grid(row=2, column=1, rowspan = 7, sticky=W+E+N+S)

        # Cash on Cash ROI
        self.label12 = Label(self.guiframe, text="ROI", font=('Ariel', 18, 'underline'))
        self.label12.grid(row=9, column=1, sticky=W+E)
        self.label13 = Label(self.guiframe, text="Down Payment", font=('Ariel', 18))
        self.label13.grid(row=10, column=1, sticky=W+E)
        self.entry13 = Entry(self.guiframe, font =('Arial', 10))
        self.entry13.grid(row=11, column=1, sticky=W+E)
        self.label14 = Label(self.guiframe, text="Closing Costs", font=('Ariel', 18))
        self.label14.grid(row=12, column=1, sticky=W+E)
        self.entry14 = Entry(self.guiframe, font =('Arial', 10))
        self.entry14.grid(row=13, column=1, sticky=W+E)
        self.label15 = Label(self.guiframe, text="Rehab Budget", font=('Ariel', 18))
        self.label15.grid(row=14, column=1, sticky=W+E)
        self.entry15 = Entry(self.guiframe, font =('Arial', 10))
        self.entry15.grid(row=15, column=1, sticky=W+E)
        self.label16 = Label(self.guiframe, text="Misc Expenses", font=('Ariel', 18))
        self.label16.grid(row=16, column=1, sticky=W+E)
        self.entry16 = Entry(self.guiframe, font =('Arial', 10))
        self.entry16.grid(row=17, column=1, sticky=W+E)
        
        self.labelr = Label(self.guiframe, text="ROI", font=('Ariel', 18, 'underline'))
        self.labelr.grid(row=18, column=1, sticky=W+E)
        self.labelr = Label(self.guiframe, text="", font=('Ariel', 18, 'underline'), background='grey')
        self.labelr.grid(row=19, column=1, rowspan = 7, sticky=W+E+N+S)


        self.button = Button(self.root, text="Calculate ROI", font=('Arial',18), command=self.get_data)
        self.button.pack(padx=20, pady=20)
        self.root.mainloop()

    # def show_message(self):
    #     print("Hello World")

    # def button_equal(self):
    #     pass

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
        lawn_e = self.entry6.get()
        vac_e = self.entry7.get()
        rep_e = self.entry8.get()
        capex_e = self.entry9.get()
        propmgmt_e = self.entry10.get()
        mort_e = self.entry11.get()
        

        list_of_expenses = [tax_e, insurance_e, util_e, hoa_e, lawn_e, vac_e, rep_e, capex_e, propmgmt_e, mort_e]
        num_list_of_expenses = []

        for x in list_of_expenses:
            if x == "":
                num_list_of_expenses.append(0)                
            else:
                num_list_of_expenses.append(int(x))
        
        expenses = sum(num_list_of_expenses)
        monthly_cash_flow = rental_income - expenses
        #ref_mcf is to use in final calculation
        ref_mcf = monthly_cash_flow
        bg = ""
        if monthly_cash_flow >= 0:
            monthly_cash_flow = f"You're making ${monthly_cash_flow} a month."
            bg = "green"
        else:
            monthly_cash_flow *= -1
            monthly_cash_flow = f"You're losing -${monthly_cash_flow} a month."
            bg = "red"
        self.labelmc.config(text=monthly_cash_flow, font= ('Helvetica 25'), background=bg)

        dp_e = self.entry13.get()
        close_e = self.entry14.get()
        rehab_e = self.entry15.get()
        misc_e = self.entry16.get()

        list_of_sinexpenses = [dp_e, close_e, rehab_e, misc_e]
        num_list_of_sinexpenses = []

        for x in list_of_sinexpenses:
            if x == "":
                num_list_of_sinexpenses.append(0)                
            else:
                num_list_of_sinexpenses.append(int(x))
        
        sinexpenses = sum(num_list_of_sinexpenses)
        if sinexpenses:
            total_roi = (ref_mcf*12) / sinexpenses

            if total_roi >= 0:
                total_roi = f"{total_roi:.2f}%"
                bg = "green"
            else:
                total_roi *= -1
                total_roi = f"-{total_roi:.2f}%"
                bg = "red"
            self.labelr.config(text=total_roi, font= ('Helvetica 20'), background=bg)
        self.root.mainloop()
MyGUI()
