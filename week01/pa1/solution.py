# -*- coding: utf-8 -*-
# useful links
# https://habrahabr.ru/post/172043/
# http://www.webpages.uidaho.edu/~stevel/504/Pandas%20DataFrame%20Notes.pdf
import pandas

from utils import pretty_print

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
# print(data[:10])
# print(data.head())

# pretty_print()

# print(data['Survived'])
print(data['Survived'].value_counts())
# print(data['Pclass'].value_counts())
# print(data['Pclass'].value_counts())

pretty_print()

print("1) Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров."
      "Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.")
print(data['Sex'].value_counts())
print(data['Sex'].count())

pretty_print()

print("2) Какую долю пассажиры первого класса составляли среди всех пассажиров? "
      "Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.")
print(data['Survived'][data['Survived'] == 1].count())
print(data['Survived'][data['Survived'] == 0].count())
print(data['Survived'].count())
print(float(data['Survived'][data['Survived'] == 1].count()) / data['Survived'].count() * 100)

pretty_print()

print("3) Какую долю пассажиры первого класса составляли среди всех пассажиров? "
      "Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.")
print(data['Pclass'][data['Pclass'] == 1].count())
print(data['Pclass'].count())
print(float(data['Pclass'][data['Pclass'] == 1].count()) / data['Pclass'].count() * 100)

pretty_print()

print("4) Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров.")
print(data['Age'].mean())
print(data['Age'].median())
with open('pa1/answers/question4.txt', 'w') as f:
    f.write('%s %s' % (str(round(data['Age'].mean(), 2)), str(round(data['Age'].median(), 2))))

pretty_print()

print("5) Коррелируют ли число братьев/сестер/супругов с числом родителей/детей? "
      "Посчитайте корреляцию Пирсона между признаками SibSp и Parch.")
print(data['SibSp'].corr(data['Parch']))
with open('pa1/answers/question5.txt', 'w') as f:
    f.write(str(round(data['SibSp'].corr(data['Parch']), 2)))

pretty_print()

# TODO
print("6) Какое самое популярное женское имя на корабле? "
      "Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name). "
      "Это задание — типичный пример того, с чем сталкивается специалист по анализу данных. "
      "Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию. "
      "Попробуйте вручную разобрать несколько значений столбца Name и выработать правило для извлечения имен, "
      "а также разделения их на женские и мужские.")


def get_name(first_name_to_parse):
    if 'Mrs.' in first_name_to_parse:
        if '(' in first_name_to_parse:
            # Bystrom, Mrs. (Karolina)
            return first_name_to_parse.split('(')[1].strip(')').split()[0]
        else:
            # Masselmani, Mrs. Fatima
            return first_name_to_parse.split('Mrs.')[1].strip().split()[0]
    elif 'Miss.' in first_name_to_parse:
        return first_name_to_parse.split('Miss.')[1].strip().split()[0]


female_names = pandas.DataFrame(data[data['Sex'] == 'female']['Name'])
pretty_print()
print(female_names)

names_filtered = female_names['Name'].apply(func=get_name)

pretty_print()

print(names_filtered)

pretty_print()

print(names_filtered.value_counts())
