# Задача 38 (на основе задачи 55):
# Условия и декомпозиции задач вынесены в файл (README.md)

from os import path


def read_file(read_file_name):
    with open(read_file_name, 'r') as pb_file:  # 3.1. + 4.3. + 5.3. + 6.2. + 7.5. + 8.3. + 9.3. + 10.3.
        return pb_file.read()  # 3.2. + 4.4. + 5.4. + 6.3. + 7.6. + 8.4. + 9.4. + 10.4.

def append_file(append_file_name, append_data):
    with open(append_file_name, 'a') as pb_file:  # 1.1. + 2.3. + 5.6. + 6.5. + 7.10. + 8.8.
        pb_file.write(append_data)  # 1.2. + 2.4. + 5.7. + 6.6. + 7.11. + 8.9.

def write_file(write_file_name, write_list):
    with open(write_file_name, 'w') as pb_file:  # 9.14. + 10.12.
        pb_file.write('\n\n'.join(write_list) + '\n\n')  # 9.15. + 9.16. + 10.13. + 10.14.

def get_contacts_list(file_name):  # (3.)
    return read_file(file_name).rstrip().split('\n\n')  # 4.5. + 7.7. + 8.5. + 9.5. + 10.5.

def input_contact():  # 2.
    surname = input('Введите Фамилию контакта: ').title()  # 2.1.
    name = input('Введите Имя контакта: ').title()  # 2.1.
    patronymic = input('Введите Отчество контакта: ').title()  # 2.1.
    phone = input('Введите Телефон контакта: ')  # 2.1.
    address = input('Введите Адрес контакта: ')  # 2.1.
    added_contact = f'{surname} {name} {patronymic} {phone}\n{address}\n\n'  # 2.2.
    append_file('phonebook.txt', added_contact)
    print()

def print_data(print_file_name='phonebook.txt'):  # 3
    contacts_list = get_contacts_list(print_file_name)
    for num, elem in enumerate(contacts_list, 1):
        print(f'{num}:\n{elem}\n')  # 3.3. + 7.3.

def select_param():
    print('Параметры контакта:\n'
          '1) Фамилия\n'
          '2) Имя\n'
          '3) Отчество\n'
          '4) Телефон\n'
          '5) Адрес'
          )
    param = input('Введите номер параметра контакта: ')  # 4.1. + 9.1. + 9.11. + 10.1.
    while param not in ('1', '2', '3', '4', '5'):
        print('Не корректный номер параметра! Повторите ввод.')
        param = input('Введите номер параметра контакта: ')  # 4.1. + 9.1. + 9.11. + 10.1.
    return int(param) - 1

def search_contact():  # 4.
    ind_param = select_param()
    search = input('\nВведите данные контакта для поиска: ').title()  # 4.2.
    print()
    contacts_list = get_contacts_list('phonebook.txt')  # 4.6.
    for contact_str in contacts_list:
        contact_params_list = contact_str.replace('\n', ' ').split()  # 4.7.
        if search in contact_params_list[ind_param]:  # 4.8.
            print(contact_str + '\n')  # 4.9.

def add_data(source, target):
    source_data = read_file(source)  # 5.5. + 6.4.
    append_file(target, source_data)

def import_data():  # 5.
    import_file = input('Введите имя импортируемого ".txt" файла (без расширения): ') + '.txt'  # 5.1.
    if path.exists(import_file):  # 5.2.
        add_data(import_file, 'phonebook.txt')
        print(f'\nФайл "{import_file}" импортирован.\n')
    else:
        print(f'\nФайла "{import_file}" не существует.\n')  # 5.2.

def export_data():  # 6.
    export_file = input('Введите имя ".txt" файла для экспорта справочника (без расширения): ') + '.txt'  # 6.1.
    add_data('phonebook.txt', export_file)
    print(f'\nЭкспорт справочника в файл "{export_file}" выполнен.\n')

def add_contact(source, target, position):    # (7.)
    contacts_list = get_contacts_list(source)  # 7.8. + 8.6.
    if 1 <= position <= len(contacts_list):  # 7.9. + 8.7.
        append_file(target, f'{contacts_list[position - 1]}\n\n')
        return True
    else:
        return False

