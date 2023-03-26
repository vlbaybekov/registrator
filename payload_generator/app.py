import random
import time
import requests
from config import URL

names = ['Vasiliy','Mikhail','Ivan','Konstantin','Aleksandr','Yuriy','Evgeniy','Dmitriy']
surnames = ['Krylov','Chekhov','Goncharov','Nekrasov','Nosov','Bunin','Andreev','Shmelev']

while True:
    requests_amount = random.randint(0,10)
    for request in range(requests_amount):
        sleep_time = random.randint(15,30)
        name_index = random.randint(0,7)
        surname_index = random.randint(0,7)
        requests.post(url = URL, json={
            "name": names[name_index],
            "surname": surnames[surname_index]
        })
    time.sleep(sleep_time)
        