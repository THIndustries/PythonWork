# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной  записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def read_file():#печатаем весь справочник
    with open(path_file,'r',encoding='UTF-8') as f:
        print('Список контактов:\n'+f.read()+'\n')


def app_in_file(): #добавляем в конец файла
    with open(path_file,'a',encoding='UTF-8') as f:
        f.writelines('\n'+input('Введите новый контакт (ФИО номер): '))


def find_file():#поиск контакта по файлу
    find_info = input('Укажите имя, фамилию или номер(часть номера) контакта: ')
    with open(path_file,'r',encoding='UTF-8') as f:
        print('Результат поиска:')
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line.strip())
    print()


def read_file_into_list():#загрузка файла в список
    with open(path_file,'r',encoding='UTF-8') as f:
        phone_book =[]
        for   line in f:
            if line.strip() !="": phone_book.append(line.strip())        
    return phone_book


def write_list_into_file(phone_book):
    with open(path_file,'w',encoding='UTF-8') as f:
        phone_book.sort()
        for item in phone_book:
            f.write ('\n'+item)


def find_in_list_and_change(phone_book):#поиск по списку и редактирование(изм/уд) контактов
    find_info = input("Укажите имя, фамилию или номер(часть номера) контакта: ")
    for item in phone_book:
        if find_info.casefold() in item.casefold():
            print(item.strip())
            if input("Редактируем эту запись д/н: ") == "д".casefold(): 
                while True:
                    request = input('(И)зменить или (У)далить запись: ')
                    if  request.casefold() == 'у'.casefold():
                        phone_book.remove(item)
                        write_list_into_file(phone_book)
                        return
                    elif request.casefold() == 'и'.casefold():
                        new_item =input('Введите исправленный контакт (ФИО и номер): ')
                        phone_book.remove(item)
                        phone_book.append(new_item)
                        write_list_into_file(phone_book)
                        return
        else: continue
    print('Ничего не найдено')
            

def consol_menu():
    while True:
        print('Меню команд:')
        text = input("(П)оказать весь справочник.\n(На)йти контакт\n(Но)вый контакт\n(Р)едактировать контакт\n(В)ыход из меню\n ->")
        if text.casefold() == 'Показать весь справочник'.casefold() or text.casefold() == 'П'.casefold():
            read_file()
        elif text.casefold() == 'Найти контакт'.casefold() or text.casefold() == 'На'.casefold():
            find_file()
        elif text.casefold() == 'Новый контакт'.casefold() or text.casefold() == 'Но'.casefold():
           app_in_file()
        elif text.casefold() == 'Редактировать контакт'.casefold() or text.casefold() == 'р'.casefold():
            
            find_in_list_and_change(read_file_into_list())
               
        elif text.casefold() == 'Выход из меню'.casefold() or text.casefold() == 'В'.casefold():
            print('Доброго дня!')
            return   
        else: print("Ошибка ввода!")


path_file = r'Telephonebook.txt'
consol_menu()