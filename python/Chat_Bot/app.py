from tkinter import Tk, Label, Text, Scrollbar, Entry, Button, PhotoImage, DISABLED, END, NORMAL
from infobot import get_response

BG_YELLOW = "#FFFF00"
BG_BLUE = "#00F5FF"
BG_COLOR = '#1E1E1E'
TEXT_COLOR = '#8B1A1A'
L_GREY = '#F0FFFF'

FONT = 'LucidaHandwritin 14'
FONT_BOLD = 'LucidaHandwritin 16 bold'

class Chat_App:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self._insert_message2()
        self.window.mainloop()
        
          
    def _setup_main_window(self):
        self.window.title("Info Bot")
        #self.window.iconbitmap('/Users/hiddenacez/code/python/Chat_Bot/Pictures/InfoBot.ico')
        self.window.resizable(width=False, height=False)
        self.window.configure(width=580,height=700, bg=BG_COLOR)


        #Image
        #img = PhotoImage(file = 'InfoBot.png')
        
        # Head Label
        head_label = Label(self.window, bg=BG_COLOR, fg="#FF0000", text='Welcome', font=FONT_BOLD,pady=10)
        head_label.place(relwidth=1)

        # Tiny divider
        line = Label(self.window, width=470, bg="#CDC8B1")
        line.place(relwidth=1,rely=0.07,relheight=0.012)

        # Text Widget
        self.text_widget = Text(self.window,width=20,height=2, bg='#FFF8DC', fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.80, relwidth=1, rely=0.082)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scroll Bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Bottom Label
        bottom_label = Label(self.window, bg=BG_COLOR, height=40)
        bottom_label.place(relwidth=1,rely=0.9)


        # Message Entry Box
        self.msg_entry = Entry(bottom_label, bg='#CCCCCC', fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74,relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

       

        # Send Botton
        send_button = Button(bottom_label, text='Send', font=FONT_BOLD, width=20, bg=BG_BLUE, fg='#DC143C', command=lambda:self._on_enter_pressed(None))
        send_button.place(relx=0.77,rely=0.008, relheight=0.06, relwidth=0.22)


    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg,'You')
    
    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

         #.after(1000, lambda: e.config(bg='white'))
         #self.text_widget.after(5000)
        msg2 = f"Info Bot: {get_response(msg)}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        self.text_widget.see(END)
    
    def _insert_message2(self, sender='InfoBot'):
        Intro = ("""\n_____________________$$$\n____________________$___$\n_____________________$$$\n_____________________$_$\n_____________________$_$\n___________________$$$_$$$\n_________________$$__$$$__$$$\n_______________$$__$$$$$$$___$\n______________$_______________$\n_____________$_________________$\n_____________$_________________$\n_____________$_____$$$$$$$$$$$$$$$\n_____________$____$_______________$\n_____________$____$___$$$$$$$$$$$$$\n_____________$___$___$___________$$$\n_____________$___$___$_$$$___$$$__$$\n_____________$___$___$_$$$___$$$__$$\n_____________$___$___$___________$$$\n_____________$____$___$$$$$$$$$$$$$\n_____________$_____$$$$$$$$$$$$$$\n_____________$_________________$\n_____________$____$$$$$$$$$$$$$$\n_____________$___$__$__$__$__$\n_____________$__$$$$$$$$$$$$$$\n_____________$__$___$__$__$__$\n_____________$___$$$$$$$$$$$$$$$\n____________$$$_________________$$$\n__________$$___$$$_________$$$$$___$$\n________$$________$$$$$$$$$__________$$$\n_______$__$$_____________________$$$$___$$\n____$$$$$___$$$$$$$$______$$$$$$$_______$_$\n__$______$$_________$$$$$$______________$_$$\n_$____$____$____________________________$_$_$\n_$_____$___$______________$$$$$$$$$$$___$_$_$$\n_$$$____$___$__$$$$$$$$$$$$__________$___$_$_$$\n$___$$$$____$__$_____________________$___$_$$_$\n$$$____$___$$__$_____________________$$__$_$__$\n$___$__$__$$___$______________________$__$$$__$\n$_____$$_$$____$_______________$$$____$__$_$__$\n
Hello my name is InfoBot, I was created to provide info to you:\nHere is a list of things I can do:\n- I can do any mathematical operation (ex. 23*23/2+2)
- Look up the weather for your area\n- Can give some random advice\n(I am currently still learning and constantly being updated so be patient with \nwhat I don’t know)\nSay Hello...""")

        msg1 = f"{sender}: {Intro}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

         #.after(1000, lambda: e.config(bg='white'))
         #self.text_widget.after(5000)
        
        self.text_widget.see(END)
    



# Start App
if __name__ == '__main__':
    app = Chat_App()
    app.run()
    