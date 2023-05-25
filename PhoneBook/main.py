# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать справочник
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# ------------------------------------------------

# Путь
path = 'phonebook.txt'

# Главное меню:


def main_menu():
    print('1 - Показать справочник')
    print('2 - Добавить новый контакт')
    print('3 - Найти контакт')
    print('4 - Изменить контакт')
    print('5 - Удалить контакт')
    print('6 - Очистить справочник')
    print('7 - Выход')

    menu = int(input('Выберите действие: '))
    match menu:
        case 1:
            show_contacts()
        case 2:
            add_contact()
        case 3:
            find_contact()
        case 4:
            change_contact()
        case 5:
            del_contact()
        case 6:
            clear_all()
        case 7:
            exit_book()

# Подменю: (не используется)


def sub_menu():
    print('1 - Изменить контакт')
    print('2 - Удалить контакт')
    print('3 - В главное меню')

    menu = int(input('Выберите действие: '))
    match menu:
        case 1:
            change_contact()
        case 2:
            del_contact()
        case 3:
            main_menu()

# Подменю 2: (не используется)


def resub_menu():
    print('1 - Изменить имя')
    print('2 - Изменить фамилию')
    print('3 - Изменить отчество')
    print('4 - Изменить телефон')

    menu = int(input('Выберите действие: '))
    match menu:
        case 1:
            main_menu()
        case 2:
            main_menu()
        case 3:
            main_menu()
        case 4:
            main_menu()

# 1. Показать справочник


def show_contacts():
    with open(path, 'r', encoding='UTF-8') as file:
        print('Список контактов:')
        print(file.read())
        main_menu()

# 2. Добавить контакт


def add_contact():
    with open(path, 'a', encoding='UTF-8') as file:
        last_name = input('Введите Фамилию: ').capitalize().replace(' ', '')
        name = input('Введите Имя: ').capitalize().replace(' ', '')
        mid_name = input('Введите Отчество: ').capitalize().replace(' ', '')
        phone = input('Введите телефон: ')
        file.write(f'{last_name} {name} {mid_name} {phone} \n')
        print('Контакт добавлен')
        main_menu()

# 3. Найти контакт


def find_contact(str='Введите значение для поиска или нажмите "Enter" для просмотра всех контактов: '):
    with open(path, 'r+', encoding='UTF-8') as file:
        find_list = []
        find_count = 0
        seach_value = input(str).capitalize()

        for index, line in enumerate(file):
            if seach_value in line:
                find_list.append({'number': index + 1, 'contact': line})
                find_count += 1

        if find_list:
            print(f'Найдено {find_count} записей')
            for contact in find_list:
                print(f"{contact['number']} : {contact['contact']}")
            # sub_menu()
        else:
            print('Ничего не найдено')
            main_menu()
        return find_list


# 4. Изменить контакт


def change_contact():
    find_list = find_contact()
    change_number = int(
        input('Введите номер контакта который необходимо изменить: '))
    replaced_contact = []

    for record in find_list:
        if record['number'] == change_number:
            replaced_contact.append(record['contact'])
            print(replaced_contact[0])

    temp_contact = str(replaced_contact).split()

    print('1 - Изменить имя')
    print('2 - Изменить фамилию')
    print('3 - Изменить отчество')
    print('4 - Изменить телефон')
    change_numb = int(input('Выберите действие: '))

    for i in range(len(temp_contact)):
        if i == change_numb-1:
            temp_contact[i] = input('Введите новое значение: ')

    re_cont = ' '.join(temp_contact)
    print(re_cont)
    print('Данные успешно изменены')

    # copy_phonebook = get_txt_copy
    # new_phonebook = []
    # with open(path, 'r+', encoding='UTF-8') as file:
    #     for line in file:
    #         if line[i] == change_numb-1:
    #             new_phonebook.append(re_cont)
    #         else:
    #             new_phonebook.append(copy_phonebook[i])
    #     print('new_phonebook')


# Доп функции:

def get_txt_copy():
    with open(path, 'r', encoding='UTF-8') as file:
        file_copy = []

        for line in file:
            file_copy.append(line.rstrip('\n'))

        return file_copy

# 5. Удалить контакт


def del_contact():
    with open(path, 'r+', encoding='UTF-8') as file:
        print('в разработке')

# 6. Очистить справочник


def clear_all():
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('')

# 7. Выход


def exit_book():
    print('Справочник закрыт')
    exit()


# Запуск
main_menu()
