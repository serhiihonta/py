adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
print(adventures_of_tom_sawer)
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

# Очищення тексту від випадкових переносів
text_clear_br = adventures_of_tom_sawer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""
# Очищення тексту від зайвих крапок
text_clear_dots = text_clear_br.replace("....", " ")
#print(text_clear_dots)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

# Очищення тексту від зайвих пробілів
text_clear_spaces = text_clear_dots.replace("  ", "").strip()
print("free from spaces",text_clear_spaces)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_letter = adventures_of_tom_sawer.count("h")
print(f"Літера \"h\" зустрічається в тексті {h_letter} разів.")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
upper_count = 0
for i in adventures_of_tom_sawer:
    if i.isupper():
        upper_count += 1
print(upper_count)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_Tom = text_clear_spaces.find("Tom")
second_Tom = text_clear_spaces.find("Tom", first_Tom + 1)
print(second_Tom)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = text_clear_spaces.split(".")
print(adventures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
third_sentence = adventures_of_tom_sawer_sentences[3]
print(third_sentence.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
string_for_search = "By the time"
if text_clear_spaces.find(string_for_search):
    print(f"Речення що починається з {string_for_search} присутнє в тексті!")
else:
    print(f"Речення що починається з {string_for_search} відсутнє в тексті!")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

the_last_sentence = adventures_of_tom_sawer_sentences[-1]
word_count = len(the_last_sentence.split(" "))
print(word_count)