small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

small_set = set(small_list)
print(small_set)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

count = 0
for i in small_list:
    count += i
№print(count, len(small_set))
print(f"Середньє арифметичне усіх елементів у спиcку \"small_list\": {count / len(small_set)}")

# task 3. Перевірте, чи є в списку big_list дублікати

big_set = set(big_list)
if len(big_list) == len(big_set):
    print(f"Усі елементи в списку \"big_list\" унікальні!")
else:
    print(f"Не усі елементи в списку \"big_list\" унікальні!")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

the_biggest = max(add_dict)
print(f"Ключ з максимальним значенням у словнику \"add_dict\": {the_biggest} .")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

get_keys = set(base_dict.keys())
get_values = set(base_dict.values())
#new_keys = get_keys
new_dict = dict(zip(get_values, get_keys))
print("Словник в якому ключі та значення замінені місцями: ", new_dict)

# # task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = {}
for key, value in base_dict.items():
    if key in add_dict:
        sum_dict[key] = str(value) + str(add_dict[key])
    else:
        sum_dict[key] = value

for key, value in  add_dict.items():
    if key not in sum_dict:
        sum_dict[key] = value

print("Словник в якому об\'єднані два словники і складені значення, якщо збігаються ключі: ", sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

line_set = set(line)
print(f"Набір символівб що входять в строку \"line\": {line_set}.")

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

set_1_differ = set_1.difference(set_2)
set_2_differ = set_2.difference(set_1)
sum_differ = sum(set_1_differ) + sum(set_2_differ)
print(f"Сума значень двох множин, які не є спільними: {sum_differ}.")

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
sum_list = list_1 + list_2
sum_set = set(sum_list)
print(f"Сет з двох списків з унікальними значеннями: {sum_set}.")

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
age_ranges = {'10-19' : [], '20-29' : [], '30-39' : [], '40-49' : []}
for person in person_list:
    name, age = person
    if age >= 10 and age <= 19:
        age_ranges['10-19'].append(name)
    elif age >= 20 and age <= 29:
        age_ranges['20-29'].append(name)
    elif age >= 30 and age <= 39:
        age_ranges['30-39'].append(name)
    elif age >= 40 and age <= 49:
        age_ranges['40-49'].append(name)

print(f"Словник імен і вікових діапазонів: {age_ranges}.")
