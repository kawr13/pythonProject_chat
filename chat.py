from datetime import datetime

pass_users = {}

while True:
    print('Добро пожаловать в чат!')
    print('Для входа введите имена и пароли')
    print('Для резервнообмена введите "stop"')
    if input('для продолжения нажмите enter для выхода напишите n: ').lower().strip() == '':
        while True:
            name = input('Введите имя: ').lower()
            passw = input('Введите пароль: ')
            if pass_users.get(name) == passw:
                print('Добро пожаловать')
                break
            elif name not in pass_users:
                pass_users[name] = passw
                print('Добро пожаловать')
                break
            else:
                print('Неверный логин или пароль')

        while True:
            all_messages = []
            chat_log = {
                'auther': 'Александр',
                'text': 'Привет',
                'time': datetime.now().strftime('%H:%M')
            }
            chat_log = {
                'auther': 'Маша',
                'text': 'Привет, Саша',
                'time': datetime.now().strftime('%H:%M')
            }
            run = True
            while run:
                msg = input('Введите сообщение: ')
                chat_log[name] = msg
                if msg == 'stop':
                    run = False
                else:
                    for key, value in chat_log.items():
                        print(f'Сообщения от {key}:')
                        print(f'{value}')

            choice = input('Хотите продолжить? (y/n): ')
            if choice == 'y':
                break
    else:
        break
else:
    input('Для выхода нажмите Enter')


