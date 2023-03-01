import asyncio

math_expression = input('Введите математическое выражение: ')
async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    print(f'Математическое выражение: {message}')
    writer.write(message.encode())
    data = await reader.read(100)
    print(f'Результат выражения: {data.decode()}')
    writer.close()

asyncio.run(tcp_echo_client(math_expression))