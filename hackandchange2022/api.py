import requests
import json
from pprint import pprint

headers = {"Authorization":"Token OGFiODBiOGItZTJlMC00NDRkLTk1ZDktZTlhYmMzZTc4ZGE3OlRJWlN0bUxTMW1jZzZueVpHdldsT1hBM05GODBmVTZOS3FhajdPeEdr"}
link = "https://admin.netmonet.co/api/external/v1/workplace/list"
response = requests.get(link,headers = headers)

json_dict = json.loads(response.text)[0]
pprint(json_dict)
groups = json_dict["groups"]
id = groups[0]['id']
print(id)

reg_link = "https://admin.netmonet.co/api/external/v1/waiter/registration/data"
user_data ={
    "codeId":None,
    "sector":"tip",
    "isDuplicateCodesAllowed":None,
    "groupId":id,
    "firstName":"Иван",
    "lastName":"Иванович",
    "phoneNumber" : "+79995269942",
}
user_code_inside = requests.post(reg_link,json = user_data,headers=headers)
print(user_code_inside.text)
user_code = json.loads(user_code_inside.text)["code"]
print(user_code)


сергей по бэку.
саша по фронту.



бэк на джанго

встраиваемое

монетизация.


платеж без регистрации.

привелегированность клиентов тинькофф - им без комиссии.
ml
развернуть.

не баг а фича.

вывод сразу на карту.
как без регистрации.

связь от

контент
    парсится?

информацию о стримере можно получать из регистрации.
апи стримингового сервиса позволяет реализовать

я непонятно изъясняюсь.


обозначть проблему и решить её.
Мало времени у человека
статистика доли пользователей.

через сервис апи можно сделать виджет.

клиента сбербанка - можем в виджете предложить карту альфабанка.
интеграция с альфой.    Топ фича.

какие данные какие подтягивать.


интеграцию.
апишки от твича можно брать.
стример регистрируется - оставляет ссылку на стрим.


донатит.

жюри также будут оценивать монетизацию.

обдумать. Говорить конкретно.

знать какую продукт разрабатываем.



.
