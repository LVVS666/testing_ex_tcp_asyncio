import asyncio
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename="py_log_client.log", filemode="w")

math_expression: str = input('Введите математическое выражение: ')
dict_math_json: dict = {'expressions': math_expression}

async def tcp_echo_client(message:dict) -> str:
    '''Отправка запроса на сервер и получение ответа'''
    try:
        reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
        logging.info(f"Соединение с сервером успешно: {datetime.now()}")
        print(f'Математическое выражение: {dict_math_json["expressions"]}')
        json_message = json.dumps(message).encode()
        writer.write(json_message)
        request = await reader.read(100)
        request_data = json.loads(request.decode())
        print(f'Результат выражения: {request_data["answer"]}')
        writer.close()
    except ConnectionRefusedError as e:
        logging.critical(f'Соеденение с сервером не установлено {datetime.now()}')

asyncio.run(tcp_echo_client(dict_math_json))
