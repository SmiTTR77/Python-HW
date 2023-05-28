main_menu = '''\nГлавное меню:
	1. Открыть файл
 	2. Записать файл
  	3. Показать контакт
	4. Добавить контакт
 	5. Найти контакт
  	6. Изменить контакт
	7. Удалить контакт
	8. Выход\n'''

input_choise = 'Выберите пункт меню: '

load_succesful = 'Телефонная книга успешно открыта'
load_error = 'Телефонная книга пуста, или не открыта'

save_succesful = 'Телефонная книга успешно сохранена'

input_contact = {'name': 'Введите имя: ',
                 'phone': 'Введите телефон: ',
                 'comment': 'Введите комментарий: '}

cancel_input = 'Отмена ввода'

new_contact = 'Введите данные нового контакта (пустое поле для отмены): '

new_change_contact = 'Введите новые данные контакта: '

find_choise = 'Введите параметр для поиска: '
find_error = 'Ничего не найдено'


def find_succesful(count: int) -> int:
    return f'Найдено записей: {count}'


def new_contact_succesful(name: str) -> str:
    return f'Контакт {name} успешно добавлен'


index_change_contact = 'Введите номер контакта, который хотите изменить: '


def change_contact(name: str):
    return f'Контакт {name} успешно изменен!'


index_del_contact = 'Введите номер контакта, который хотите удалить: '


def del_contact(name: str):
    return f"Контакт {name} успешно удален!"
