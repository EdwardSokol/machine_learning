# -*- coding: utf-8 -*-
import pandas

from utils import pretty_print

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
# print(data[:10])
# print(data.head())

pretty_print()

# print(data['Survived'])
# print(data['Survived'].value_counts())
# print(data['Pclass'].value_counts())
# print(data['Pclass'].value_counts())

pretty_print()

print(data['Sex'].value_counts())
print(data['Sex'].count())

pretty_print()

print(data['Survived'][data['Survived'] == 1].count())
print(data['Survived'][data['Survived'] == 0].count())
print(data['Survived'].count())
print(float(data['Survived'][data['Survived'] == 1].count()) / data['Survived'].count() * 100)
