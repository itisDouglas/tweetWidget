#A simple widget for sending tweets to my twitter without all the overhead in the app itself
from tkinter import *
import twitter
import keys

api = twitter.Api(consumer_key= keys.CONSUMER_KEY, consumer_secret=keys.CONSUMER_SECRET, access_token_key=keys.ACCESS_TOKEN_KEY,access_token_secret=keys.ACCESS_TOKEN_SECRET)

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

    

    def tweet(self, texto):
        #this method will be used to send a tweet
        #it's activated when the button gets pressed
        #how do i grab the text from the text box?
        #establish a tweet parameter
        #inputVal = self.text.get("1.0", "end-1c")
        api.PostUpdate(status = str(texto))
        
    
    
root = Tk()
root.title("Tweet widget")
root.geometry('300x150')
app = Application(root)
root.mainloop()
