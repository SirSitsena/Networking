import tkinter as tk
import tkinter.scrolledtext as tksctxt

#----------------------------------------------------FIREBASE
import firebase_admin
from firebase_admin import db

cred = firebase_admin.credentials.Certificate("C:\dev\PythonProjects\Lab12\privateKey.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://ebatoriya-default-rtdb.firebaseio.com/'}) #  https://ebatoriya-default-rtdb.firebaseio.com/
ref = firebase_admin.db.reference('/')
#----------------------------------------------------FIREBASE


DEFAULT_HOST = 'localhost:60003'


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # -------------------------------------------------------------------
        # row 1: connection stuff (and a clear-messages button)
        # -------------------------------------------------------------------
        self.groupCon = tk.LabelFrame(bd=0)
        self.groupCon.pack(side="top")
        #
        self.nameLbl = tk.Label(self.groupCon, text='Name', padx=10)
        self.nameLbl.pack(side="left")
        #
        self.name = tk.Entry(self.groupCon, width=20)
        self.name.insert(tk.END, "")
        # if the focus is on this text field and you hit 'Enter',
        # it should (try to) connect
        # self.ipPort.bind('<Return>', connectHandler)
        self.name.pack(side="left")
        #
        padder = tk.Label(self.groupCon, padx=5)
        padder.pack(side="left")

        # -------------------------------------------------------------------
        # row 2: the message field (chat messages + status messages)
        # -------------------------------------------------------------------
        self.msgText = tksctxt.ScrolledText(height=15, width=42,
                                            state=tk.DISABLED)
        self.msgText.pack(side="top")

        # -------------------------------------------------------------------
        # row 3: sending messages
        # -------------------------------------------------------------------
        self.groupSend = tk.LabelFrame(bd=0)
        self.groupSend.pack(side="top")
        #
        self.textInLbl = tk.Label(self.groupSend, text='message', padx=10)
        self.textInLbl.pack(side="left")
        #
        self.textIn = tk.Entry(self.groupSend, width=38)
        # if the focus is on this text field and you hit 'Enter',
        # it should (try to) send
        self.textIn.bind('<Return>', sendMessage)
        self.textIn.pack(side="left")
        #
        padder = tk.Label(self.groupSend, padx=5)
        padder.pack(side="left")
        #
        self.sendButton = tk.Button(self.groupSend, text='send',
                                    command=sendButtonClick)
        self.sendButton.pack(side="left")


def clearButtonClick():
    g_app.msgText.configure(state=tk.NORMAL)
    g_app.msgText.delete(1.0, tk.END)
    g_app.msgText.see(tk.END)
    g_app.msgText.configure(state=tk.DISABLED)


def sendButtonClick():
    # forward to the sendMessage method
    sendMessage(g_app)


def handleMessage(message):
    printToMessages(message["name"]+": "+message["text"])


def streamHandler(incomingData):
    if incomingData.event_type == 'put':
        if incomingData.path == '/':
            # This is the very first reading just after subscription:
            # we get all messages or None (if no messages exists).
            if incomingData.data != None:
                for key in incomingData.data:
                    message = incomingData.data[key]
                    handleMessage(message)
        else:
            # Not the first reading.
            # Someone wrote a new message that we just got.
            message = incomingData.data
            handleMessage(message)


# a utility method to print to the message field
def printToMessages(message):
    print(message)
    g_app.msgText.configure(state=tk.NORMAL)
    g_app.msgText.insert(tk.END, message + '\n')
    # scroll to the end, so the new message is visible at the bottom
    g_app.msgText.see(tk.END)
    g_app.msgText.configure(state=tk.DISABLED)


# if attempt to close the window, it is handled here
def on_closing():
    myQuit()


# when quitting, do it the nice way
def myQuit():
    g_root.destroy()
    messages_stream.close()


# attempt to send the message (in the text field g_app.textIn) to the server
def sendMessage(master):
    newMessage = {'name': master.name.get(), 'text': master.textIn.get()}
    ref.child('messages').push(newMessage)


# launch the gui
g_root = tk.Tk()
g_app = Application(master=g_root)


# # schedule the next call to pollMessages

messages_stream = ref.child('messages').listen(streamHandler)


# if attempt to close the window, handle it in the on-closing method
g_root.protocol("WM_DELETE_WINDOW", on_closing)

# start the main loop
g_app.mainloop()
