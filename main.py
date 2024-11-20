import asyncio
from os import startfile
import platform
import random
import string
import sys
import discord
import json
import datetime
from discord.ext import commands
import fade
import time
import psutil
import requests  # Importa la librería requests para hacer solicitudes HTTP


ascii_art = """
██╗███╗   ██╗███████╗██╗███╗   ██╗██╗████████╗███████╗██╗   ██╗ ██████╗ ██╗██████╗       ██╗      █████╗ ██████╗ 
██║████╗  ██║██╔════╝██║████╗  ██║██║╚══██╔══╝██╔════╝██║   ██║██╔═══██╗██║██╔══██╗      ██║     ██╔══██╗██╔══██╗
██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║██║   ██║   █████╗  ██║   ██║██║   ██║██║██║  ██║█████╗██║     ███████║██████╔╝
██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██║   ██║   ██╔══╝  ╚██╗ ██╔╝██║   ██║██║██║  ██║╚════╝██║     ██╔══██║██╔══██╗
██║██║ ╚████║██║     ██║██║ ╚████║██║   ██║   ███████╗ ╚████╔╝ ╚██████╔╝██║██████╔╝      ███████╗██║  ██║██████╔╝
╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚══════╝  ╚═══╝   ╚═════╝ ╚═╝╚═════╝       ╚══════╝╚═╝  ╚═╝╚═════╝

    ╔══════════════════════════════════════════════════════════════════════════════════════════╗
    {:^92} 
    ╚══════════════════════════════════════════════════════════════════════════════════════════╝
"""
def jugando():
    return discord.Activity(
        type=discord.ActivityType.playing, 
        name="PornHub",  # El nombre del juego
        assets=dict(
            large_image='mp:external/c6HJKi5m6KDKG6weTzeBsiW2s4UB_DXoP-fgHlgcfSc/https/i.postimg.cc/d0N4ctPg/images.png?format=webp&quality=lossless',  # Enlace directo de la imagen grande
            large_text='Que Miras??',  # Este es el texto cuando el usuario pasa el ratón sobre el icono grande
            small_image='mp:external/ZPTZtl0Lwpa0bu-piHmM1Pz3l9FRWNq28Oo4Zdgf9N8/https/i.postimg.cc/76CXH8qh/59i343110hwd1.gif',  # Enlace directo de la imagen pequeña
            small_text='AmongUs culo'))
def twitch():
    return discord.Streaming(name='InfiniteVoid', url='https://www.twitch.tv/infinitevoidlab', details='https://github.com/InfiniteVoid-lab')

def spoty():
    return discord.Activity(type=discord.ActivityType.listening,
                            name='ロボットハート',
                            details='Yunomi; Kizuna AI',
                            state='未来茶屋 (vol.1)',
                            start=datetime.datetime.utcnow(),
                            end=datetime.datetime.utcnow() + datetime.timedelta(minutes=2, seconds=56),
                            assets=dict(large_image='spotify:ab67616d00001e02768629f8bc5b39b68797d1bb',
                                        large_text='未来茶屋 (vol.1)',
                                        small_image='spotify:ab6761610000f178049d8aeae802c96c8208f3b7',
                                        small_text='Spotify'))

def yt():
    return discord.Activity(type=discord.ActivityType.watching,
                            name='la bolsa de valores',
                            url='https://github.com/InfiniteVoid-lab',
                            details='Working with it',
                            state='Trading',
                            assets=dict(large_image='mp:external/3ABbtCs-WezIDycFR3r0Gs-uOuPd5hCZuUpPN2-VyUk/https/www.likeinteligente.org/wp-content/uploads/2023/10/68747470733a2f2f6d656469612e74656e6f722e636f6d2f7a7a6e746d325f3942336741414141432f6861636b65722e676966.gif',
                                        large_text='Youtube',
                                        small_image='mp:external/Wga9Z7hbBMMsvrPfjT4JY2hTTc8hYYHSdAtuSsZPbZw/https/media.tenor.com/qJRMLPlR3_8AAAAi/maxwell-cat.gif?width=450&height=301',
                                        small_text='Bot',))

