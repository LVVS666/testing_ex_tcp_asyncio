import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    print(message)
    writer.write(message.encode())
    data = await reader.read(100)
    print(data.decode())
    writer.close()

asyncio.run(tcp_echo_client('10 + 10'))