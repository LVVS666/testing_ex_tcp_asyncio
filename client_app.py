import asyncio
import json
import logging

logging.basicConfig(level=logging.INFO, filename="py_log_client.log",filemode="w")

math_expression = input('Введите математическое выражение: ')
dict_math_json = {'expressions': math_expression}

async def tcp_echo_client(message):
    try:
        reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
        logging.info("Соединение с сервером успешно")
        print(f'Математическое выражение: {dict_math_json["expressions"]}')
        json_message = json.dumps(message).encode()
        writer.write(json_message)
        request = await reader.read(100)
        request = json.loads(request.decode())
        print(f'Результат выражения: {request["answer"]}')
        writer.close()
    except ConnectionRefusedError:
        logging.critical('Соеденение с сервером не установлено')

asyncio.run(tcp_echo_client(dict_math_json))