# Password generator by GDWR
# https://github.com/GDWR

from tkinter import *
import tkinter.messagebox
import random
import string

class Password:

    def __init__(self, root):
        self.root = root
        self.root.title('Password Generator by GDWR')

        frame = Frame(self.root, bd=10)
        frame.grid()

        titleFrame = Frame(frame, bd=10, width=100)
        titleFrame.pack(side=TOP)

        gap =  Frame(frame, width=100)
        gap.pack(side=TOP)

        descFrame = Frame(frame, pady=10, width=100)
        descFrame.pack(side=TOP)

        entryFrame1 = Frame(frame, width=150, bd=10, relief=RIDGE, bg="#c0ded9")
        entryFrame1.pack(side=TOP)

        outputFrame = Frame(frame, pady=10, width=100)
        outputFrame.pack(side=TOP)

        self.lettersLower = string.ascii_lowercase
        self.lettersUpper = string.ascii_uppercase

        letters = StringVar()
        numbers = StringVar()

        self.labelDesc = Label(titleFrame, font=("Courier", 20, 'underline'), text="Password Generator", justify=CENTER, bd=7)
        self.labelDesc.grid(row=0, column=0, sticky=W)

        self.labelLetters = Label(entryFrame1, font=('Courier'), text="Amount of letters", justify=CENTER, bg="#c0ded9")
        self.labelNumbers = Label(entryFrame1, font=('Courier'), text="Amount of numbers", justify=CENTER, bg="#c0ded9")
        self.entryLetters = Entry(entryFrame1, justify=CENTER, bg="#c0ded9", textvariable=letters)
        self.entryNumbers = Entry(entryFrame1, justify=CENTER, bg="#c0ded9", textvariable=numbers)
        self.desc = Label(descFrame, font=('Courier'), text="Minimum of 6 characters")
        self.labelLetters.grid(row=0, column=0)
        self.entryLetters.grid(row=1, column=0)
        self.labelNumbers.grid(row=2, column=0)
        self.entryNumbers.grid(row=3, column=0)
        self.desc.grid(row=0, column=0, sticky=S)

        def reset():
            self.nCount = 0
            self.lCount = 0
            self.randomLetters = []
            self.randomNumbers = []
            self.tempPassword = []
            self.password = ""

        def generate():
            numLetters = (letters.get())
            numNumbers = (numbers.get())
            if (numLetters.isdigit() and numNumbers.isdigit()):
                reset()
                numL = int(numLetters)
                numN = int(numNumbers)
                if numN + numL >= 6:
                    while self.lCount < numL:
                        temp = random.choice([True, False])
                        if temp == True:
                            temp1 = random.randrange(0,26)
                            self.tempPassword.append(self.lettersLower[temp1])
                        if temp == False:
                            temp2 = random.randrange(0,26)
                            self.tempPassword.append(self.lettersUpper[temp2])
                        numL += -1

                    while self.nCount < numN:
                        self.tempPassword.append(random.randrange(0,10))
                        numN += -1

                    while len(self.tempPassword) > 0:
                        temp3 = len(self.tempPassword)
                        temp4 = random.randrange(0, temp3)
                        self.password += str(self.tempPassword[temp4])
                        self.tempPassword.pop(temp4)
                    tkinter.messagebox.showinfo("Your New Password", self.password)
                else:
                    tkinter.messagebox.showwarning("Wrong values", "Please have a minimum of 6 characters")
            else:
                tkinter.messagebox.showwarning("Wrong values", "Please only use numbers")


        self.button = Button(entryFrame1, justify=CENTER, bg="#c0ded9", font=('Courier'), text="Generate", width=14, command=generate).grid(row=4, column=0)




if __name__=='__main__':
    root = Tk()
    app = Password(root)
    root.mainloop()
