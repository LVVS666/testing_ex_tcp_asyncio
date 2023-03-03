import asyncio
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename="py_log_server.log", filemode="w")

async def handle_echo(reader, writer):
    '''Обработка запроса от клиента и отправка ответа.'''
    request: object = (await reader.read(100))
    request_data: dict = json.loads(request.decode())
    try:
        logging.info(f'Вычисления провелись удачно: {datetime.now()}')
        expressions_response: str = str(eval(request_data["expressions"]))
        response_json: dict = {"answer": expressions_response}
        response_json_answer: object = json.dumps(response_json).encode()
        writer.write(response_json_answer)
        await writer.drain()
        writer.close()
    except NameError:
        logging.warning(f' Невалидные данные для вычисления: {datetime.now()}')
        response_json: dict = {"answer": request_data["expressions"] + ' invalid expression'}
        response_json_answer: object = json.dumps(response_json).encode('utf8')
        writer.write(response_json_answer)
        await writer.drain()
        writer.close()

async def main():
    '''Запуск сервера'''
    try:
        logging.info(f' Сервер работает корректно : {datetime.now()}')
        server = await asyncio.start_server(
            handle_echo, '127.0.0.1', 8888)
        addr = server.sockets[0].getsockname()
        print(f'Host server: {addr[0]}'
              f'\nPort server: {addr[1]}')
        async with server:
            await server.serve_forever()
    except ConnectionRefusedError as e:
        logging.critical(f' Сервер не работает! : {datetime.now()}')
        server.close()

asyncio.run(main())
