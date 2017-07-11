import tkinter as tk
from tkinter import font
from tkinter import messagebox
import GuessNumber


class Application:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x200')
        self.root.resizable(width=False, height=False)
        self.root.title('Number Guessing')
        self.guessNumber = GuessNumber.GuessNumber()

    def start(self):
        self.mymenu()
        titleFont = font.Font(family='Helvetica', size=24)
        infoFont = font.Font(family='Helvetica', size=18)
        self.mlabel = tk.Label(fg='#f000cc',
                  bg='#88c0c0',
                  width=12,
                  font=titleFont)
        self.titleText()
        self.mlabel.pack(pady=10)

        self.mentry = tk.Entry(master=self.root,
                               font=titleFont,
                               justify=tk.CENTER,
                               width=6)
        self.mentry.bind('<Return>', self.guess)
        self.mentry.pack()
        self.mentry.focus_set()

        self.infolabel = tk.Label(font=infoFont)
        self.infolabel.pack()

        self.root.mainloop()

    def mymenu(self):
        menubar = tk.Menu(self.root)
        fileMenu = tk.Menu(menubar, tearoff=0)
        fileMenu.add_command(label='New Game', command=self.wannaRestart)
        fileMenu.add_command(label='About', command=self.about)
        fileMenu.add_command(label='Close', command=self.quit)
        menubar.add_cascade(label='Game', menu=fileMenu)
        self.root.config(menu=menubar)

    def titleText(self):
        report = self.guessNumber.report()
        text = '(%d - %d)' % (report['min'], report['max'])
        if report['min'] == report['max']:
            text = '(%d)' % report['min']
        self.mlabel['text'] = 'ทายตัวเลข %s' % text

    def setInfoText(self, text):
        self.infolabel['text'] = text

    def quit(self):
        isquit = messagebox.askyesno(title='ปิดโปรแกรม',
                               message='ต้องการปิดโปรแกรมหรือไม่')
        if isquit: self.root.destroy()

    def guess(self, event=None):
        report = self.guessNumber.report()
        if report['finish']: return
        try:
            number = int(self.mentry.get())
            if number < report['min'] or number > report['max']:
                raise ValueError
        except ValueError:
            message='ทายตัวเลขเป็นจำนวนเต็ม\nตั้งแต่ %d ถึง %d นะ' % (report['min'], report['max'])
            self.setInfoText(message)
        else:
            result = self.guessNumber.guess(number)
            self.updateInfo()
            if not result['finish']:
                 self.titleText()
            else:
                isrestart = messagebox.askyesno(title='Start New Game',
                                    message='ต้องการเริ่มใหม่หรือไม่')
                if isrestart:
                    self.restart()
        self.mentry.delete(0, tk.END)

    def wannaRestart(self):
        isreset = messagebox.askyesno(title='เริ่มเกมใหม่',
                               message='ต้องการเริ่มเกมใหม่หรือไม่')
        if isreset: self.restart()

    def restart(self):
        self.guessNumber.reset()
        self.titleText()
        self.setInfoText("")
        self.mentry.delete(0, tk.END)

    def updateInfo(self):
        report = self.guessNumber.report()
        text = ''
        if not report['finish']:
            text = 'คุณทายตัวเลขแล้ว %d ครั้ง\n' % report['count']
            text += 'ยังไม่ถูกต้อง'
        else:
            text = 'คุณทายตัวเลขถูกต้องในครั้งที่ %d\n' % report['count']
        self.setInfoText(text)

    def about(self):
        text = 'Version 1.0\n'
        text += 'โดย Saac Sornchai\n'
        text += '11 กรกฎาคม 2560'
        self.setInfoText(text)
