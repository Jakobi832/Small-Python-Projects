from tkinter import *

#back end function to calculate a percentage

def calc_percentage(top, bot):
    percent = (top * 100) // bot
    return str(percent) + '%'

#the bit in themiddle between front and back end
def calc_and_display():
    num = numerator.get()
    den = denominator.get()
    answer = calc_percentage(int(num), int(den))
    result['text'] = answer
    



#set up the window
calculator = Tk()
calculator.title("percentage calculator")

#define a font for the various widgets
calc_font = ("Arial", 60)

#create the front end user interface

#label for results
result = Label(calculator, text = 'Hello', font = ("Arial", 20))
result.pack()

#text entry boxes for user to enter numbers
numerator = Entry(calculator, font = calc_font, width = 5)
numerator.pack()

denominator = Entry(calculator, font = calc_font, width = 5)
denominator.pack()

#button for starting the calculation
start_button = Button(calculator, font = calc_font, text = "Start", command =
                      calc_and_display)
start_button.pack()

#wait for user inputs (events)
calculator.mainloop()
