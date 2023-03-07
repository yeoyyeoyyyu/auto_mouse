import tkinter as tk
import pyautogui

class Event:
    def __init__(self):
        self.app = tk.Tk()

        self.X = 0
        self.Y = 0
        self.period = 0

        self.position_label = tk.Label(self.app, text='Position: ')
        self.position_label.grid(row=0, column=0)

        self.position_value_label = tk.Label(self.app, text='X: 0, Y: 0')
        self.position_value_label.grid(row=1, column=0)

        self.position_label = tk.Label(self.app, text='Press g to save cursor position')
        self.position_label.grid(row=2, column=0)
    
    def run(self):
        self.app.bind("<Key>",self.keyEvent)
        self.app.title('macro v0.2')
        self.app.geometry('250x180')
        self.update_position_value_label()

        f_input = tk.Entry(self.app, width=15)
        f_input.insert(0, 'Enter a click interval')
        f_input.config(fg='grey', justify='center')

        def on_input_click(event):
            if f_input.get() == 'Enter a click interval':
                f_input.delete(0, tk.END)

        f_input.bind('<FocusIn>', on_input_click)
        f_input.grid(row=4, column=0)

        click_button = tk.Button(self.app, text='Click!', 
                                 command=lambda: self.setValues(int(f_input.get())))
        click_button.grid(row=5, column=0)
        self.app.mainloop()

    def setValues(self, f):
        self.period = f * 1000
        self.click_at_position()

    # clicking on specific coordinates at regular intervals
    def click_at_position(self):
        pyautogui.click(self.X, self.Y)
        self.app.after(self.period, self.click_at_position)
    
    # Real-time mouse cursor coordinate output
    def update_position_value_label(self):
        self.curX, self.curY = pyautogui.position()
        context = f'X: {self.curX}, Y: {self.curY}'
        self.position_value_label.config(text=context)
        self.app.after(100, self.update_position_value_label)

    # Save mouse cursor coordinates for the moment when the key is entered
    def keyEvent(self, event):
        if event.char in ['g', 'G', 'ㅎ']:
            self.X, self.Y = event.x, event.y
            print(f'set coordinate: ({self.X}, {self.Y})')
e = Event()
e.run()
