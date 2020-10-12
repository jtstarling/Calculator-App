# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:37:24 2020

@author: jaqua
"""
#Need to Pre-define inverse_pressed So That Trig Functions Can operate Normally 
inverse_pressed = ''

# import everything from tkinter module 
from tkinter import *

#Importing the Math library 
import math

#Imports everything from math module 
from math import cos, acos 

# globally declare the expression variable, empty, "" = string 
expression = "" 


# Function to update expression 
# in the text entry box 
def press(num): 
	# allows for the use of the global expression variable 
	global expression 

	# adding a string to previous string 
	expression = expression + str(num) 

	# update the results on screen by using set method 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 

		global expression 

		# eval function evaluate the expression, to do basic functions, +, -, *, /,
		# also checks whether vaild  
		total = eval("__import__('math')")
		total = eval(expression)

                # update the result by using set method with answer 
		equation.set(total)

                #setting expression value to the string of total so it can be used further
		expression = str(total)
		
	# if not valid, an error is generated, then handle 
	# by the except block 
	except: 
                # Shows user there is an Error
		equation.set(" Error ")

		# then empties string
		expression = "" 



# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression
	# empties string
	expression = ""

	# Clears what is Showed to user, aka blank text box
	equation.set("")

	
        #Changes text in label to let the user know that their answer will now be in radians 
	deg_rad_label.config(text='Calculator is in Radians') 


#The following function "def sqrt()" isn't used and is not needed in this version - It was used in the old version
# Function to do the Square Root 
def sqrt(): 
	# point out the global expression variable 
	global expression 

	# math equation, using Math library,
	# must convert to interger to use in equation 
	expression = math.sqrt(int(expression))

	# update the result by using set method with answer, using interger to truncate decimals  
	equation.set(int(expression))

        # setting expression value to the string of the expression so it can be used further
	expression = str(expression) 
# The above function "def sqrt()" isn't used in the program
#


# # You can create more funtions here for more calculator functions # #
    
#Function of Sine Function
def sine(): 
    global expression, inverse_pressed 
    
    try:
        #If statement checks to see if the inverse button was pressed
        #If inverse_pressed == 'inverse_pressed' that means that the inverse button was pressed 
        
        if inverse_pressed=='inverse_pressed':
            #Inverse cosine function using math library 
            #Converts expresssion from string to float 
            
            expression = expression + "math.asin("
            equation.set(expression) 
            expression = str(expression)
            
            #Need to clear a for future usage 
            inverse_pressed = '' 
        else: 
            
            #cosine function, using math library
            #converts expression from string to float
            expression = expression + "math.sin("
    
            #update result using float expression
            equation.set(expression)
    
            #Display expression
            expression = str(expression)
    except:
        equation.set("Domain Error")
        expression = ''
 
#Function of cosine function
def cosine(): 
    global expression, inverse_pressed 
    
    try:
        #If statement checks to see if the inverse button was pressed
        #If a==a that means that the inverse button was pressed 
        
        if inverse_pressed=='inverse_pressed':
            #Inverse cosine function using math library 
            #Converts expresssion from string to float 
            
            expression = expression + "math.acos("
            equation.set(expression) 
            expression = str(expression)
            
            #Need to clear a for future usage 
            inverse_pressed = '' 
        else: 
            
            #cosine function, using math library
            #converts expression from string to float
            expression = expression + "math.cos("
    
            #update result using float expression
            equation.set(expression)
    
            #Display expression
            expression = str(expression)
    except:
        equation.set("Domain Error")
        expression = ''

#Function of tangent function 
def tangent(): 
    global expression, inverse_pressed 
    
    try:
        #If statement checks to see if the inverse button was pressed
        #If a==a that means that the inverse button was pressed 
        
        if inverse_pressed=='inverse_pressed':
            #Inverse cosine function using math library 
            #Converts expresssion from string to float 
            
            expression = expression + "math.atan("
            equation.set(expression) 
            expression = str(expression)
            
            #Need to clear inverse_pressed for future usage 
            inverse_pressed = '' 
        else: 
            
            #cosine function, using math library
            #converts expression from string to float
            expression = expression + "math.tan("
    
            #update result using float expression
            equation.set(expression)
    
            #Display expression
            expression = str(expression)
    except:
        equation.set("Domain Error")
        expression = ''
    
        
#Reciprical Function 
def reciprocal(): 
    global expression
    try:
        
        expression = 1/float(expression)
        equation.set(float(expression))
        
    except:
        equation.set("Syntax Error")
        expression =''
#Inverse function to be used on trig functions       
def inverse():
    global inverse_pressed
    inverse_pressed = 'inverse_pressed'

#Lets the calculator know that the user wants their answers to be in degrees 
def degrees_pressed():
    global degree_button_pushed, radians_button_pushed, expression
    
    #This variable cconfirms that the degree button was pushed 
    degree_button_pushed = 'degrees_pushed'
    
    #Changes text in label to let the user know that their answer will now be in degrees 
    deg_rad_label.config(text = 'Calculator is in Degrees')

    #Cleans the radians pushed button so that the radians button is no longer active
    radians_button_pushed = ''
    
    #Convers the Expression from Radians to Degrees 
    expression = math.radians(float(expression))
    
    #Update result using float expression 
    equation.set(float(expression))
    
    #Display expression 
    expression = str(expression)

def radians_pressed():
    global radians_button_pushed, degree_button_pushed, expression 

    #This variable confirms that the radians button was pushed 
    radians_button_pushed = 'radians_pushed'

    #Changes text in label to let the user know that their answer will now be in radians
    deg_rad_label.config(text='Calculator is in Radians')

    #Cleans the degrees pushed button so that the degrees button is no longer active
    degree_button_pushed = ''
    
    #Convers the Expression from Degreees to Radians 
    expression = math.degrees(float(expression))
    
    #Update result using float expression 
    equation.set(float(expression))
    
    #Display expression 
    expression = str(expression)
    
#Function of logarithmic function with a base of 10
    
def log(): 
    global expression 
        
    try: 
        expression = expression + "math.log10("
        equation.set(expression)
        expression = str(expression)
    except:
        equation.set("Syntax Error")
        expression = ''

#Function of the 2*e^x
def exponent(): 
    global expression 
        
    try: 
        expression = expression + "2*math.exp("
        equation.set(expression)
        expression = str(expression)
    except:
        equation.set("Syntax Error")
        expression = ''

def calculate():
        global expression,x1,x2,x3,x4
        try:
                expression = 2*x1 + 3*x2+ x3**2 + x4
                equation.set(expression)
        except:
                equation.set('Cant Calculate x1,x2,x3,&x4') 

# Program code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="light blue") 

	# set the title of GUI window 
	gui.title("Calculator") 

	# set the size of GUI window 
	gui.geometry("365x360") 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text "entry" box for showing the expression, aka results
	expression_field = Entry(gui, textvariable=equation)
    

	# grid method is used for placing separate items in the GUI Window into a certain number of columns & rows
	
	# sets the size of the text box, span across columns & span length 
	expression_field.grid(columnspan=5, ipadx=120)

        # sets the initial text of the text box 
	equation.set('Enter Your Expression')
	 

	# create a Button, with text in it, font color, background color,
	# Uses Lambda commands for each number or expression OR commands for a defined function above
	# Height & Length for the size of the button
	# Then places the Button on the grid in a certain row & column: Rows start at 2, and Columns at 0
	button1 = Button(gui, text=' 1 ', fg='black', bg='pink', command=lambda: press(1), height=3, width=9) 
	button1.grid(row=6, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='pink', command=lambda: press(2), height=3, width=9) 
	button2.grid(row=6, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='pink', command=lambda: press(3), height=3, width=9) 
	button3.grid(row=6, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='pink', command=lambda: press(4), height=3, width=9) 
	button4.grid(row=5, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='pink', command=lambda: press(5), height=3, width=9) 
	button5.grid(row=5, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='pink', command=lambda: press(6), height=3, width=9) 
	button6.grid(row=5, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='pink', command=lambda: press(7), height=3, width=9) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='pink', command=lambda: press(8), height=3, width=9) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='pink', command=lambda: press(9), height=3, width=9) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='pink', command=lambda: press(0), height=3, width=9) 
	button0.grid(row=7, column=1) 

	plus = Button(gui, text=' + ', fg='black', bg='yellow', command=lambda: press("+"), height=3, width=9) 
	plus.grid(row=4, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='yellow', command=lambda: press("-"), height=3, width=9) 
	minus.grid(row=5, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='yellow', command=lambda: press("*"), height=3, width=9) 
	multiply.grid(row=7, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='yellow', command=lambda: press("/"), height=3, width=9) 
	divide.grid(row=6, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='light green', command=equalpress, height=3, width=9) 
	equal.grid(row=7, column=2) 

	clear = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=3, width=9) 
	clear.grid(row=5, column=4)

	sqrt = Button(gui, text='√x', fg='black', bg='white', command= lambda: press("math.sqrt("), height=3, width=9) 
	sqrt.grid(row=2, column=3)

	dec = Button(gui, text=' . ', fg='black', bg='orange', command=lambda: press("."), height=3, width=9) 
	dec.grid(row=7, column=0)

# # You can create more buttons here for more calculator functions # #

trig_sine = Button(gui, text='sin', fg='black', bg='#9494b8', command=sine, height=3, width=9)
trig_sine.grid(row=3, column=0)

trig_cosine = Button(gui, text='cos', fg='black', bg='#9494b8', command=cosine, height=3, width=9)
trig_cosine.grid(row=3, column=1)

trig_tangent = Button(gui, text='tan', fg='black', bg='#9494b8', command=tangent, height=3, width=9)
trig_tangent.grid(row=3, column=2)

left_parentheses = Button(gui, text='(', fg='black', bg='#9494b8', command=lambda:press("("), height=3, width=9)
left_parentheses.grid(row=2, column=4)

right_parentheses = Button(gui, text=')', fg='black', bg='#9494b8', command=lambda:press(")"), height=3, width=9)
right_parentheses.grid(row=3, column=4)

convert_radian = Button(gui, text='rad to deg', fg='black', bg='#9494b8',command = radians_pressed, height=3, width=9)
convert_radian.grid(row=2, column=0)

convert_degree = Button(gui, text='deg to rad', fg='black', bg='#9494b8',command = degrees_pressed, height=3, width=9)
convert_degree.grid(row=2, column=1)

inverse_button = Button(gui, text='INV', fg='black', bg='#9494b8',command = inverse, height=3, width=9)
inverse_button.grid(row=2, column=2)

recip = Button(gui, text='1/x', fg='black', bg='#9494b8',command = reciprocal, height=3, width=9)
recip.grid(row=3, column=3)

log_button = Button(gui, text = 'log', fg='black', command = log , bg = '#9494b8', height=3, width=9)
log_button.grid(row=4, column=4)

exp_button = Button(gui, text='2*e^x', fg='black', command= exponent, bg='#A689D3', height=3, width=9)
exp_button.grid(row=6,column=4)


# Starts the GUI 
gui.mainloop() 
