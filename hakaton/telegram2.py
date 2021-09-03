
import random

# число попыток угадать
guesses_made = 0

# получаем имя пользователя из консольного ввода
name = input('Привет! Как тебя зовут?\n')

# получаем случайное число в диапазоне от 1 до 30
number = random.randint(1, 10)
print ('Отлично, {0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))

while guesses_made < 6:
    
    # получаем число от пользователя
    guess = int(input('Введи число: '))
    
    guesses_made += 1

    if guess < number:
        print ('Твое число меньше того, что я загадал.')

    if guess > number:
        print ('Твое число больше загаданного мной.')

    if guess == number:
        break

if guess == number:
    print ('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
else:
    print ('А вот и не угадал! Я загадал число {0}'.format(number))
 
