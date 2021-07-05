'H2Hacks Submission (Game)'
import tkinter as tk
import random
import json
import sys

class Application(tk.Frame):
    'Main Application Class'
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.welcome()
        self.month_counter = 1
        self.counter = 0
        self.quizoptions = {
            'How many watts is 18 kWh': [('18000', 1),
                                         ('1800', 2),
                                         ('1.80', 3),
                                         ('180000', 4)],

            'what is the most efficient fuel source': [('Hydroeletric', 1),
                                         ('Geothermal', 2),
                                         ('Wind', 3),
                                         ('Fossil Fuels', 4)]
        }
        self.balance = 1000000
        self.renewable = 0
    def welcome(self):
        'Welcome user'
        self.welcome_text = tk.Label(self, text='Welcome, player! Please input your name here: ')
        self.welcome_text.pack(side='top')
        self.welcome_entry = tk.Entry(self)
        self.welcome_entry.pack(side='top')

        self.welcome_submit = tk.Button(self, text='SUBMIT', fg='green', command=self.intro)
        self.welcome_submit.pack(side='top')
    def intro(self):
        'Introduce character'
        self.welcome_text.pack_forget()
        self.welcome_entry.pack_forget()
        self.welcome_submit.pack_forget()

        introtext = f'''Hello, {self.welcome_entry.get()}! You are now the CEO of virtual
         H2Hacks. You only have {random.randrange(1, 10)} years left before climate change 
        destroys the Earth. You must make the right choices for your company before your 
        company becomes bankrupt and before the Earth gets destroyed.'''
        self.intro_text = tk.Label(self, text=introtext)
        self.intro_text.pack(side='top')
        self.done = tk.Button(self, text='DONE', fg='green', command=self.choose)
        self.done.pack(side='top')
    def choose(self):
        'Choose from a list of options'
        self.intro_text.pack_forget()
        self.done.pack_forget()

        options = ['Do Nothing',
                   'Convert to Renewable Energy',
                   'Release New Product',
                   'Dissolve the Company']

        self.choice = tk.StringVar(self)
        self.choice.set(options[0])
        choices = tk.OptionMenu(self, self.choice, *options)
        choices.pack()

        self.choices_submit = tk.Button(self, text='SUBMIT', fg='green', command=self.main)
        self.choices_submit.pack()
    def main(self):
        'The main part of the game.'
        if self.choice.get() == 'Do Nothing':
            self.balance -= (100-self.renewable)*500
            if self.check(worker_strike=True):
                ws_label = tk.Label(self, text='There was a worker strike. You lost $75,000.')
                ws_label.pack()
                self.balance -= 75000
        elif self.choice.get() == 'Convert to Renewable Energy':
            self.choices_submit.pack_forget()
            percentages = [('0', 1),
                           ('10', 2),
                           ('20', 3),
                           ('30', 4),
                           ('40', 5),
                           ('50', 6),
                           ('60', 7),
                           ('70', 8),
                           ('80', 9),
                           ('90', 10),
                           ('100', 11)]
            var = tk.StringVar()
            var.set('L')
            for text, option in percentages:
                self.percentage_options = tk.Radiobutton(self,
                                                         text=text,
                                                         variable=var,
                                                         value=option,
                                                         command=self.check_percent)
                self.percentage_options.pack(side='top')
  
            self.percent_submit = tk.Button(self, text='SUBMIT', fg='green', command=self.check_percent)
            self.percent_submit.pack()
        elif self.choice.get() == 'Release New Product':
            self.product_entry = tk.Entry(self)
            self.product_entry.pack(side='top')
            if random.choice(['positive', 'negative']) == 'negative':
                boycott_label = tk.Label(self, text='''Your customers did not like the product and
                boycotted your company. You lost $50,000.''')
                boycott_label.pack()
                self.balance -= 50000
            else:
                boycott_label = tk.Label(self, text='''Your customers did like the product and
                supported your company. You gained $50,000.''')
                boycott_label.pack()
                self.balance += 50000
            
        elif self.choice.get() == 'Dissolve the Company':
            self.game_over()

        self.month_counter += 3
        if self.month_counter == 1:
            month = 'January'
        elif self.month_counter == 4:
            month = 'April'
        elif self.month_counter == 7:
            month = 'July'
        else:
            month = 'October'

        if self.month_counter > 12:
            self.month_counter -= 12
            self.quiz()

        if self.counter == 0:
            self.month_text = tk.Label(self, text='')
            self.month_text.pack(side='left')

            self.bal_text = tk.Label(self, text='')
            self.bal_text.pack(side='right')

            self.counter += 1

            self.month_text.pack_forget()
            self.month_text = tk.Label(self, text=month)
            self.month_text.pack(side='left')

            self.bal_text.pack_forget()
            self.bal_text = tk.Label(self, text=self.balance)
            self.bal_text.pack(side='right')
        else:
            self.month_text.pack_forget()
            self.month_text = tk.Label(self, text=month)
            self.month_text.pack(side='left')

            self.bal_text.pack_forget()
            self.bal_text = tk.Label(self, text=self.balance)
            self.bal_text.pack(side='right')
    def check(self, worker_strike=None):
        'Check for variables such as balance, worker strikes, etc.'
        if worker_strike is None:
            if self.balance < 0:
                self.game_over()
        elif worker_strike:
            if random.randrange(1, 10) == 1 and self.renewable > 50:
                return True
            elif random.randrange(1, 20) in range(1, 3):
                return True
    def check_percent(self, value):
        'Actions taken for percent change for renewable resources'
        self.renewable += value
    def quiz(self):
        'Quiz every game year'
        var = tk.StringVar()
        var.set('L')

        for text, option in self.quizoptions['question']:
            self.quiz_options = tk.Radiobutton(self, text=text, variable=var, value=option)
            self.quiz_options.config(indicatoron=0)
            self.quiz_options.pack(side='top')
    def logs(self):
        'Keeps track of everything that happened in the game.'
    def game_over(self):
        'What to do when the game is over.'
        sys.exit()

ROOT = tk.Tk()
ROOT.geometry('500x500')
ROOT.title('You\'re The Boss! Environmental Edition')
APP = Application(master=ROOT)
APP.mainloop()
