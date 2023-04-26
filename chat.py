from datetime import datetime

pass_users = {}

all_messages = []

chat_log = {
    'auther': 'Александр',
    'text': 'Привет',
    'time': datetime.now().strftime('%H:%M')
}
chat_log_2 = {
    'auther': 'Маша',
    'text': 'Привет, Саша',
    'time': datetime.now().strftime('%H:%M')
}
all_messages.append(chat_log)

all_messages.append(chat_log_2)

def add_message(author, text = None, password = None):
    chat_log = {
        'auther': author,
        'text': text,
        'password': password,
        'time': datetime.now().strftime('%H:%M')
    }
    all_messages.append(chat_log)
    chat_log_2 = {
        'auther': author,
        'text': text,
        'password': '123',
        'time': datetime.now().strftime('%H:%M')
    }
    all_messages.append(chat_log)


while True:
    print('Добро пожаловать в чат!')
    print('Для входа введите имена и пароли')
    print('Для резервнообмена введите "stop"')
    if input('для продолжения нажмите enter для выхода напишите n: ').lower().strip() == '':
        while True:
            name = input('Введите имя: ').lower()
            passw = input('Введите пароль: ')
            add_message(name, passw)
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
            run = True
            while run:
                msg = input('Введите сообщение: ')
                add_message(name, msg)
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


