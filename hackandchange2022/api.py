import requests
import json
from pprint import pprint

def netmonet(phone_number,first_name):
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
        "firstName":first_name,
        "lastName":"Иванович",
        "phoneNumber" : phone_number,
    }
    user_code_inside = requests.post(reg_link,json = user_data,headers=headers)
    print(user_code_inside.text)
    user_code = json.loads(user_code_inside.text)["code"]
    print(user_code)
    return user_code

phone_number = "+79995269942"
first_name = "Иван"



print(netmonet(phone_number,first_name))
