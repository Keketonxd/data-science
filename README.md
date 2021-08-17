### Методы сбора и обработки данных из сети Интернет

#### _Урок 1. Основы клиент-серверного взаимодействия. Парсинг API_
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

#### _Урок 2. Парсинг HTML. BeautifulSoup, MongoDB_

1. Необходимо собрать информацию по продуктам питания с сайта: https://roscontrol.com/category/produkti/#popup. Приложение должно анализировать несколько страниц сайта (вводим через input или аргументы).
Получившийся список должен содержать:

    - Наименование продукта.
    - Все параметры (Безопасность, Натуральность, Пищевая ценность, Качество)
    - Общую оценку
    - Сайт, откуда получена информация.

Общий результат можно вывести с помощью dataFrame через Pandas. Сохраните в json либо csv.

#### _Урок 3. Системы управления базами данных MongoDB и SQLite в Python_

1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, записывающую собранные вакансии в созданную БД.
2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы. (Для тех, кто делал росконтроль, вывести продукты с рейтингом выше, либо равным, чем введённый)
3. Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта.

#### _Урок 4. Парсинг HTML. XPath_

1. Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex.ru/news/. Для парсинга использовать XPath. Структура данных должна содержать:
    - название источника;
    - наименование новости;
    - ссылку на новость;
    - дата публикации.
2. Сложить собранные данные в БД


#### _Урок 5. Selenium_

Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
Логин тестового ящика: study.ai_172@mail.ru
Пароль тестового ящика: NextPassword172!?

#### _Урок 6. Scrapy_

1. Создать двух пауков по сбору данных о книгах с сайта labirint.ru
2. Каждый паук должен собирать:
    - Ссылку на книгу
    - Наименование книги
    - Автор(ы)
    -  Основную цену
    - Цену со скидкой
    - Рейтинг книги
3. Собранная информация дожна складываться в базу данных

