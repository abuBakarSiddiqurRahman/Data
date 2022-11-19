from tkinter import *
import formula


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first, text='First number')
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=5, side='left')
        self.entry_first.pack(padx=30, side='left')
        self.frame_first.pack(anchor='w', pady=10)

        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second, text='Second number')
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=5, side='left')
        self.entry_second.pack(padx=15, side='left')
        self.frame_second.pack(anchor='w', pady=10)

        self.frame_operation = Frame(self.window)
        self.label_operation = Label(self.frame_operation, text='Operation\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_add = Radiobutton(self.frame_operation, text='Add', variable=self.radio_1, value=1)
        self.radio_subtract = Radiobutton(self.frame_operation, text='Subtract', variable=self.radio_1, value=2)
        self.radio_multiply = Radiobutton(self.frame_operation, text='Multiply', variable=self.radio_1, value=3)
        self.radio_divide = Radiobutton(self.frame_operation, text='Divide', variable=self.radio_1, value=4)
        self.label_operation.pack(side='left', padx=5)
        self.radio_add.pack(side='left')
        self.radio_subtract.pack(side='left')
        self.radio_multiply.pack(side='left')
        self.radio_divide.pack(side='left')
        self.frame_operation.pack(anchor='w', pady=10)

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='COMPUTE', command=self.compute)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def compute(self):
        try:
            first_num = self.entry_first.get()
            second_num = self.entry_second.get()
            operation = self.radio_1.get()

            if operation == 1:
                self.label_result.config(text=f'{first_num} + {second_num} = {formula.add(first_num, second_num)}')
            elif operation == 2:
                self.label_result.config(text=f'{first_num} - {second_num} = {formula.subtract(first_num, second_num)}')
            elif operation == 3:
                self.label_result.config(text=f'{first_num} * {second_num} = {formula.multiply(first_num, second_num)}')
            elif operation == 4:
                self.label_result.config(text=f'{first_num} / {second_num} = {formula.divide(first_num, second_num)}')
            else:
                self.label_result.config(text='No operation selected')
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except ZeroDivisionError:
            self.label_result.config(text='Cannot divide by 0 (change second number value)')
        except:
            self.label_result.config(text='Error occurred! Check input values')
