from pomosh import *

while True:
    plesure = files.return_curr_dir()
    print(f'Текущий каталог: {plesure}')
    print('Выберите действие:\n\n0. Сменить рабочий каталог\n1. Преобразовать PDF в Dock\n2. Преобразовать Docx в '
          'PDF\n3. Произвести сжатие изображений\n4. Удалить группу файлов\n5. Выход')
    while True:
        choice = input('Выбор: ')
        if not choice.isdigit() or choice not in ['0', '1', '2', '3', '4', '5']:
            print('Введено неправильное действие!')
        else:
            break
    if choice == '0':
        delete.change_dir()
    elif choice == '1':
        pdftodoc.pdf_to_docx()
    elif choice == '2':
        pdftodoc.docx_to_pdf()
    elif choice == '3':
        image.compress_img()
    elif choice == '4':
        delete.delete_files()
    elif choice == '5':
        print('Goodbye :)')
        exit()
    else: 
        print("\033[35m{}".format(' ' * 10 + 'Всё заблагорассудится!\n'),
              "\033[0m{}".format(' ' * 9 + 'До скорой встречи!'))
