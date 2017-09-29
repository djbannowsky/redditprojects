import praw
from config import keys
from tkinter import *
from tkinter import ttk

client_id = keys['client_id']
client_secret = keys['client_secret']

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='my user agent')

list = []
for submission in reddit.subreddit('news').hot(limit=10):
    list.append(str(str(submission.ups) + ' : ' + submission.title))


class Application:
    count = 0

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        master.iconbitmap(self, default="clienticon.ico")
        master.wm_title("Reddit News")

        master.geometry("1400x400")

        style = ttk.Style()
        style.configure('TLabel', font='helvetica 16')

        self.title = ttk.Label(frame, text='Top 10 Hot Posts from /r/News\n')
        self.title.grid(row=0, sticky=W)

        self.article1 = ttk.Label(frame, text=list[0], style='TLabel')
        self.article1.grid(row=1, columnspan=4, sticky=W)
        self.article2 = ttk.Label(frame, text=list[1], style='TLabel')
        self.article2.grid(row=2, columnspan=4, sticky=W)
        self.article3 = ttk.Label(frame, text=list[2], style='TLabel')
        self.article3.grid(row=3, columnspan=4, sticky=W)
        self.article4 = ttk.Label(frame, text=list[3], style='TLabel')
        self.article4.grid(row=4, columnspan=4, sticky=W)
        self.article5 = ttk.Label(frame, text=list[4], style='TLabel')
        self.article5.grid(row=5, columnspan=4, sticky=W)
        self.article6 = ttk.Label(frame, text=list[5], style='TLabel')
        self.article6.grid(row=6, columnspan=4, sticky=W)
        self.article7 = ttk.Label(frame, text=list[6], style='TLabel')
        self.article7.grid(row=7, columnspan=4, sticky=W)
        self.article8 = ttk.Label(frame, text=list[7], style='TLabel')
        self.article8.grid(row=8, columnspan=4, sticky=W)
        self.article9 = ttk.Label(frame, text=list[8], style='TLabel')
        self.article9.grid(row=9, columnspan=4, sticky=W)
        self.article10 = ttk.Label(frame, text=list[9], style='TLabel')
        self.article10.grid(row=10, columnspan=4, sticky=W)


root = Tk()
app = Application(root)
root.mainloop()
