Практикум Python. Проект 1
Кузнецов Андрей Б05-323 

Графическое приложение: Клавиатурниый тренажер на python с tkinter.

После запуска тренировки приложение будет генерировать пользователю случайный текст, который ему надо будет напечатать в специальное окно ввода.
Это окно ввода не позволяет пользователю писать неправильные символы. Также введен подсчет статистики каждой тренировки пользователя: количество ошибок, процент ошибок, скорость печатанья и т.п. Эта статистика будет храниться между запусками тренировок.


Архитектура:
Папка texts:
Содержит архив текстов

Файл history.txt: 
Содержит информацию о предыдущих тренировках
 
Папка src:
Класс TextGenerator - генерирует пользователю случайный текст из архива. Имеет метод getText().
Класс Menu - начальное меню приложения. Имеет кнопку "Start", чтобы начать тренировку.
Класс ExampleBoard - виджет с текстом, который надо напечатать
Класс InputBoard - поле для ввода текста пользователем. Не дает пользователю вводить некорректные символы. Эта функция реализованна с помощью вспомогательного класса Checker, который имеет атрибуты text (текст который перепечатывает пользователь) и number_of_written_symbols (количество корректно введенных символов)
Класс StatsBoard - виджет со статистикой текущей тренировки, имеет атрибуты number_of_missclicks и метод get_percent_of_missclicks
Класс App - класс, в котором прописаны переходы между состяниями меню/тренировка/просмотр истории

Для того, чтобы запустить проект необходимо клонировать данный репозиторий, а затем из директории /src/ запустить файл main.py

