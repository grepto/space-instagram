# Космический Инстаграм
Скрипт вытягивает фотографии запусков ракет SpaceX и снимки телескопа Hubble и публикует их в 
инстаграмм-аккаунте


### Как установить
В корне нужно создать файл `.env` и прописать в него строки с логином и паролем от инстаграм-аккаунта,
В параметре IMAGE_DIRECTORY нужно указать название папки в которую будут скачиваться изображения. 
В POSTED_IMAGES_FILE нужно указать название файла в который приложение будет записывать названия опубликованных
фотографий
В HUBBLE_API_URL нужно указать адрес API для получения изображений с телескопа HUBBLE. На момент последнего изменения
корректный адрес - http://hubblesite.org/api/v3
В SPACEX_API_URL нужно указать адрес API для получения изображений пусков ракет SPACEX. На момент последнего изменения
корректный адрес - https://api.spacexdata.com/v3/launches/66

Пример содержимого файла `.env`
```.env
INSTAGRAM_LOGIN=ваш_логин_в_инстаграмм
INSTAGRAM_PASSWORD=ваш_пароль_в_инстаграмм
IMAGE_DIRECTORY=images
POSTED_IMAGES_FILE=posted_images.txt
HUBBLE_API_URL=http://hubblesite.org/api/v3
SPACEX_API_URL=https://api.spacexdata.com/v3/launches/66
```

Скрипт использует следующие библиотеки
 - `requests` для выполения запросов к API SpaceX и Hubble
 - `instabot` для публикации фотографий в инстаграм
 - `python-dotenv` для получения значений настроек из файла `.env`
 
Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.