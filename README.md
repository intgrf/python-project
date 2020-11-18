## Список запланированных задач

### О проекте
Реализация списка запланированных дел на Python с использованием Flask и SQLAlchemy. Для разметки страниц используются HTML-шаблоны. Для оформления элементов страниц используется Bootstrap.

Поддерживаемые функции:

- Добавление новой задачи в список
- Можно отметить, выполнена задача или нет
- Редактирование названия задач
- Добавление описания к задачам
- Удаление задач из списка

Вся информация о задачах хранится в базе данных.

### Структура проекта

1. Логика приложения находится в файле `app.py`
2. Папка `static` содержит файлы Bootstrap с CSS-стилями оформления страниц.
3. Папка `templates` содержит HTML-шаблоны страниц.
4. Файлы `Dockerfile`, `docker-compose.yml`, `requirements.txt` необходимы для сборки докер-контейнера.

### Запуск

Чтобы запустить проект:

1. Клонируйте репозиторий

2. Находясь в директории репозитория, выполните в терминале `docker-compose up`
