import asyncio, socket


def result_math(string):
    string = string.split()
    if string[1] == '+':
        return int(string[0]) + int(string[2])
    elif string[1] == '-':
        return int(string[0]) - int(string[2])
    elif string[1] == '*':
        return int(string[0]) * int(string[2])
    elif string[1] == '/':
        return int(string[0]) / int(string[2])
    else:
        return f'Не правильно составлено выражение'


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    message = result_math(message)
    writer.write(data)
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    async with server:
        await server.serve_forever()

asyncio.run(main())