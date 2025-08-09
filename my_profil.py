# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone_number = ''
email = ''
index = ''
other = ''
mailing_address = ''
# info entrepreneur
ogrnip = ''
inn = ''
checking_account = '' # расчетный счет
name_bank = ''
bik = ''
correspondent_account = ''
count = 0



def full_info_user(name_parameter, age_parameter, phone_number_parameter, email_parameter,
                   index_parameter, mailing_address_parameter, ogrnip_parameter, inn_parameter,
                   checking_account_parameter,
                   name_bank_parameter, bik_parameter,
                   correspondent_account_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_number_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс:', index_parameter)
    print('Адрес:', mailing_address_parameter,'\n')
    print('Информация о предпринимателе')
    print('ОГРНИП:', ogrnip_parameter)
    print('ИНН:', inn_parameter)
    print('Банковские реквизиты')
    print('Р/с:', checking_account_parameter)
    print('Банк:', name_bank_parameter)
    print('БИК:', bik_parameter)
    print('К/с:', correspondent_account_parameter)


def general_info_user(name_parameter, age_parameter, phone_number_parameter, email_parameter, index_parameter, mailing_address_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_number_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс:', index_parameter)
    print('Адрес:', mailing_address_parameter)
    if other:
        print('')
        print('Дополнительная информация:')
        print(other)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')
                phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in phone_number:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch

                email = input('Введите адрес электронной почты: ')
                index = int(input('Введите почтовый индекс: '))
                mailing_address = input('Введите почтовый адрес (без индекса): ')
                other = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input
                while True:
                    ogrnip = input('Введите ОГРНИП: ')
                    for i in ogrnip:
                        count += 1
                    if count != 15:
                        print('Ошибка: ОГРНИП содержит 15 цифр - попробуйте еще раз')
                        count *= 0
                    elif count == 15:
                        count *= 0
                        break
                inn = int(input('Введите ИНН: '))
                while True:
                    checking_account = input('Введите Расчетный счёт: ')
                    for i in checking_account:
                        count += 1
                    if count != 20:
                        print('Ошибка: Расчетный счет содержит 20 цифр - попробуйте еще раз')
                        count *= 0
                    elif count == 20:
                        count *= 0
                        break
                name_bank = input('Введите название банка: ')
                bik = int(input('Введите БИК: '))
                correspondent_account = int(input('Введите корреспондентский счет: '))
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone_number, email, index, mailing_address)

            elif option2 == 2:
                full_info_user(name, age, phone_number, email, index, mailing_address, ogrnip, inn, checking_account,
                               name_bank, bik, correspondent_account)

            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
