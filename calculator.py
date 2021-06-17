# from tkinter import *
import tkinter
# cal = tkinter.Tk()
# cal.title("CALCULATOR")
# cal.geometry("500x500")
# def clicked():
#     lab_1 = Label(cal, text="1")
#     lab_1.grid(row=0, column=0)
# num_1 = Button(cal, text="1", relief="sunken", command=clicked)
# num_1.grid(row=1, column=0)
#entry = Text(cal, relief='sunken', width=50, height=5)
#entry.grid(row=0, column=0)
# myFont = font.Font(size=50)
# entry['font'] = myFont
# #relief='sunken'
# cal.mainloop()



#---------------------------------------START----------------------------------------
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression in the text entry box
def press(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialze the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	cal = Tk()

	# set the background colour of cal window
	cal.configure(background="grey")

	# set the title of cal window
	cal.title("Basic Calculator")

	# set the configuration of cal window
    # cal.resizable(0,0)
    ## cal.attributes(toolwindow=1)
	cal.maxsize(width=247, height=410)
#	cal.minsize(width=247, height=410)

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	# create the text entry box for
	# showing the expression .
	expression_field = Entry(cal, textvariable=equation, background="grey", font=("default",13), 
    justify=RIGHT, borderwidth=0)

	expression_field.grid(columnspan=3)
#columnspan=4, ipadx=50

	button1 = Button(cal, text=' 1 ', fg='white', bg='black',
					command=lambda: press(1), height=5, width=8, borderwidth=0)
	button1.grid(row=2, column=0)

	button2 = Button(cal, text=' 2 ', fg='white', bg='black',
					command=lambda: press(2), height=5, width=8, borderwidth=0)
	button2.grid(row=2, column=1)

	button3 = Button(cal, text=' 3 ', fg='white', bg='black',
					command=lambda: press(3), height=5, width=8, borderwidth=0)
	button3.grid(row=2, column=2)

	button4 = Button(cal, text=' 4 ', fg='white', bg='black',
					command=lambda: press(4), height=5, width=8, borderwidth=0)
	button4.grid(row=3, column=0)

	button5 = Button(cal, text=' 5 ', fg='white', bg='black',
					command=lambda: press(5), height=5, width=8, borderwidth=0)
	button5.grid(row=3, column=1)

	button6 = Button(cal, text=' 6 ', fg='white', bg='black',
					command=lambda: press(6), height=5, width=8, borderwidth=0)
	button6.grid(row=3, column=2)

	button7 = Button(cal, text=' 7 ', fg='white', bg='black',
					command=lambda: press(7), height=5, width=8, borderwidth=0)
	button7.grid(row=4, column=0)

	button8 = Button(cal, text=' 8 ', fg='white', bg='black',
					command=lambda: press(8), height=5, width=8, borderwidth=0)
	button8.grid(row=4, column=1)

	button9 = Button(cal, text=' 9 ', fg='white', bg='black',
					command=lambda: press(9), height=5, width=8, borderwidth=0)
	button9.grid(row=4, column=2)

	button0 = Button(cal, text=' 0 ', fg='white', bg='black',
					command=lambda: press(0), height=5, width=8, borderwidth=0)
	button0.grid(row=5, column=0)

	plus = Button(cal, text=' + ', fg='white', bg='navy blue',
				command=lambda: press("+"), height=5, width=8, borderwidth=0)
	plus.grid(row=2, column=3)

	minus = Button(cal, text=' - ', fg='white', bg='navy blue',
				command=lambda: press("-"), height=5, width=8, borderwidth=0)
	minus.grid(row=3, column=3)

	multiply = Button(cal, text=' * ', fg='white', bg='navy blue',
					command=lambda: press("*"), height=5, width=8, borderwidth=0)
	multiply.grid(row=4, column=3)

	divide = Button(cal, text=' / ', fg='white', bg='navy blue',
					command=lambda: press("/"), height=5, width=8, borderwidth=0)
	divide.grid(row=5, column=3)

	equal = Button(cal, text=' = ', fg='white', bg='black',
				command=equalpress, height=5, width=8, borderwidth=0)
	equal.grid(row=5, column=2)

	clear = Button(cal, text='Clear', fg='white', bg='black',
				command=clear, height=5, width=8, borderwidth=0)
	clear.grid(row=5, column='1')

	Decimal= Button(cal, text='.', fg='white', bg='navy blue',
					command=lambda: press('.'), height=5, width=8, borderwidth=0)
	Decimal.grid(row=0, column=3)

	cal.mainloop()