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
        for key in tasks:
            if key == s:
                print(key, tasks[key])
                break
            elif s == 'все' or s == '':
                for key in tasks:
                    print(key, tasks[key])
                    break
            else:
                print("Задача не найдена")
                break
    elif command == 'add':
        date = input("Введите дату задачи: ")
        task = input('введите название задачи: ')
        tasks[date] = task
        print('Задача добавлена')
    elif command == 'выход':
        run = False
        print("Досвиданье")
    else:
        print("Неизвестная комманда")

print(str(tasks))



