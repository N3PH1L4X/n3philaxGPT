import discord, openai, time

### Cambiar esto
openai.api_key = "apikey"
discord_token = "token"
canales_para_escuchar = [
    1198564142752215050
]





banner = """\n\n
            ████████        █████     ███████                     █████████ ███████████ ███████████
           ███░░░░███      ░░███     ░░░░░███                    ███░░░░░██░░███░░░░░██░█░░░███░░░█
 ████████ ░░░    ░██████████░███████ ████░███  ██████ █████ ███████     ░░░ ░███    ░██░   ░███  ░ 
░░███░░███   ██████░░███░░██░███░░██░░███░███ ░░░░░██░░███ ░░██░███         ░██████████    ░███    
 ░███ ░███  ░░░░░░██░███ ░██░███ ░███░███░███  ███████░░░█████░░███    █████░███░░░░░░     ░███    
 ░███ ░███ ███   ░██░███ ░██░███ ░███░███░███ ███░░███ ███░░░██░░███  ░░███ ░███           ░███    
 ████ ████░░████████░███████████ ████████████░░████████████ ████░░█████████ █████          █████   
░░░░ ░░░░░ ░░░░░░░░ ░███░░░░░░░ ░░░░░░░░░░░░░ ░░░░░░░░░░░░ ░░░░░ ░░░░░░░░░ ░░░░░          ░░░░░    
                    ░███                                                                           
                    █████        Implementacion de ChatGPT en bot de discord con Python
                   ░░░░░    Desarrollado por José López (n3philax) | https://github.com/N3PH1L4X/n3philaxGPT
\n\n"""

def enviarMensajeChatGPT(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

print(banner)

@client.event
async def on_ready():
    print(f'{client.user} se ha conectado a Discord!')

    print('\nInformacion de la sesion:')
    print(f"Usuario: {client.user.name}")
    print(f"ID: {client.user.id}")

    print("\nLista de servidores y IDs:")
    for guild in client.guilds:
        print(f'   - {guild.name} | {guild.id}\n')

    print("################## Iniciando lectura de mensajes ##################")

@client.event
async def on_message(message):
    if message.channel.id in canales_para_escuchar:
        print(f">>>> Mensaje de {message.author} recibido <<<<\n{message.content}\n")
        
        try:
            respuestaGPT = enviarMensajeChatGPT(prompt=message.content)
        except Exception as e:
            respuestaGPT = e

        canal = client.get_channel(message.channel.id)
        if message.author != client.user:
            await canal.send(respuestaGPT)
            

client.run(discord_token)
