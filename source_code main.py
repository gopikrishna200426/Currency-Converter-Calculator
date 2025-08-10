from tkinter import *
from tkinter import ttk

def currency():
    window = Tk()
    window.title("Currency Converter")
    window.geometry("600x400")

    values = {
    "Euro": 100.0,
    "United States Dollar": 87.66,
    "UAE Dirham": ...,
    "Malaysian Ringgit": ...,
    "Japanese Yen": ...
    }


    def calc():
        p = rupees.get()
        ans = v.get()
        d = values.get(ans, None)
        conv = float(d) * float(p)
        res.delete(1.0, END)
        res.insert(INSERT, conv)

    res = Text(window, height=2, width=20, font=("arial bold", 10), bd=5)
    res.grid(column=1, row=2)

    ind = Label(window, text="Value in selected currency:", fg='blue', font=("arial bold", 10))
    ind.grid(column=0, row=1)

    rate = Label(window, text="Converted rate:", fg='blue', font=('arial bold', 10))
    rate.grid(column=0, row=2)

    rupees = Entry(window, font=("arial bold", 10))
    rupees.grid(column=1, row=1)

    ch = Label(window, text="Choice:", fg='green', font=("arial bold", 10))
    ch.grid(column=0, row=0)

    v = StringVar(window)
    v.set(None)
    option = OptionMenu(window, v, *values)
    option.grid(column=1, row=0)

    b = Button(window, text="Convert", font=("arial", 20), fg='red', command=calc)
    b.grid(column=3, row=0)

    window.mainloop()


def calc():
    class Calculator:
        def __init__(self, cal):
            cal.title("GUI Calculator")
            font, calbtn, btnArray, operator = ('arial', 20, "bold"), "789+456-123*0C=/", [], ""
            text_input = StringVar()

            def BtnClick(number):
                nonlocal operator
                operator = operator + str(number)
                text_input.set(operator)

            def Equal():
                nonlocal operator
                try:
                    calculated = eval(operator)
                    text_input.set(calculated)
                    operator = ""
                except:
                    text_input.set("Error")
                    operator = ""

            def ClearEntry():
                nonlocal operator
                text_input.set("")
                operator = ""

            Entry(cal, textvariable=text_input, font=font, bg="powder blue", bd=30, justify="right").grid(columnspan=4)
            index = 0
            for row in range(4):
                for column in range(4):
                    btnArray.append(Button(cal, text=calbtn[index], bg="powder blue", padx=16, pady=16, bd=8, font=font))
                    btnArray[index].grid(row=row + 1, column=column)
                    btnArray[index]['command'] = Equal if calbtn[index] == "=" else ClearEntry if calbtn[index] == "C" else lambda x=calbtn[index]: BtnClick(x)
                    index += 1

            cal.mainloop()

    cal = Tk()
    Calculator(cal)


def menu():
    print('1. Use Currency Converter')
    print('2. Use Calculator')
    ch = int(input('Enter your choice:'))
    if ch == 1:
        currency()
    elif ch == 2:
        calc()
    c = input('Do you want to try again? (y/n):')
    if c.lower() == 'y':
        menu()

menu()
