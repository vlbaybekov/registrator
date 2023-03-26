from flask import Flask, request
from db import add_user
from datetime import datetime
import random
import string

app = Flask(__name__)

#Ручка для проверки сервиса, для дальнейшего мониторинга    
@app.route('/health', methods=['GET'])
def health():
    return 'OK', 200

#Основая ручка для регистрации пользователя, приходит post запрос с именем и фамилией
@app.route('/register', methods=['POST'])
def register_user():
    current_time = datetime.now().replace(microsecond=0)
    data = request.json
    uuid = uuid_generator(20)
    add_user(data['name'], data['surname'], uuid, current_time)
    return f'New user {data["name"]} {data["surname"]} has been added', 200

def uuid_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))