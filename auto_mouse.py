import tkinter as tk
import pyautogui

class Event:
    def __init__(self):
        self.app = tk.Tk()

        self.X = 0
        self.Y = 0
        self.freq = 0

        self.position_label = tk.Label(self.app, text="Position: ")
        self.position_label.grid(row=0, column=0)

        self.position_value_label = tk.Label(self.app, text="X: 0, Y: 0")
        self.position_value_label.grid(row=1, column=0)

    def run(self):
        self.app.bind("<Button-1>", self.callback_mouse)
        self.app.title('macro v0.1')
        self.app.geometry("250x180")
        self.update_position_value_label()

        x_label = tk.Label(self.app, text='x좌표:')
        x_label.grid(row=2, column=0)
        x_input = tk.Entry(self.app, width=5)
        x_input.grid(row=2, column=1)
        
        y_label = tk.Label(self.app, text='y좌표:')
        y_label.grid(row=3, column=0)
        y_input = tk.Entry(self.app, width=5)
        y_input.grid(row=3, column=1)

        f_label = tk.Label(self.app, text='주기:')
        f_label.grid(row=4, column=0)
        f_input = tk.Entry(self.app, width=5)
        f_input.grid(row=4, column=1)

        click_button = tk.Button(self.app, text="Click", 
                                 command=lambda: self.setValues(int(x_input.get()), int(y_input.get()), int(f_input.get())))
        click_button.grid(row=5, column=0)
        self.app.mainloop()

    def setValues(self, x, y ,f):
        self.X, self.Y, self.freq = x, y, f * 1000
        self.click_at_position()

    def click_at_position(self):
        pyautogui.click(self.X, self.Y)
        print(f'freq = {self.freq} ms')
        self.app.after(self.freq, self.click_at_position)

    def callback_mouse(self, event):         
        self.curX, self.curY = event.x, event.y
        print(self.curX, self.curY)
    
    def update_position_value_label(self):
        self.curX, self.curY = pyautogui.position()
        context = f'X: {self.curX}, Y: {self.curY}'
        self.position_value_label.config(text=context)
        self.app.after(100, self.update_position_value_label)

e = Event()
e.run()