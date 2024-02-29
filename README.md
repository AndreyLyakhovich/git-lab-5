# Лабораторная работа 5
Git advanced workshop

## Предварительные требования:

1. Основы работы с Git (лабораторная работа по введению в Git).
2. Установленный Git на локальной машине.


## Введение

1. Создание репозитория на GitHub:

    Зайдите в свою учетную запись GitHub и создайте новый репозиторий, например, с именем git-practice.
    Скопируйте URL вашего репозитория.

2. Клонирование репозитория:

    ![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/clone.jpeg)

3. Добавление файла:

    ![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/fcommit.jpeg)

4. Создание ветки:

    Создал ветку feature-branch

5. Отредактируйте файл example.txt, добавив еще текст.

    Добавил отредактированный файл example.txt

6. Слияние изменений:

    ![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/merge.jpeg)

7. Завершение:

    Изменения успешно слиты

## Работа с ветками

1. Создайте новый текстовый файл с базовой структурой книги, например:

Создал новый текстовый файл book.txt

2. Создайте ветку "feature-login" для разработки новой функциональности:

Создал ветку feature-login

3. Внесите изменения в файл:

   Внёс изменения в файл book.txt

```
# Название книги

## Глава 1: Введение
Здесь будет введение в тему книги.

## Глава 2: Основы Git
Основные понятия и команды Git.

## Глава 3: Вход в систему
Раздел по новой функциональности входа в систему.
```

4. Завершите изменения, закоммитьте их и отправьте ветку на GitHub:

Закоммитил изменения

## Работа с удаленным репозиторием

1. Переключитесь на основную ветку (main) и внесите изменения:

```
git checkout main
```

2. Внесите изменения в основной ветке (например, добавьте описание книги):

   Изменил файл book.txt

```
# Название книги: Приключения в мире Git

## Глава 1: Введение
Здесь будет введение в удивительный мир Git.

## Глава 2: Основы Git
Основные понятия и команды Git.

```

3. Закоммитьте изменения и отправьте их на GitHub:

   Закоммитил изменения и отправил на гитхаб

```
git add <filename>
git commit -m "Изменено название книги и введение"
git push origin main

```


## Моделирование конфликта

1. Вернитесь в ветку "feature-login" и внесите изменения в том же участке:

```
git checkout feature-login
```

2. Измените главу 2 в файле

```
# Название книги: Приключения в мире Git

## Глава 1: Введение
Здесь будет введение в удивительный мир Git.

## Глава 2: Основы Git и магия конфликтов
Основные понятия и команды Git, а также волшебство разрешения конфликтов.

```

3. Закоммитьте изменения и отправьте их на GitHub:

```
git add README.md
git commit -m "Добавлен раздел о магии конфликтов"
git push origin feature-login

```

## Разрешение конфликта

1. Вернитесь в основную ветку и попробуйте слить изменения:

```
git checkout main
git pull origin main
```

2. Возникнет конфликт. Разрешите его в файле

Возник конфликт

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/conflict1.jpeg)

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/conflict2.jpeg)

3. Разрешите конфликт, удалив метки и оставив нужные изменения:

Удалил метки, разрешил конфликт

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/conflictResolved.jpeg)

4. Закоммитьте разрешение конфликта и отправьте изменения на GitHub:

Закоммитил разрешение конфликта и отправил на гитхаб

## Автоматизация проверки формата файлов при коммите

Хорошо, предположим, у вас есть задача автоматизировать проверку формата файлов при коммите с использованием Git Hooks. Давайте создадим простую задачу и решение для этого случая.

1. Задача

Перед каждым коммитом необходимо автоматически проверять, чтобы все .txt файлы в репозитории соответствовали определенному формату.

2. Решение

Создал файл check_format.sh, который проверят являются ли файлы формата .txt Добавил его в пре-коммиты, дав разрешение на исполнение файла.

```
#!/bin/bash

for file in *; do 
	if [[ $file != *.txt ]]
	then 
		echo "$file is not a .txt"
	else 
		if [[ $file == *.txt ]]
		then
			echo "$file is a .txt"
		fi
	fi
done;
```

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/pre-commits.jpeg)

## Использование Git Flow в проекте

Задача: интегрировать Git Flow в проект для управления циклом разработки, создания релизов и управления hotfixes. 
Предположим, у вас есть задача на создание новой функциональности для вашего проекта с использованием Git Flow. Давайте рассмотрим конкретный пример.

1. Убедитесь, что Git Flow установлен на локальной машине:

```
sudo apt-get install git-flow
```

2. В корне репозитория выполните инициализацию Git Flow. Создайте ветку для новой функциональности "task-management":

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/flow1.jpeg)

3. Внесите изменения в код для добавления функционала управления задачами (например, в файл task_manager.py):

```
print('WELCOME TO YOUR TASK MANAGER!')

filename = input('What would you like your filename to be: \n(Please type \'.txt\' at the end of the name)');

tasks = []
with open(filename, 'w+') as f:
	prompt = 'Please enter what you need to do: \n(separated by commas and a space. Ex: laundry, clean) \n When you are done puting in tasks please press enter and type \'exit\' '
	user_input = f.write(input(prompt).strip())

while (user_input != 'exit'):
    tasks.append(user_input)
    user_input = input(prompt).strip()
    f.write(user_input)

tasks.sort()

print('\nAlphabetical order:')
for task in tasks:
    print(task)
```

Выполните коммит изменения по мере разработки:

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/flow2.jpeg)

4. После завершения разработки функции завершите фичу и объедините ее с основной веткой:

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/flow3.jpeg)

5. Переключитесь на ветку "develop" и начните создание релиза. Внесите изменения, связанные с релизом (например, обновите версию в файле version.txt):

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/flow4.jpeg)

7. Завершите релиз и объедините его с ветками "develop" и "main":

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/flow5.jpeg)

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/flow7.jpeg)

11. Завершение работы и отправка изменений на удаленный репозиторий. Отправьте изменения на удаленный репозиторий:

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/5311b31e03a4147b0385163bd8a4f0a4c458e3cc/report/flow8.jpeg)

![](https://github.com/AndreyLyakhovich/git-lab-5/blob/0d11de11ed65c5cd6f79d00b67442d327eb9a875/report/flow9.jpeg)