with open('config.json') as file:
    config = json.load(file)

token = config['token']
prefix = config['prefix']

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, self_bot=True, intents=intents)

# Definir startfile al inicio
startfile = time.time()  # Este es el momento en que el bot se inicia

PIPES = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"

# Lista de opciones disponibles en el menú
menu_options = ['spotify', 'youtube', 'twitch', 'juego', 'ninguno']

descripciones_sobre_mi = [
    "¡Hola! Soy un bot genial.",
    "Puedes preguntarme cualquier cosa.",
    "¡Disponible para ayudar!",
    "¡Estoy en modo animación! 🎉"
]

# Función asincrónica para cambiar la descripción de "Sobre mí"
async def cambiar_sobre_mi():
    indice = 0
    while True:
        nueva_descripcion = descripciones_sobre_mi[indice]
        try:
            # Cambia la descripción del perfil del bot
            await bot.user.edit(about_me=nueva_descripcion)
        except Exception as e:
            print(f"Error al cambiar la descripción: {e}")

        # Espera X segundos antes de cambiar la descripción nuevamente
        await asyncio.sleep(10)  # Cambia el número 10 por la cantidad de segundos que prefieras

        # Actualiza el índice para la siguiente descripción
        indice = (indice + 1) % len(descripciones_sobre_mi)

@bot.command()
async def rich(ctx):
    # Presenta las opciones al usuario
    options_text = "\n".join(f"{index + 1}. {option.capitalize()}" for index, option in enumerate(menu_options))
    menu_message = await ctx.send(f"Selecciona una opción:\n{options_text}")

    def check(message):
        # Verifica que el mensaje sea del mismo autor y esté en el mismo canal
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        # Espera la respuesta del usuario con un límite de tiempo
        response = await bot.wait_for('message', check=check, timeout=30.0)
        choice = response.content.strip().lower()

        if choice.isdigit():
            choice_index = int(choice) - 1  # Restamos 1 porque las opciones están indexadas desde 0 en Python
            choice = menu_options[choice_index]
        
        if choice in menu_options:
            await ctx.send(f"Configurando presencia para {choice.capitalize()}...")

            if choice == 'twitch':
                presenceData = twitch()
            elif choice == 'spotify':
                presenceData = spoty()
            elif choice == 'youtube':
                presenceData = yt()
            elif choice == 'juego':
                presenceData = jugando()  # Aquí el bot estará jugando
            elif choice == 'ninguno':
                presenceData = None  # Esto quitará la presencia actual
            else:
                await ctx.send("Opción no válida.")

            await bot.change_presence(activity=presenceData)
        else:
            await ctx.send("Opción no válida.")

    except asyncio.TimeoutError:
        await ctx.send("Se acabó el tiempo. Por favor, vuelve a ejecutar el comando.")

bot.remove_command('help')  # Desactiva el comando de ayuda predeterminado

@bot.command(name="help")
async def help(ctx):
    help_message = (
        "**Lista de Comandos:**\n\n"
        "❓ **!help** -- Muestra la lista de comandos disponibles.\n"
        "🌐 **!ping** -- Muestra el ping del bot.\n"
        "👑 **!rich** -- Personaliza tu perfil de Discord.\n"
        "🖼️ **!av** -- Muestra el avatar actual del bot.\n"
        "🪬 **!av_user** -- Muestra el avatar de otra persona(Solo funciona dentro de los servidores).\n"
        "✈️ **!avion** -- 9/11.\n"
        "💦 **!cum** -- CUM.\n"
        "🐱‍💻 **!geoip** -- Te da la informacion de cualquier IP que pongas.\n"
        "💻 **!serverinfo** -- Te muestra la informacion de cualqueir servidor.\n"
        "🔭 **!whois** -- Te da la informacion de cualquier usuario (Funciona mejor en servidores).\n"
        "💣 **!nuke** -- Para Raidear.\n"
        "📢 **!info** -- Informacion del del selfbot y de tu equipo.\n"
    )
    await ctx.send(help_message)

