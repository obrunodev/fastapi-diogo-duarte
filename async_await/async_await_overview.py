import asyncio

async def soma(a, b):
    return a + b

async def mostra_soma(a, b):
    resultado = await soma(a, b)
    print(f'Resultado igual a {resultado}')
    

# Event loop
event_loop = asyncio.new_event_loop()
event_loop.run_until_complete(mostra_soma(57, 6))
