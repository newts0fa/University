import random

def load_words(filename):
    """Загрузка слов из файла."""
    try:
        with open('worlds.txt', "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]
            if not words:
                raise ValueError("Файл не содержит слов.")
            return words
    except FileNotFoundError:
        print("Файл со словами не найден. Убедитесь, что файл существует.")
        exit()
    except Exception as e:
        print(f"Ошибка при загрузке слов: {e}")
        exit()

def select_difficulty():
    """Выбор уровня сложности."""
    while True:
        try:
            print("Выберите уровень сложности:")
            print("1. Легкий (7 жизней)")
            print("2. Средний (5 жизней)")
            print("3. Сложный (3 жизни)")
            choice = int(input("Ваш выбор: "))
            if choice == 1:
                return 7
            elif choice == 2:
                return 5
            elif choice == 3:
                return 3
            else:
                print("Введите число от 1 до 3.")
        except ValueError:
            print("Некорректный ввод. Введите число от 1 до 3.")

def mask_word(word, revealed):
    """Создание строки с маскированным словом."""
    return "".join(char if revealed[i] else "■" for i, char in enumerate(word))

def is_word_revealed(revealed):
    """Проверка, угадано ли слово полностью."""
    return all(revealed)

def play_round(word, lives):
    """Игровой раунд."""
    revealed = [False] * len(word)
    print(f"Игра началась! у вас {lives} жизней.")
    
    while lives > 0:
        print(f"Слово: {mask_word(word, revealed)}")
        guess = input("Введите букву или слово целиком: ").strip().lower()

        # Проверка ввода
        if not guess.isalpha():
            print("Некорректный ввод. Введите только буквы.")
            continue

        if len(guess) == 1:
            # Игрок ввел букву
            if guess in word:
                print(f"Буква '{guess}' есть в слове!")
                for i, char in enumerate(word):
                    if char == guess:
                        revealed[i] = True
            else:
                lives -= 1
                print(f"Буквы '{guess}' нет в слове. Осталось жизней: {lives}")
        else:
            # Игрок ввел слово
            if guess == word:
                print(f"Поздравляем! Вы угадали слово: {word}")
                return True
            else:
                lives -= 1
                print(f"Неверное слово. Осталось жизней: {lives}")

        if is_word_revealed(revealed):
            print(f"Поздравляем! Вы угадали слово: {word}")
            return True

    print(f"Вы проиграли. Загаданное слово: {word}")
    return False

def play_game(word_list):
    """Основная игровая функция."""
    while word_list:
        word = random.choice(word_list)
        word_list.remove(word)
        lives = select_difficulty()

        try:
            success = play_round(word, lives)
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}. Попробуйте перезапустить игру.")
            return

        if not word_list:
            print("Слова закончились! Спасибо за игру!")
            break

        play_again = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
        if play_again != "да":
            print("Спасибо за игру! До новых встреч!")
            break

# Основной запуск игры
    words = load_words("words.txt")  
    play_game(words)
