import asyncio

async def handle_echo(reader, writer):
    request = (await reader.read(255)).decode('utf8')
    try:
        response = str(eval(request))
        writer.write(response.encode('utf8'))
        await writer.drain()
        writer.close()
    except BaseException:
        response = request + ' невалидное выражение'
        writer.write(response.encode('utf8'))
        await writer.drain()
        writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Host server: {addr[0]}'
          f'\nPort server: {addr[1]}')
    async with server:
        await server.serve_forever()

asyncio.run(main())