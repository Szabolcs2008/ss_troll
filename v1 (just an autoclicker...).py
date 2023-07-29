import subprocess
import sys
import ctypes
import time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()


def BSOD0():
    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("BSOD Successfull!")
    else:
        print("BSOD Failed...")


def BSOD1():
    rc = subprocess.run(["powershell", "-Command", "wininit"], capture_output=True)


if len(sys.argv) > 1:
    if "--type=0" in sys.argv:
        BSOD0()
        sys.exit()
    if "--type=1" in sys.argv:
        if is_admin():
            BSOD1()
            sys.exit()
        else:
            print('Run me as admin')

if is_admin():
    print('0) 0xDEADDEAD (works without administrator)\n'
          '1) CITICAL PROCESS DIED (requires admin)')
    inp = input('Ur pc is about to bluescreen! chose a BSOD msg (default: 0) ')
    if inp == "":
        BSOD0()
    if inp == "0":
        BSOD0()
    if inp == "1":
        BSOD1()
        time.sleep(3)
        print("Well that did not work, try running me as an admin")
else:
    print('Run me as admin')
