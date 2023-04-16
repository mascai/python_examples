# coroutine

import asyncio


async def echo_server(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print("received %r from %r" % (message, addr))
    writer.close()

loop = asyncio.get_event_loop()
coro = loop.create_task(asyncio.start_server(echo_server, "127.0.0.1", 8888))
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    print("Stop program")

"""
>>> import socket
>>> s = socket.create_connection(("127.0.0.1", 8888))
>>> s.send(b"ping2")
5

Server prints
received 'ping2' from ('127.0.0.1', 51923)
received 'ping2' from ('127.0.0.1', 51927)
"""
