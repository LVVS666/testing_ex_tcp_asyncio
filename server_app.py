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
    request = (await reader.read(255)).decode('utf8')
    response = str(result_math(request))
    writer.write(response.encode('utf8'))
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    async with server:
        await server.serve_forever()

asyncio.run(main())