##### Для начала я подготовил image для работы с моим питоновсикм кодом, взять его можно [здесь](https://hub.docker.com/search?q=pndf%2F&type=image) , и называется он "pndf/my-py".
##### Чтобы собрать образ "pndf/my-py" я использовал образ "ubuntu", запускал его в контейнере, доустанавливал туда python 3.8, curl, ping и другие необходимые библиотеки для работы моих программ, собранных в докер-контейнерах, после чего собирал образ с помощью команды 
```
docker commit ubuntu pndf/my-py
```
##### images "pndf/server" и "pndf/client" это собранные из "pndf/my-py" образы на основе Dockgile которые лежат в соответсвующих дерикториях.
##### Собирались они командами, приведенными ниже из соответствующих директорий
```
docker build -t pndf/client:latest
docker build -t pndf/server:latest
```
##### В данном проекте используется утилита docker-compose, из корневой директории 
##### запуск
```
docker-compose up -d
```
##### остановка
```
docker-compose down
```
>Запускаем клинет по адресу localhost:82, который запрашивает json c сервера,
> и изменяет в нем значение "user agent": .... и "machine": "server" на "machine": "client"
>, если сервер не доступен - выводит json вида
```
{
    "string": "server not available now",
    "machine": "client"
}
```