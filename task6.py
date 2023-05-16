# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    """Print multiplication table up to max value 25"""
    multiplier = 1

    while multiplier <= 25:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(4)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_nums(x, y):
    """Calculating the sum of two numbers"""
    sum = x + y
    return print(f"Сума числа {x} та {y} дорівнює {sum}.")
#sum_two_nums(3, 7)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers_list = [1, 2, 3, 4]

def arithmetical_mean(numbers):
    """Calculate arithmetical mean"""
    return print(f"{sum(numbers) / len(numbers)}")

#arithmetical_mean(numbers_list)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string_to_reverse):
    """Reverse a string"""
    return string_to_reverse[::-1]

string = "Купила мама коника"
reversed = reverse_string(string)
print(reversed)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
word_list = ["one", "a", "quartern", "engage"]
def longest_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
#print(f"Найдовше слово в списку : {longest_word(word_list)}.")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""