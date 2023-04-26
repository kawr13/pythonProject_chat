HELP = '''
help - Напечатать справку по программе.
add - добавить задачу
show - напечатать все добавленный задачи.'''

tasks = {}

run = True

while run:
    command = input('Введите комманду: ')
    if command == 'help':
        print(help)
    elif command == 'show':
        s = input("Введите дату задачи: ")
        if s in tasks.keys():
            print(f'{s}: {tasks[s]}')
        elif s == 'все':
            for key, value in tasks.items():
                print(f'{key}: {value} ')
        else:
            print("Задача не найдена")
    elif command == 'add':
        date = input("Введите дату задачи: ")
        task = input('введите название задачи: ')
        task_exists = False
        for key, value in tasks.items():
            if key == date:
                if task in value:
                    if task == value:
                        print("Задача уже существует")
                        task_exists = True
                        break
        else:
            tasks[date] = task
            print("Задача добавлена")
    elif command == 'выход':
        run = False
        print("Досвиданье")
    else:
        print("Неизвестная комманда")

print(str(tasks))