@bot.command()
async def av(ctx):
    avatar_url = str(ctx.bot.user.avatar_url)
    await ctx.send(f"Tu foto de perfil es: {PIPES}{avatar_url}")

@bot.command()
async def av_user(ctx):
    await ctx.send("Por favor, introduce el ID del usuario del cual deseas ver el avatar:")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        # Esperar a que el usuario envíe un ID
        response = await bot.wait_for('message', check=check, timeout=30.0)
        user_id = response.content.strip()

        # Intentar convertir el ID a un entero
        user_id = int(user_id)

        # Intentar buscar al usuario en el servidor
        user = ctx.guild.get_member(user_id)

        if user is None:
            # Si no se encuentra en el servidor, intenta buscarlo globalmente
            try:
                user = await bot.fetch_user(user_id)
            except discord.NotFound:
                await ctx.send("No se encontró ningún usuario con ese ID.")
                return

        # Obtener la URL del avatar
        avatar_url = str(user.avatar_url) if user.avatar else "Este usuario no tiene un avatar."

        await ctx.send(f"El avatar de {user.name} es: {PIPES}{avatar_url}")

    except ValueError:
        await ctx.send("Por favor, introduce un ID válido.")
    except asyncio.TimeoutError:
        await ctx.send("Se acabó el tiempo. Por favor, vuelve a ejecutar el comando.")

@bot.command()
async def stats(ctx):
    online_members = len([member for member in ctx.guild.members if member.status != discord.Status.offline])
    await ctx.send(f"📊 Hay {online_members} usuarios en línea de {ctx.guild.member_count} en este servidor.")

@bot.command()
async def avion(ctx):
    # Eliminar el mensaje del comando
    await ctx.message.delete()

    # Define los pasos de la animación
    frames = [
        "       ✈ 🏢🏢",# Primer frame
        "          ✈🏢🏢",# Segundo frame
        "           💥💥💥"# Tercer frame
    ]

    # Mostrar el primer frame
    message = await ctx.send(frames[0])
    
    # Iterar sobre cada frame, eliminando el anterior y enviando el siguiente
    for frame in frames[1:]:
        await asyncio.sleep(0.5)  # Pausa entre frames
        await message.delete()  # Eliminar el mensaje anterior
        message = await ctx.send(frame)  # Enviar el siguiente frame

@bot.command()
async def cum(ctx):
    # Eliminar el mensaje del comando
    await ctx.message.delete()

    # Secuencia de animación paso a paso (ajustada para evitar duplicación)
    frames = [
        "8=✊=D",          # Primer frame
        "8==✊D",          # Segundo frame
        "8=✊=D",          # Tercer frame
        "8=✊=D💦🥵"        # Cuarto frame
    ]

    # Mostrar el primer frame
    message = await ctx.send(frames[0])
    
    # Iterar sobre cada frame, eliminando el anterior y enviando el siguiente
    for frame in frames[1:]:
        await asyncio.sleep(0.5)  # Pausa entre frames
        await message.delete()  # Eliminar el mensaje anterior
        message = await ctx.send(frame)  # Enviar el siguiente frame

