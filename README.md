Технологии:

```Django```
```Nominatim```
```Open-Meteo```
```DaData```

Web-приложение, где пользователь вводит название города, и получает прогноз погоды в этом городе на ближайшее время.
Проект написан на Django, Nominatim используется для получения координат по городу, Open-Meteo используется для получения погоды на ближайшее время по координатам, DaData используется для подсказок при вводе города в поле ввода

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
