# Десктопное приложение обрабатывающее данные помощью API
 Это приложение позволяет просматривать access.log из файла

 ## Установка и запуск
 1. Склонируйте репозиторий на свой компьютер
 2. Откройте код
 (- если вы запускаете код в Visual studio code откройте весь проект в одном окне, а папку api в другом
 - если запуск кода происходит в Pycharm используйте два разных терминала для основного проекта и API.py)
 3. Установите необходимые библиотеки (pip install ttkbootstrap, pip install flask, pip install requests, pip install tkinter, pip install sqlite3)
 4. Запустите itog.py

 ## Описание файлов проекта
 ### Основные файлы
 1. itog.py - файл запуска приложения.
 2. login.py - файл авторизация.
 3. reg.py - файл регистрации.
 4. logo.py - основной файл приложения.
 5. users.db - база данных содержащая зарегестрированных пользователей.
 6. logi.db - база данных содержащая логи.
 ### Файлы из папки api
 1. access_logs.log - файл с логами
 2. API.py - api для фильтрации
 3. log.json - файл с логами формата json
 
 ## Функционал приложения
 1. Во вкладке "База данных" отображена таблица с логами из файла
 2. Во вкладке "Фильтр по ip" осуществляется фильтрация по IP
 3. Во вкладке "Фильтр по ip с датой" осуществляется фильтрация по IP и дате
 4. Во вкладке "Фильтр по дате" осуществляется фильтрация по дате

 ## Язык программирования
 Python
