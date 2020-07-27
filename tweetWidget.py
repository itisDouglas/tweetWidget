from tkinter import *
import twitter
import config

"""

This tweet widget app is a simple gui that allows you to tweet without overhead of the website.

The first thing that needs to be done is set your access and consumer key information in the
config.py file. Afterwards, the api variable will hold all the information for you.

This application sets the gui using tkinter.

The tweet() takes an argument 'text'. This text values for this argument is supplied by the anonymous function in create_widgets(). Buttons in tkinter have a command value that can be supplied. In this app, this particular value is captured, sent to the tweet() and converted into a string. That string value is sent as a status updated (or tweet) to your twitter timeline.

"""

api = twitter.Api(consumer_key= config.CONSUMER_KEY, consumer_secret=config.CONSUMER_SECRET, access_token_key=config.ACCESS_TOKEN_KEY,access_token_secret=config.ACCESS_TOKEN_SECRET)

class Application(Frame):
    def __init__(self, master):
        #making the frame
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def get_input(self):
        input_Val = self.text.get("1.0", "end-1c")
        return str(input_Val)
    
    def create_widgets(self):
        #creating widgets
        #need a label, text box, button
        self.lbl = Label(self, text = 'Tweet!')
        self.lbl.grid_configure()
        #this is my text box
        self.text = Text(self, width = 25, height =5, wrap = WORD)
        self.text.grid_configure(column=3)
        #this is my button
        self.btn = Button(self, text='Tweet!', command = lambda: self.tweet(self.get_input()))
        self.btn.grid_configure(column=3)

    

    def tweet(self, text):
        #this method will be used to send a tweet
        api.PostUpdate(status = str(text))
        
    
    
root = Tk()
root.title("Tweet widget")
root.geometry('300x150')
app = Application(root)
root.mainloop()
