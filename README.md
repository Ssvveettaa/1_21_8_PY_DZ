### 1 Четверть. 21. Знакомство с языком Python (семинары). Семинар 8. Работа с файлами. Домашнее задание.

Задача 55:  
Создать телефонный справочник – файл должен иметь расширение ".txt".  
Использовать функции – программа не должна быть линейной.  
Справочник должен содержать данные: Фамилия, Имя, Отчество, Номер телефона.  
Реализовать в программе:  

    – Сохранение данных контакта в файл;  
    – Вывод данных;  
    – Поиск определенной записи по одной из характеристик, введённой пользователем – например, Имя или Фамилия;  
    – Возможность импорта и экспорта данных.  

Задача 38:  
Дополнить телефонный справочник функционалом:  

    – Копирование данных из одного файла в другой, пользователь выбирает запись для копирования вводом порядкового номера контакта;
    – Изменение данных контакта, пользователь выбирает запись для изменения вводом данных одного из параметров контакта – например, Имя или Фамилия (изменять же может данные другого параметра, выбранной записи);
    – Удаление контакта, пользователь выбирает запись для удаления вводом данных одного из параметров контакта – например, Имя или Фамилия.

Решение – Декомпозиция задачи (разложение на подзадачи – разбиваем сложную задачу на несколько простых):

0. Создать интерфейс пользователя:  
    0.1. Добавить контакт;  
    0.2. Показать весь телефонный справочник;  
    0.3. Найти контакты;  
    0.4. Импорт всех данных;  
    0.5. Экспорт всех данных;  
    0.6. Импорт контакта;  
    0.7. Экспорт контакта;  
    0.8. Изменить контакт;  
    0.9. Удалить контакт;  
    0.10. Выход.  
1. Создать файл для телефонного справочника, если файла не существует:  
    1.1. Открыть файл в режиме добавления данных (a) – append;  
    1.2. Записать в файл пустую строку.  
2. Записать в файл данные контакта:  
    2.1. Ввести все данные для контакта: Фамилия, Имя, Отчество, Номер телефона, Адрес (пользовательский ввод);  
    2.2. Подготовить данные для сохранения в файл;  
    2.3. Открыть файл в режиме добавления данных (a) – append;  
    2.4. Записать данные в файл.  
3. Вывести все контакты на экран:  
    3.1. Открыть файл в режиме чтения (r) – read;  
    3.2. Прочитать все данные из файла;  
    3.3. Вывести полученные данные на экран.  
4. Найти записи по заданным параметрам, и вывести их на экран:  
    4.1. Ввести параметр поиска (пользовательский ввод);  
    4.2. Ввести данные для поиска по выбранному параметру (пользовательский ввод);  
    4.3. Открыть файл в режиме чтения (r) – read;  
    4.4. Прочитать все данные из файла;  
    4.5. Разбить эти данные на отдельные контакты;  
    4.6. Сохранить список контактов в программе;  
    4.7. Разбить контакт на список параметров;  
    4.8. Найти контакты по указанным данным в заданном параметре;  
    4.9. Вывести на экран найденные контакты.  
5. Импортировать все контакты из другого файла:  
    5.1. Ввести имя импортируемого файла (пользовательский ввод);  
    5.2. Проверить наличие импортируемого файла (если файл не существует – вывести сообщение об этом);  
    5.3. Открыть импортируемый файл в режиме чтения (r) – read;  
    5.4. Прочитать все данные из импортируемого файла;  
    5.5. Сохранить прочитанные данные в программе;  
    5.6. Открыть файл справочника в режиме добавления данных (a) – append;  
    5.7. Записать импортированные данные в файл справочника.  
6. Экспортировать все контакты в другой файл:  
    6.1. Ввести имя файла для экспорта справочника в него (пользовательский ввод);  
    6.2. Открыть файл справочника в режиме чтения (r) – read;  
    6.3. Прочитать все данные из файла справочника;  
    6.4. Сохранить прочитанные данные в программе;  
    6.5. Открыть файл для экспорта в режиме добавления данных (a) – append;  
    6.6. Записать полученные из справочника данные в файл для экспорта.  
