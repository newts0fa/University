import os


def return_curr_dir():
    return os.getcwd()


def change_dir():
    while True:
        try:
            num = input('Введите новый путь: ')
            os.chdir(num)
            print('Путь успешно изменён')
            break
        except (NotADirectoryError, IsADirectoryError, FileNotFoundError, OSError):
            print('Неправильно введён путь!')


pleas = 1
def find_files(*args, type:int=0):
    global pleas
    searching_for = tuple([*args])
    file_list = os.listdir(os.getcwd())
    file_nums = {}
    print(f'Поиск файлов с подстрокой {", ".join([*args])} в данном каталоге')
    if type == 0:
        for i in file_list:
            if i.endswith(searching_for):
                file_nums[len(file_nums) + 1] = i
                print(str(len(file_nums)) + ': ' + i)
    elif type == 1:
        for i in file_list:
            if i.startswith(searching_for):
                file_nums[len(file_nums) + 1] = i
                print(str(len(file_nums)) + ': ' + i)
    elif type == 2:
        for i in file_list:
            end = i.rindex('.')
            if i[:end].endswith(searching_for):
                file_nums[len(file_nums) + 1] = i
                print(str(len(file_nums)) + ': ' + i)
    elif type == 3:
        for i in file_list:
            end = i.rindex('.')
            for wanted in searching_for:
                if wanted in i[:end]:
                    file_nums[len(file_nums) + 1] = i
                    print(str(len(file_nums)) + ': ' + i)
    else:
        print("Для чего вам это?")
    if file_nums == {}:
        if pleas:
            pleas = 0
            print("\033[33m{}".format('\n'+' ' * 10 + 'Advancement Made!\n'),
                  "\033[0m{}".format(' ' * 9 + 'We Need to Go Deeper\n'))
        print('Файлы не найдены. Попробуйте другой каталог')
        return file_nums
    return file_nums


def delete_files():
    print('Выберите действие:\n\n1. Удалить все файлы начинающиеся на введенную подстроку\n2. Удалить все файлы '
          'оканчивающиеся на введенную подстроку\n3. Удалить все файлы содержащие введенную подстроку\n'
          '4. Удалить файлы по расширению')
    while True:
        choice = input('Выбор: ')
        if not choice.isdigit() or choice not in ['1', '2', '3', '4']:
            print('Введено неправильное действие!')
        else:
            break
    stroka= input('Введите подстроку: ')
    if choice == '1':
        for i in list(find_files(stroka, type=1).values()):
            try:
                os.remove(i)
                print(f'Файл {i} удален успешно')
            except PermissionError:
                print('Недостаточно прав для удаления!')
    elif choice == '2':
        for i in list(find_files(stroka, type=2).values()):
            try:
                os.remove(i)
                print(f'Файл {i} удален успешно')
            except PermissionError:
                print('Недостаточно прав для удаления!')
    elif choice == '3':
        for i in list(find_files(stroka, type=3).values()):
            try:
                os.remove(i)
                print(f'Файл {i} удален успешно')
            except PermissionError:
                print('Недостаточно прав для удаления!')

    else:
        if not stroka.startswith('.'):
            stroka = '.' + stroka
        for i in list(find_files(stroka, type=0).values()):
            try:
                os.remove(i)
                print(f'Файл {i} удален успешно')
            except PermissionError:
                print('Недостаточно прав для удаления!')
