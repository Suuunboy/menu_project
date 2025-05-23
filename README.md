# Menu

В приложении `menu_app` реализовано древовидное меню, выводимое через template tag и редактируемое из админки. Для демонстрации был создан шаблон `index.html`, включающий в себя 2 несвязанных между собой древовидных меню. Отображение реализовано с помощью динамического роутинга для удобства добавления новых пунктов меню.
![image](https://github.com/user-attachments/assets/d4aa0338-2462-4a25-b64c-f0816f428051)


---

## Удовлятворяет поставленным требованиям:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