7. Импортировать контакт из другого файла по номеру строки:  
    7.1. Ввести имя файла для импорта контакта из него (пользовательский ввод);  
    7.2. Проверить наличие такого файла (если файл не существует – вывести сообщение об этом);  
    7.3. Вывести все контакты из указанного файла на экран;  
    7.4. Ввести порядковый номер импортируемого контакта;  
    7.5. Открыть указанный файл в режиме чтения (r) – read;  
    7.6. Прочитать все данные из этого файла;  
    7.7. Разбить полученные данные на отдельные контакты;  
    7.8. Сохранить список контактов в программе;  
    7.9. Проверить не выходит ли заданный порядковый номер за границы длинны списка;  
    7.10. Открыть файл справочника в режиме добавления данных (a) – append;  
    7.11. Записать полученный из списка по заданному номеру контакт в файл справочника.  
8. Экспортировать контакт в другой файл по номеру строки:  
    8.1. Ввести имя файла для экспорта контакта в него (пользовательский ввод);  
    8.2. Ввести порядковый номер экспортируемого контакта;  
    8.3. Открыть файл справочника в режиме чтения (r) – read;  
    8.4. Прочитать все данные из файла справочника;  
    8.5. Разбить эти данные на отдельные контакты;  
    8.6. Сохранить список контактов в программе;  
    8.7. Проверить не выходит ли заданный порядковый номер за границы длинны списка;  
    8.8. Открыть файл для экспорта контакта в режиме добавления данных (a) – append;  
    8.9. Записать полученный из списка по заданному номеру контакт в файл для экспорта.  
9. Изменить контакт:  
    9.1. Ввести параметр для поиска изменяемого контакта (пользовательский ввод);  
    9.2. Ввести данные для поиска изменяемого контакта по выбранному параметру (пользовательский ввод);  
    9.3. Открыть файл справочника в режиме чтения (r) – read;  
    9.4. Прочитать все данные из файла справочника;  
    9.5. Разбить эти данные на отдельные контакты;  
    9.6. Сохранить список контактов в программе;  
    9.7. Разбить контакт на список параметров;  
    9.8. Найти контакт по указанным данным в заданном параметре;  
    9.9. Вывести на экран найденный контакт;  
    9.10. Подтвердить или отменить изменение найденного контакта;  
    9.11. Ввести параметр для изменения в найденном контакте (пользовательский ввод);  
    9.12. Ввести новые данные для изменяемого параметра найденного контакта (пользовательский ввод), и сохранить их в список параметров;  
    9.13. Объединить изменённый список параметров в контакт, и сохранить его список контактов;  
    9.14. Открыть файл справочника в режиме перезаписи данных (w) – write;  
    9.15. Объединить изменённый список контактов в один массив данных;  
    9.16. Записать эти данные в файл справочника.  
10. Удалить контакт:  
    10.1. Ввести параметр для поиска удаляемого контакта (пользовательский ввод);  
    10.2. Ввести данные для поиска удаляемого контакта по выбранному параметру (пользовательский ввод);  
    10.3. Открыть файл справочника в режиме чтения (r) – read;  
    10.4. Прочитать все данные из файла справочника;  
    10.5. Разбить эти данные на отдельные контакты;  
    10.6. Сохранить список контактов в программе;  
    10.7. Разбить контакт на список параметров;  
    10.8. Найти контакт по указанным данным в заданном параметре;  
    10.9. Вывести на экран найденный контакт;  
    10.10. Подтвердить или отменить удаление найденного контакта;  
    10.11. Удалить найденный контакт из списка контактов;  
    10.12. Открыть файл справочника в режиме перезаписи данных (w) – write;  
    10.13. Объединить изменённый список контактов в один массив данных;  
    10.14. Записать эти данные в файл справочника.  
