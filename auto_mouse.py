import tkinter as tk
import pyautogui

class Event:
    def __init__(self):
        self.app = tk.Tk()

        self.period = 0
        self.idx = 0
        self.numOfPoints = 1
        self.points = []

        self.position_label = tk.Label(self.app, text='Position: ')
        self.position_label.grid(row=0, column=0)

        self.position_value_label = tk.Label(self.app, text='X: 0, Y: 0')
        self.position_value_label.grid(row=1, column=0)

        self.position_label = tk.Label(self.app, text='Press g to save cursor position')
        self.position_label.grid(row=2, column=0)

        self.position_label = tk.Label(self.app, text=f'Number of click points: {self.numOfPoints}')
        self.position_label.grid(row=3, column=0)
    
    def run(self):
        self.app.bind("<Key>",self.keyEvent)
        self.app.title('macro v0.3')
        self.app.geometry('200x240')
        self.update_position_value_label()

        f_input = tk.Entry(self.app, width=15)
        f_input.insert(0, 'Enter a click interval')
        f_input.config(fg='grey', justify='center')

        def on_input_click(event):
            if f_input.get() == 'Enter a click interval':
                f_input.delete(0, tk.END)

        def setNumOfPoints(op):
            self.numOfPoints += 1 if op == '+' else -1
            self.position_label.config(text=f'Number of click points: {self.numOfPoints}')
        
        btn_increase = tk.Button(self.app, text='+', 
                                 command=lambda:setNumOfPoints('+'))
        btn_increase.grid(row=4, column=0)

        btn_decrease = tk.Button(self.app, text='-', 
                                 command=lambda:setNumOfPoints('-'))
        btn_decrease.grid(row=5, column=0)

        btn_clear = tk.Button(self.app, text='clear',
                                 command=lambda:self.points.clear())
        btn_clear.grid(row=6, column=0)
        
        f_input.bind('<FocusIn>', on_input_click)
        f_input.grid(row=7, column=0)

        btn_click = tk.Button(self.app, text='Click!', 
                                 command=lambda: self.setValues(int(f_input.get())))
        btn_click.grid(row=8, column=0)
        self.app.mainloop()

    def setValues(self, f):
        self.period = f# * 1000
        self.click_at_position()

    # clicking on specific coordinates at regular intervals
    def click_at_position(self):
        # pyautogui.click(self.X, self.Y)
        # self.app.after(self.period, self.click_at_position)
        pyautogui.click(self.points[self.idx])
        if self.idx + 1 == self.numOfPoints:
            self.idx = 0
        else:
            self.idx += 1
        self.app.after(self.period * 1000, self.click_at_position)
    
    # Real-time mouse cursor coordinate output
    def update_position_value_label(self):
        self.curX, self.curY = pyautogui.position()
        context = f'X: {self.curX}, Y: {self.curY}'
        self.position_value_label.config(text=context)
        self.app.after(100, self.update_position_value_label)

    # Save mouse cursor coordinates for the moment when the key is entered
    def keyEvent(self, event):
        if event.char in ['q', 'Q', 'ㅂ']:
            self.app.destroy()

        if event.char not in ['g', 'G', 'ㅎ']:
            return

        if self.numOfPoints - len(self.points) > 0:
            self.points.append((event.x, event.y))        
            print(self.points)
e = Event()
e.run()
