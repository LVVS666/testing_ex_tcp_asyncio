import asyncio
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename="py_log_client.log", filemode="w")

math_expression: str = input('Введите математическое выражение: ')
dict_math_json: dict = {'expressions': math_expression}

async def tcp_echo_client(message:dict):
    '''Отправка запроса на сервер и получение ответа'''
    try:
        reader, writer= await asyncio.open_connection(
        '127.0.0.1', 8888)
        logging.info(f' Соединение с сервером успешно {datetime.now()}')
        print(f'Математическое выражение: {dict_math_json["expressions"]}')
        json_message: object = json.dumps(message).encode()
        writer.write(json_message)
        request: object = await reader.read(100)
        request_data: dict = json.loads(request.decode())
        if 'invalid expression' not in request_data["answer"]:
            logging.info(f'Вычисления проведены удачно: {datetime.now()}')
            print(f'Результат выражения: {request_data["answer"]}')
            writer.close()
        else:
            logging.warning(f'Были отправлены некоректные данные, вычисление не выполнено: {datetime.now()}')
            print('Были отправлены некоректные данные, вычисление не выполнено')
            writer.close()
    except ConnectionRefusedError as e:
        logging.critical(f' Соеденение с сервером не установлено {datetime.now()}')

asyncio.run(tcp_echo_client(dict_math_json))
