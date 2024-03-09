from tkinter import *

root = Tk()

def submit():
    print("You meals included!")
    
root.title("Mad-Travels")
root.geometry("600x600")
root.minsize(600,600)
root.maxsize(600,600)
heading = Label(text="Welcome To Mad Travels!",font="comicsansms 14 bold",pady=15).grid(row=0,column=3)

# Text For Our Form
name = Label(root,text="Name")
phone = Label(root,text="Phone")
gender = Label(root,text="Gender")
emergency = Label(root,text="Emergency")
payment = Label(root,text="Payments Mode")

# Pack The Form Using grid
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)

# Define variables for storing entrys
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

# Entry for our form
namevalueentry = Entry(root,textvariable=namevalue)
phonevalueentry = Entry(root,textvariable=phonevalue)
gendervalueentry = Entry(root,textvariable=gendervalue)
emergencyvalueentry = Entry(root,textvariable=emergencyvalue)
paymentvalueentry = Entry(root,textvariable=paymentvalue)

# Pack The Entry Using grid
namevalueentry.grid(row=1,column=3)
phonevalueentry.grid(row=2,column=3)
gendervalueentry.grid(row=3,column=3)
emergencyvalueentry.grid(row=4,column=3)
paymentvalueentry.grid(row=5,column=3)

# checkbox & packing
foodservice = Checkbutton(text="Want to prebook your meals?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

# Button and packing
Button(text="Submit to Mad-Travels!",command=submit).grid(row=7,column=3)


root.mainloop()