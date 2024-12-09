from PIL import Image
from supp_mods import files


def compress_img():
    images = files.find_files('.jpg', '.jpeg', '.gif', '.png')
    if images == {}:
        pass
    else:
        while True:
            choice = input('Выберите изображение, которое необходимо сжать (выберите 0, если необходимо сжать все): ')
            if not choice.isdigit() or (int(choice) not in list(images.keys()) and int(choice) != 0):
                print('Выбрано неправильное изображение!')
            else:
                break
        while True:
            compression = input('Введите степень сжатия (от наибольшей к наименьшей: 1-100): ')
            if not compression.isdigit():
                print('Введено не число!')
            elif not (1 <= int(compression) <= 100):
                print('Введите число от 1 до 100')
            else:
                break
        if int(choice) == 0:
            for i in list(images.values()):
                image_file = Image.open(i)
                image_file.save('compressed'+i, quality=int(compression))
                print(f'Изображение {i} сжато')
        else:
            image = images.get(int(choice))
            image_file = Image.open(image)
            image_file.save('compressed'+image, quality=int(compression))
            print(f'Изображение {image} сжато')
