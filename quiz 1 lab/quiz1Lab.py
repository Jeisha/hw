from tkinter import *

def submit():
    print('Name        : {0} {1}'.format(entryFirstName.get(),entryLastName.get()))
    print('Address 1   :',entryAddressLine1.get())
    print('Address 2   :',entryAddressLine2.get())
    print('City        :',entryCity.get())
    print('State       :',entryState.get())
    print('Postal Code :',entryPostalCode.get())
    print('Country     :',entryCountry.get())



def clear():
    entryFirstName.delete(0,END)
    entryLastName.delete(0,END)
    entryAddressLine1.delete(0,END)
    entryAddressLine2.delete(0,END)
    entryCity.delete(0,END)
    entryState.delete(0,END)
    entryPostalCode.delete(0,END)
    entryCountry.delete(0,END)

window = Tk()

window.title('Lab Quiz 1 18000960')

inputFrame = LabelFrame(window, relief = SUNKEN)
inputFrame.pack(side=TOP, padx=10, pady=4)

lblFirstName = Label(inputFrame, text='First Name:', font=('Arial',12), fg='black')
lblFirstName.grid(row=0,column=0,sticky=E)
entryFirstName = Entry(inputFrame,font=('Arial',12),fg='black',width=30)
entryFirstName.grid(row=0,column=1)

lblLastName = Label(inputFrame, text='Last Name:', font=('Arial',12), fg='black')
lblLastName.grid(row=1,column=0,sticky=E)
entryLastName = Entry(inputFrame,font=('Arial',12),fg='black',width=30)
entryLastName.grid(row=1,column=1)

lblAddressLine1 = Label(inputFrame, text='Address Line 1:', font=('Arial',12), fg='black')
lblAddressLine1.grid(row=2,column=0,sticky=E)
entryAddressLine1 = Entry(inputFrame,font=('Arial',12),fg='black',width=30)
entryAddressLine1.grid(row=2,column=1)

lblAddressLine2 = Label(inputFrame, text='Address Line 2:', font=('Arial',12), fg='black')
lblAddressLine2.grid(row=3,column=0,sticky=E)
entryAddressLine2 = Entry(inputFrame,font=('Arial',12),fg='black',width=30)
entryAddressLine2.grid(row=3,column=1)

lblCity = Label(inputFrame, text='City:', font=('Arial',12), fg='black')
lblCity.grid(row=4,column=0,sticky=E)
entryCity = Entry(inputFrame,font=('Arial',12),fg='black',width=30)
entryCity.grid(row=4,column=1)

lblState = Label(inputFrame, text='State/Province:', font=('Arial',12), fg='black')
lblState.grid(row=5,column=0,sticky=E)
entryState = Entry(inputFrame,font=('Arial',12),fg='black',width=30)
entryState.grid(row=5,column=1)

lblPostalCode = Label(inputFrame, text='Postal Code:', font=('Arial',12), fg='black')
lblPostalCode.grid(row=6,column=0 ,sticky=E)
entryPostalCode = Entry(inputFrame,font=('Arial',12),fg='black',width=30)
entryPostalCode.grid(row=6,column=1)

lblCountry = Label(inputFrame, text='Country:', font=('Arial',12), fg='black')
lblCountry.grid(row=7,column=0,sticky=E)
entryCountry = Entry(inputFrame,font=('Arial',12),fg='black',width=30)
entryCountry.grid(row=7,column=1)

buttonSubmit = Button(window,text='Submit',width = 10,command = submit)
buttonSubmit.pack(side=RIGHT,padx=10,pady=4)
buttonClear = Button(window,text='Clear',width = 10,command =clear)
buttonClear.pack(side=RIGHT,padx=10,pady=4)

window.mainloop()