import asyncio
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename="py_log_server.log", filemode="w")

async def handle_echo(reader, writer):
    '''Обработка запроса от клиента и отправка ответа.'''
    request = (await reader.read(100))
    request_data = json.loads(request.decode())
    try:
        expressions_response = str(eval(request_data["expressions"]))
        response_json = {"answer": expressions_response}
        response_json_answer = json.dumps(response_json).encode()
        writer.write(response_json_answer)
        await writer.drain()
        writer.close()
    except NameError:
        response_json = {"answer": request_data["expressions"] + ' invalid expression'}
        response_json_answer = json.dumps(response_json).encode('utf8')
        writer.write(response_json_answer)
        await writer.drain()
        writer.close()

async def main():
    '''Запуск сервера'''
    try:
        logging.info(f'Сервер работает корректно : {datetime.now()}')
        server = await asyncio.start_server(
            handle_echo, '127.0.0.1', 8888)
        addr = server.sockets[0].getsockname()
        print(f'Host server: {addr[0]}'
              f'\nPort server: {addr[1]}')
        async with server:
            await server.serve_forever()
    except ConnectionRefusedError as e:
        logging.critical(f'Сервер не работает! : {datetime.now()}')
        server.close()

asyncio.run(main())
