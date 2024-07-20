Технологии:

```Django```
```Open-Meteo```
```DaData```
```Nominatim```

Web-приложение, где пользователь вводит название города, и получает прогноз погоды в этом городе на ближайшее время.

В дополнении реализовано:
+ Подскаазки при вводе города

#### Установить зависимости
```
pip install -r requirements.txt
```
#### Установить токен DaData (для подсказок)
```
В файл app_metcast\static\app_metcast\scripts\suggestion.js:
var token = "YOUR_DADATA_API_KEY"
```
#### Запустить проект
```
python manage.py runserver
```
