import asyncio

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

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    print(message)
    writer.write(message.encode())
    data = await reader.read(100)
    print(result_math(message))
    writer.close()

asyncio.run(tcp_echo_client('10 + 10'))