@bot.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '8.8.8.8'):
    await ctx.message.delete()  # Borra el mensaje que ejecutó el comando

    try:
        # Realiza la solicitud a la API de geolocalización en formato JSON
        r = requests.get(f'http://ip-api.com/json/{ipaddr}')
        
        # Verifica si la solicitud fue exitosa
        if r.status_code != 200:
            await ctx.send(f"[ERROR]: No se pudo obtener la información de la IP. Código de estado: {r.status_code}")
            return

        # Convierte la respuesta en JSON
        geo = r.json()

        # Verifica si la API devolvió un estado de éxito
        if geo.get('status') == 'fail':
            await ctx.send("[ERROR]: No se pudo obtener la geolocalización de la IP. La IP podría no ser válida.")
            return

        # Asegúrate de que todos los campos necesarios tengan datos
        ip_info = f"""
        **Información de Geolocalización de la IP:**
        
        **IP**: {geo['query']}
        **País**: {geo['country']}
        **Región**: {geo['regionName']}
        **Ciudad**: {geo['city']} ({geo['zip']})
        **Latitud y Longitud**: {geo['lat']} - {geo['lon']}
        **ISP**: {geo['isp']}
        **Organización**: {geo['org']}
        **Zona Horaria**: {geo['timezone']}
        **AS**: {geo['as']}
        """
        
        # Enviar la información como un mensaje de texto a Discord
        await ctx.send(ip_info)

    except requests.exceptions.RequestException as e:
        await ctx.send(f"[ERROR]: Hubo un error al realizar la solicitud: {e}")
    except Exception as e:
        await ctx.send(f"[ERROR]: {e}")

@bot.command()
async def serverinfo(ctx):
    try:
        # Obtén los datos básicos del servidor
        guild = ctx.guild
        guild_name = guild.name
        guild_id = guild.id
        guild_created_at = guild.created_at.strftime("%d/%m/%Y")
        member_count = guild.member_count
        owner = guild.owner
        channel_count = len(guild.channels)
        
        # Verificar nivel de boost (Nitro)
        nitro_level = guild.premium_tier
        nitro_boosts = guild.premium_subscription_count

        # Construye el URL completo del icono, y verifica si es GIF
        if guild.icon:
            icon_format = "gif" if guild.is_icon_animated() else "png"
            icon_url = f"https://cdn.discordapp.com/icons/{guild_id}/{guild.icon}.{icon_format}"
        else:
            icon_url = "No tiene icono."

        # Construir el mensaje de información del servidor
        server_info = f"""
        **Información del Servidor:**
        
        **Nombre del Servidor:** {guild_name}
        **ID del Servidor:** {guild_id}
        **Fecha de Creación:** {guild_created_at}
        **Número de Miembros:** {member_count}
        **Dueño del Servidor:** {owner}
        **Número de Canales:** {channel_count}
        **Nivel de Nitro (Boost):** {nitro_level} ({nitro_boosts} Boosts)
        **URL del Icono:** {icon_url}
        """

        # Envía el mensaje al canal
        await ctx.send(server_info)

    except Exception as e:
        await ctx.send(f"[ERROR]: Hubo un error al enviar la información del servidor: {e}")

@bot.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()

    # Si no se especifica un usuario, se usará el que ejecutó el comando
    if user is None:
        user = ctx.author

    # Formato de fecha
    date_format = "%a, %d %b %Y %I:%M %p"

    # Información del usuario
    info = [
        f"**Usuario:** {str(user)}",
        f"**ID:** {user.id}",
        f"**Cuenta creada:** {user.created_at.strftime(date_format)}"
    ]

    # Si el mensaje está en un servidor
    if ctx.guild is not None:
        info.append(f"**Se unió al servidor:** {user.joined_at.strftime(date_format)}")

        # Calcula la posición de ingreso en el servidor
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        join_position = members.index(user) + 1
        info.append(f"**Posición de ingreso:** {join_position}")

        # Roles
        if len(user.roles) > 1:
            roles = ' '.join([r.mention for r in user.roles][1:])
            info.append(f"**Roles [{len(user.roles) - 1}]:** {roles}")

        # Permisos
        permissions = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        info.append(f"**Permisos:** {permissions}")

    # Enviar la información como mensaje de texto
    await ctx.send("\n".join(info))



