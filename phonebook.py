
""" Задача №49. Решение в группах Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
1. Программа должна выводить данные 
2. Программа должна сохранять данные в текстовом файле 
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 


# 1. прога запускается, пробует подключиться к файлу
# 2. если файл есть то загружаем данные в коллекцию
# 3. если файла нет то можно подгрузить набор данных по умолчанию
# 4. внутри постоянно идет цикл While True , постоянно запрашивается некая команда
# 5. идет обработка этой команды
# 6. новая итерация цикла
# 7. если стоп слово то выходим из цикла
# 8. автоматическое сохранение в файл"""

from random import *
import json
from easygui import *
import os.path

phonebook = {}

def save():
    with open("phoneb.json", "w", encoding="utf-8") as pb:
        pb.write(json.dumps(phonebook, ensure_ascii=False))
    print("Наша телефонная книга была успешно сохранена в файле phoneb.json")

#if os.path.isfile("phoneb.json"):
def load_p():
    try:
        with open("phoneb.json", "w", encoding="utf-8") as pb:
            phonebook = json.load(pb)
        print("Наша телефонная книга была успешно загружена")
    except:
        phonebook = {"дядя Ваня":{"phones": [1231654,45646644],
        "birthday": "01.01.1960",
        "email": "vanya@mail.ru" },
        "дядя Вася": {"phones" : [12121244444]}
        }
    return phonebook
    
try:
    with open("phoneb.json", "w", encoding="utf-8") as pb:
        phonebook = json.load(pb)
    print("Наша телефонная книга была успешно загружена")
except:
    phonebook = {"дядя Ваня":{"phones": [1231654,45646644],
    "birthday": "01.01.1960",
    "email": "vanya@mail.ru" },
    "дядя Вася": {"phones" : [12121244444]}
    }
while True:
    choice = choicebox("Выберите действие", "Главное меню", ["Добавление (изменение) записи", "Просмотр телефонной книги", 
    "Загрузка телефонной книги", "Поиск записи", "Удаление записи",
    "Сохранение телефонной книги", "Выход"])
    if choice == "Выход":
        msgbox("Телефонная книга сохранена.")
        save()
        break
    elif choice == "Добавление (изменение) записи":
        abonent_fio = input("Введите данные Ф.И.О. абонента ")
        abonent_atr = input("Введите данные телефонного абонента ")
        phonebook.update({abonent_fio: abonent_atr})
        msgbox("Телефонная книга дополнена.")
    elif choice == "Просмотр телефонной книги":
        msg = phonebook
        msgbox(msg, "Просмотр телефонной книги")
    elif choice == "Загрузка телефонной книги":
        with open("phoneb.json", "w", encoding="utf-8") as pb:
            phonebook = json.load(pb)
        msgbox("Телефонная книга успешно загружена.")
    elif choice == "Сохранение телефонной книги":
        save()
        msgbox("Телефонная книга успешно сохранена.")
    elif choice == "Удаление записи":
        abonent_fio = input("Введите данные Ф.И.О. удляемого абонента ")
        phonebook.pop(abonent_fio)
        msgbox("Запись успешно удалена.")        
    elif choice == "Поиск записи":
        abonent_fio = input("Введите данные Ф.И.О. абонента ")
        if abonent_fio in phonebook:
            msgbox(phonebook.get(abonent_fio), "Найдена поисковая запись в телефонной книге")
        else:
            msgbox("Поисковая запись в телефонной книге не найдена ")