def import_contact():  # 7.
    source_file = input('Введите имя ".txt" файла для импорта контакта (без расширения): ') + '.txt'  # 7.1.
    if path.exists(source_file):  # 7.2.
        print()
        print_data(source_file)
        num = int(input('Введите порядковый номер импортируемого контакта: '))  # 7.4.
        if add_contact(source_file, 'phonebook.txt', num):
            print(f'\nИмпорт контакта из файла "{source_file}" выполнен.\n')
        else:
            print(f'\nВ файле "{source_file}" нет контакта c порядковым номером {num}.\n')
    else:
        print(f'\nФайла "{source_file}" не существует.\n')  # 7.2.

def export_contact():  # 8.
    target_file = input('Введите имя ".txt" файла для экспорта контакта (без расширения): ') + '.txt'  # 8.1.
    num = int(input('Введите порядковый номер экспортируемого контакта: '))  # 8.2.
    if add_contact('phonebook.txt', target_file, num):
        print(f'\nЭкспорт контакта в файл "{target_file}" выполнен.\n')
    else:
        print(f'\nВ файле "phonebook.txt" нет контакта c порядковым номером {num}.\n')

def yes_no():
    print('Подтвердите или отмените действие:\n'
          '1) Yes\n'
          '2) No'
          )
    check = input('Введите номер операции: ')  # 9.10. + 10.10.
    while check not in ('1', '2'):
        print('Не корректный номер операции! Повторите ввод.')
        check = input('Введите номер операции: ')  # 9.10. + 10.10.
    if int(check) == 1: return True
    else: return False

def change_contact():
    ind_param_search = select_param()
    change = input('\nВведите данные контакта для изменения: ').title()  # 9.2.
    contacts_list = get_contacts_list('phonebook.txt')  # 9.6.
    for i in range(len(contacts_list)):
        contact_params_list = contacts_list[i].replace('\n', ' ').split()  # 9.7.
        if change in contact_params_list[ind_param_search]:  # 9.8.
            print('\n' + contacts_list[i] + '\n\nИзменить контакт?\n')  # 9.9.
            if yes_no():
                print('\nКакой параметр нужно изменить?\n')
                ind_param_change = select_param()
                contact_params_list[ind_param_change] = input('\nВведите новые данные: ').title()  # 9.12.
                contacts_list[i] = f'{contact_params_list[0]} {contact_params_list[1]} {contact_params_list[2]} {contact_params_list[3]}\n{contact_params_list[4]}'  # 9.13.
                print('\nКонтакт изменён.')
    write_file('phonebook.txt', contacts_list)
    print()

def delete_contact():
    ind_param = select_param()
    delete = input('\nВведите данные контакта для удаления: ').title()  # 10.2.
    contacts_list = get_contacts_list('phonebook.txt')  # 10.6.
    for i in range(-1, -len(contacts_list), -1):
        contact_params_list = contacts_list[i].replace('\n', ' ').split()  # 10.7.
        if delete in contact_params_list[ind_param]:  # 10.8.
            print('\n' + contacts_list[i] + '\n\nУдалить контакт?\n')  # 10.9.
            if yes_no():
                del contacts_list[i]  # 10.11.
                print('\nКонтакт удалён.')
    write_file('phonebook.txt', contacts_list)
    print()

def interface():  # 0.
    command = ''
    close = '0'
    while command != close:
        print('Выберите вариант работы с телефонным справочником:\n'
              '1) Добавить контакт\n'
              '2) Показать весь телефонный справочник\n'
              '3) Найти контакты\n'
              '4) Импорт всех данных\n'
              '5) Экспорт всех данных\n'
              '6) Импорт контакта\n'
              '7) Экспорт контакта\n'
              '8) Изменить контакт\n'
              '9) Удалить контакт\n'
              '0) Выход'
              )
        command = input('Введите номер операции: ')
        while command not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', close):
            print('Не корректный номер операции! Повторите ввод.')
            command = input('Введите номер операции: ')
        print()
        match command:
            case '1': input_contact()  # 0.1.
            case '2': print_data()  # 0.2.
            case '3': search_contact()  # 0.3.
            case '4': import_data()  # 0.4.
            case '5': export_data()  # 0.5.
            case '6': import_contact()  # 0.6.
            case '7': export_contact()  # 0.7.
            case '8': change_contact()  # 0.8.
            case '9': delete_contact()  # 0.9.
            case close: print('Bye-bye!')  # 0.10.
        if command != close:
            input('Нажмите <Enter> для продолжения: ')
            print()

append_file('phonebook.txt', '')  # (1.)
interface()  # (0.)