@bot.command()
async def nuke(ctx, verification_code: int = None):
    """
    Borra todos los roles y canales de un server y crea 250 canales y roles llamado raid
    """
    await ctx.message.delete()
    random_number = random.randint(1000, 9999)
    confirm_message = await ctx.send(f"Para confirmar la acción, escribe el siguiente número aleatorio de 4 dígitos: `{random_number}`. Escribe 'si' seguido del número para continuar o cualquier otra cosa para cancelar.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() == f"si {random_number}"

    try:
        await bot.wait_for("message", check=check, timeout=30)
    except asyncio.TimeoutError:
        await confirm_message.edit(content="Tiempo de espera agotado. Acción cancelada.")
        return

    # Eliminar todos los canales del servidor
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass

    # Eliminar todos los roles del servidor
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

    # Intentar cambiar la información del servidor
    try:
        await ctx.guild.edit(
            name="".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32))),
            description="You have been raided by Super",
            reason="You have been raided by Super",
            icon=None,
            banner=None
        )
    except:
        pass

    # Crear 250 canales de texto con el nombre "raid <3"
    for _i in range(250):
        await ctx.guild.create_text_channel(name="Super")

    # Crear 250 roles con el nombre "raid <3" y colores aleatorios
    for _i in range(250):
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        await ctx.guild.create_role(name="Super", color=randcolor)

@bot.command()
async def info(ctx):
    """
    Comando para mostrar estadísticas del equipo y selfbot.
    """
    await ctx.message.delete()

    python_version = sys.version
    discord_version = discord.__version__
    os_platform = platform.system()
    os_info = f"{platform.system()} {platform.release()}"
    guild_count = len(bot.guilds)
    member_count = sum(len(guild.members) for guild in bot.guilds)

    # Use psutil to get CPU and memory information
    cpu_cores = psutil.cpu_count(logical=False)
    ram_info = psutil.virtual_memory()
    cpu_info = platform.processor()

    # Calculate uptime in seconds
    uptime_seconds = round(time.time() - startfile)
    uptime_str = str(datetime.timedelta(seconds=uptime_seconds))    

    stats = (
        f"╔═══════════════════════════════════════════════════════════╗\n"
        f"║                                                                      Información del Selfbot\n"
        f"╠═══════════════════════════════════════════════════════════╣\n"
        f"║ 📌 Versión de Python: {python_version}\n"
        f"║ 📌 Versión de Discord.py: {discord_version}\n"
        f"║ 📌 Sistema Operativo: {os_platform} {platform.release()}\n"
        f"╠═══════════════════════════════════════════════════════════╣\n"
        f"║ 📍 Servidores activos: {guild_count}\n"
        f"╠═══════════════════════════════════════════════════════════╣\n"
        f"║ 🖥️ CPU: {cpu_info}\n"
        f"║ ⚡ Núcleos de CPU: {cpu_cores}║\n"
        f"║ 💻 RAM Total: {ram_info.total / (1024 ** 3):.2f} GB\n"  # Convertir bytes a gigabytes
        f"║ 📊 Uso de memoria: {ram_info.percent}%\n"
        f"║ ⏳ Tiempo de Actividad (Uptime): {uptime_str}\n"
        f"╚═══════════════════════════════════════════════════════════╝\n"
        f"                                                                       📡 Made by InfiniteVoid-lab 📡")

    await ctx.send(stats)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Tu ping es de: {round(bot.latency * 1000)}ms !')

@bot.event
async def on_ready():
    connected_info = f'{bot.user.name}'
    # Obtener la lista de amigos del bot (relaciones de tipo 1)
    friends = [relationship for relationship in bot.user.relationships if relationship.type == discord.RelationshipType.friend]

    # Obtener la lista de servidores en los que está el bot
    servers = bot.guilds

    # Reemplazar el marcador de posición en el arte ASCII con la información de conexión
    styled_ascii_art = ascii_art.format(f'Connected:{connected_info} | Servers:{len(servers)} | Friends:{len(friends)}')
    # Imprimir el arte ASCII estilizado usando fade
    print(fade.purplepink(styled_ascii_art))

    print('Presiona Ctrl + C para cerrar el bot.')

try:
    bot.run(token, bot=False)
except KeyboardInterrupt:
    print('Cerrando el bot manualmente.')