import os
import os.path as p
import sys


PATH = r'~/PycharmProjects'


def make_dir(lesson, task):
    for i in range(1, lesson + 1):
        os.mkdir(f'lesson_{i}')
        print(f'\nДиректория lesson_{i} создана')
        if task != 0:
            tasks = task
        else:
            tasks = int(input('Введите количество заданий: '))
        for j in range(1, tasks + 1):
            with open(f'lesson_{i}/task_{j}.py', 'w'):
                pass
            print(f'файл lesson_{i}/task_{j}.py создан.')


def make_proj(path):
    dir_new_project = input('Введите название нового проекта: ')
    try:
        os.mkdir(f'{path}/{dir_new_project}')
        os.chdir(f'{path}/{dir_new_project}')
        print(f'Проект {dir_new_project} создан\n')
    except OSError as e:
        print(e)
        if input('Такой проект уже существует. Создать проект с другим именем? (y/n)') == 'y':
            return make_proj(path)
        else:
            return False
    return True


def main():
    if os.name == 'posix' and p.isdir(p.expanduser(PATH)):
        base_dir = p.expanduser(PATH)
        if not make_proj(base_dir):
            print('Проект не был создан!')
            sys.exit(1)
        many_lesson = int(input('Введите количество уроков: '))
        if input('Количество заданий в уроках одинаково? (y/n): ') == 'y':
            many_task = int(input('Введите количество заданий: '))
            make_dir(many_lesson, many_task)
        else:
            make_dir(many_lesson, 0)


if __name__ == '__main__':
    main()
