if __name__ == "__main__":
    pass

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        #print(f'Message from {message.author}: {message.content}')
        if message.author.id != self.user.id:
            await message.reply(content=":)")
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('123')