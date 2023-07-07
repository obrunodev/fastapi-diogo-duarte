# Chapar pão
# Fritar hamburguer
# Montar o sanduiche
# Fazer o milk shake
from time import sleep, time
import asyncio


class SyncSpongeBob:
    def cook_bread(self):
        sleep(3)
    
    def cook_burguer(self):
        sleep(10)
    
    def mount_sandwich(self):
        sleep(5)
    
    def make_milkshake(self):
        sleep(8)
    
    def cook(self):
        self.cook_bread()
        self.cook_burguer()
        self.mount_sandwich()
        self.make_milkshake()


class AsyncSpongeBob:
    async def cook_bread(self):
        await asyncio.sleep(3)
    
    async def cook_burguer(self):
        await asyncio.sleep(10)
    
    async def mount_sandwich(self):
        await asyncio.sleep(5)
    
    async def make_milkshake(self):
        await asyncio.sleep(8)
    
    async def make_sandwich(self):
        await asyncio.gather(self.cook_bread(),
                             self.cook_burguer())
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mount_sandwich())
    
    async def cook(self):
        await asyncio.gather(self.make_sandwich(),
                             self.make_milkshake())
        

# EXECUTANDO BOB ESPONJA SINCRONO
# sync_sponge_bob = SyncSpongeBob()
# init_proccess = time()
# sync_sponge_bob.cook()
# finished_proccess = time()
# print(finished_proccess - init_proccess)

# EXECUTANDO BOB ESPONJA ASSINCRONO
async_sponge_bob = AsyncSpongeBob()
init_proccess = time()
asyncio.run(async_sponge_bob.cook())
finished_proccess = time()
print(finished_proccess - init_proccess)