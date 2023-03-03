import tkinter as tk


# root.geometry("1500x1500")
# root.title("My First GUI")



# root.mainloop()

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("1200x1200")
        self.root.title("ROI Calculator")

        self.label = tk.Label(self.root, text="ROI Calculator", font=('Ariel', 18))
        self.label.pack()
        
        self.guiframe = tk.Frame(self.root)
        self.guiframe.columnconfigure(0, weight = 1)
        self.guiframe.columnconfigure(1, weight = 2)
        self.guiframe.pack(fill='x')
        # Income
        self.labelh1 = tk.Label(self.guiframe, text="Monthly Income", font=('Ariel', 18))
        self.labelh1.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.label1 = tk.Label(self.guiframe, text="Rental Income", font=('Ariel', 18))
        self.label1.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.entry1 = tk.Entry(self.guiframe, font =('Arial', 10))
        self.entry1.grid(row=2, column=0, sticky=tk.W+tk.E)
        # Expenses
        self.labelh2 = tk.Label(self.guiframe, text="Expenses", font=('Ariel', 18))
        self.labelh2.grid(row=3, column=0, sticky=tk.W+tk.E)
        
        self.label2 = tk.Label(self.guiframe, text="Tax", font=('Ariel', 18))
        self.label2.grid(row=4, column=0, sticky=tk.W+tk.E)
        self.entry2 = tk.Entry(self.guiframe, font =('Arial', 10))
        self.entry2.grid(row=5, column=0, sticky=tk.W+tk.E)

        self.label3 = tk.Label(self.guiframe, text="Insurance", font=('Ariel', 18))
        self.label3.grid(row=6, column=0, sticky=tk.W+tk.E)
        self.entry3 = tk.Entry(self.guiframe, font =('Arial', 10))
        self.entry3.grid(row=7, column=0, sticky=tk.W+tk.E)

        self.label4 = tk.Label(self.guiframe, text="Utilities", font=('Ariel', 18))
        self.label4.grid(row=8, column=0, sticky=tk.W+tk.E)
        self.entry4 = tk.Entry(self.guiframe, font =('Arial', 10))
        self.entry4.grid(row=9, column=0, sticky=tk.W+tk.E)

        self.label5 = tk.Label(self.guiframe, text="HOA Fees", font=('Ariel', 18))
        self.label5.grid(row=10, column=0, sticky=tk.W+tk.E)
        self.entry5 = tk.Entry(self.guiframe, font =('Arial', 10))
        self.entry5.grid(row=11, column=0, sticky=tk.W+tk.E)

        # Monthly Cash FLow
        self.label6 = tk.Label(self.guiframe, text="Monthly Cash Flow", font=('Ariel', 18))
        self.label6.grid(row=0, column=1, sticky=tk.W+tk.E)

        # Cash on Cash ROI
        



        


        self.button = tk.Button(self.root, text="Calculate ROI", font=('Arial',18))
        self.button.pack(padx=20, pady=20)
        self.root.mainloop()

MyGUI()
