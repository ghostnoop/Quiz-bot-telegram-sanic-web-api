.env для конфигурации. В ней указаны доступы к бд, токен бота и ник канала. 

Для запуска нужно перейти в папку /root/quiz/
Произвести команду для запуска окружения:
`source env/vin/activate` 

`python bot_start.py - для запуска бота`

`python api_start.py - для запуска апи`

ip:port/backcall - post запрос с телом 
```json
{
    "name":"quiz",
    "phone":"8199191"
}
```


ip:port/afterquiz - post запрос с телом 
```json
{
    "name":"quiz",
    "phone":"8199191",
    "parameter1":"test",
    "parameter2":100,
    "parameter3":"test3",
    "parameter4":1241515
}
```
