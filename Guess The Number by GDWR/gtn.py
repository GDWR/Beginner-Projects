# Guess the number by GDWR
# https://github.com/GDWR


from tkinter import *
import random

class gtn:

    def __init__(self, root):
        self.root = root
        self.root.title('Guess the number by GDWR')
        self.root.geometry("350x325")
        self.root.minsize(350, 325)
        self.root.maxsize(350, 325)

        frame = Frame(self.root, bd=10)
        frame.grid()

        titleFrame = Frame(frame, bd=10, width=100, relief=RIDGE)
        titleFrame.pack(side=TOP)

        self.title = Label(titleFrame, font=("Courier", 24, 'bold'), text="Guess the Number", justify=CENTER, bg="#c0ded9" )
        self.title.grid(padx=2)

        descFrame = Frame(frame, bd=10, width=100, relief=RIDGE)
        descFrame.pack(side=TOP)

        entryFrame = Frame(frame, bd=10, width=100, relief=RIDGE)
        entryFrame.pack(side=TOP)

        stateFrame = Frame(frame, bd=10, width=100, relief=RIDGE)
        stateFrame.pack(side=TOP)

        num = StringVar()
        self.guessed= True


        self.labelDesc = Label(descFrame, font=("Courier", 10), text="Guess the number between 1-20. \n Then press Guess! \n After you guess the correct number, \n It will randomise a new one!", justify=CENTER, bd=7)
        self.labelDesc.grid(row=0, column=0, sticky=W)

        self.entryNum = Entry(entryFrame, font=("Courier", 12), bd=7, textvariable=num, width=16)
        self.entryNum.grid(row=0, column=1)

        def game():
            if self.guessed == True:
                self.randomNum = random.randint(0, 20)
                number = (num.get())
            else:

                number = (num.get())

            if (number.isdigit()):
                guessNum = int(number)
                if guessNum == self.randomNum:
                    win(self.randomNum)
                elif guessNum < self.randomNum:
                    tooLow(self.randomNum)
                elif guessNum > self.randomNum:
                    tooHigh(self.randomNum)
            else:
                print('Numbers only')

        def win(x):
            self.guessed = True
            self.labelState = Label(stateFrame, font=('Courier', 24, 'bold'), fg="darkgreen", justify=CENTER, bd=8, text="You Win")
            self.labelState.grid(row=0, column=0)
            print('Win')
            print(x)

        def tooLow(x):
            self.guessed = False
            self.labelState = Label(stateFrame, font=('Courier', 24, 'bold'), fg="darkred", justify=CENTER, bd=8, text="Too Low")
            self.labelState.grid(row=0, column=0)
            print('Too Low')
            print(x)

        def tooHigh(x):
            self.guessed = False
            self.labelState = Label(stateFrame, font=('Courier', 24, 'bold'), fg="darkred", justify=CENTER, bd=7, text="Too High")
            self.labelState.grid(row=0, column=0)
            print('Too High')
            print(x)

        self.button=Button(entryFrame, font=('Courier', 12), width=7, text="Guess",bg="#c0ded9", command=game).grid(row=0, column=2)





if __name__=='__main__':
    root = Tk()
    app = gtn(root)
    root.mainloop()
