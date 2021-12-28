import os
import string
import random
import winreg


def rand(chars_number : int):
    _str = ''
    for i in range(0, chars_number):
        if random.randint(0,1):
            _str += str(random.randint(1, 9))
        else:
            _str += random.choice(string.ascii_lowercase)
    return _str


new_inst_uid = f"{rand(8)}-{rand(4)}-{rand(4)}-{rand(4)}-{rand(12)}"


REG_PATH = r'SOFTWARE\Wow6432Node\SkyLine\Plagiarism Detector App Settings'
try:
    winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
    registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, 'inst_uid', 0, winreg.REG_SZ, new_inst_uid)
    winreg.CloseKey(registry_key)
except WindowsError as e:
    print(e)
    os.system("pause")
    exit(0)


print("\n\n\n====================================================\n")
print("---------- Plagiarism Detector was reset. ----------")
print("\n====================================================\n\n\n")
os.system("pause")
